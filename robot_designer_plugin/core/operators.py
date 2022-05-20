# #####
# This file is part of the RobotDesigner of the Neurorobotics subproject (SP10)
# in the Human Brain Project (HBP).
# It has been forked from the RobotEditor (https://gitlab.com/h2t/roboteditor)
# developed at the Karlsruhe Institute of Technology in the
# High Performance Humanoid Technologies Laboratory (H2T).
# #####

# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####

# #####
#
# Copyright (c) 2016, FZI Forschungszentrum Informatik
#
# Changes:
#
#   2016-01-15: Stefan Ulbrich (FZI), Major refactoring. Integrated into complex plugin framework.
#
# ######

"""
This submodule provides the base class and decorators, and some functions for defining Blender :term:`operators` that
register automatically.
"""
import inspect

import bpy
from .config import PLUGIN_PREFIX, EXCEPTION_MESSAGE
from .logfile import log_callstack, log_callstack_last, operator_logger as logger
from .conditions import Condition
from .gui import InfoBox


def get_registered_operator(operator):
    """
    Helper function that gets the registered Blender :term:`operator` based on its ``bl_idname`` tag.

    :param operator: A subclass of :class:`RDOperator` class.
    :return: The actually callable operator function. One has to pass :term:`keyword arguments` that match the name
        of the classes attributes.
    """

    # logger.debug('For debug only')
    return getattr(getattr(bpy.ops, PLUGIN_PREFIX), operator.bl_idname.replace(PLUGIN_PREFIX + '.', ''))


class RDOperator(bpy.types.Operator):
    """
    Base class for the :term:`operators<operator>` in the RobotDesigner.

    :term:`Blender operators<operator>` are defined as :term:`class objects` derived from :class:`bpy.types.Operator`.
    A plugin must *register* these classes by calling :func:`bpy.utils.register_class` which causes blender to
    create a callable function *out of a method* (:meth:`bpy.types.Operator.execute`) that accepts
    :term:`keyword arguments <keyword argument>` that are bound to the class' attributes -- if they are
    subclasses
    of :class:`bpy.types.Property`. Note that the static method has not the same arguments and operates on its
    attributes.
    Finally, the operator is addressed to by its ID. For example:

    .. code-block:: python

        class NewOp(bpy.types.Operator):
            bl_label = "Description" # Obligatory
            bl_idname = "plugin_name.newop" # obligatory

            test = StringProperty() # A property. It's value is passed when calling the operator.

            def execute(self, context):
                self.report({INFO}, self.text)
                return {'FINISHED'}

        # ...

        bpy.utils.register(NewOp)

        # ...

        bpy.ops.plugin_name.newop(test="Hello World)


    This example show an operator that opens a window containing the message *"Hello World"*. While this is feasible
    for smaller plugins, what happens, if you have a lot of operators written, and you want to have code completion.
    What happens if you want to refactor the names of of the identifier or class attributes. While for the latter there
    is no simple solution available, the :mod:`robot_designer_plugin.core` provides this wrapper class with
    an additional ``run(**kwargs)`` method (that can---and should---be overridden to provide keyword completion).
    Furthermore, it provides decorators for automatically setting preconditions (that define the
    :meth:`bpy.types.Operator.poll` method) for automatic condition checking, logging functionality and post condition
    checking. Together with the :meth:`.pluginmanager.PluginManager.register` method, this makes developing faster (
    code completion,
    code navigation, less verbosity, ...) and safer.

    An examplary :term:`operator` looks like this:

    .. literalinclude:: ../../../resources/templates/operator.py
        :emphasize-lines: 7-11,16-18, 31-33, 60-62
        :lines: 50-111
        :linenos:

    A template is located in ``<RobotDesignerDirectory>/resources/templates/operator.py`` (where you should insert
    the path to the repository) that can be used to quickly write new operators.
    """

    _pre_conditions = {}
    """Dictionary set by the :meth:`PreConditions` decorator. Stores the :class:`.conditions.Condition` that are
    checked for each :class:`RDOperator` -based operator"""

    logger = logger
    """For convenience, every the operators share a logging instance."""

    @classmethod
    def poll(cls, context):
        """
        The :meth:`bpy.types.Operator.poll` class method is called every time, an operator is to be executed, but
        also when it is placed in a guy (it becomes greyed out). This method is defined in this base class and
        the checks are defined by a list of :class:`.conditions.Condition` derived classes that are given by
        the :meth:`Preconditions` decorator. Derived classes do not need to override this method and should
        call the parent's method otherwise.

        :param context: The actual Blender :term:`context`.
        :type context: :class:`bpy.types.Context`
        :return:
        """
        if cls in cls._pre_conditions:
            check, messages = Condition.check_conditions(*cls._pre_conditions[cls])
            if not check:
                cls.logger.debug("Unmet preconditions: \n{}".format(messages))
            return check
        return True

    @staticmethod
    def pass_keywords():
        """
        Helper function that extracts the arguments of the callee (must be a (class) method) and returns them.

        Credits to `Kelly Yancey <http://kbyanc.blogspot.de/2007/07/python-aggregating-function-arguments.html>`_
        """

        args, _, _, locals = inspect.getargvalues(inspect.stack()[1][0])
        args.pop(0)
        kwargs = {i: j for i, j in locals.items() if i in args}
        return kwargs

    @classmethod
    def run(cls, **kwargs):
        """
        Enables to run an :ref:`operator` by calling its class object.
        Child classes *should* override this method with keywords. Then your :term:`IDE` will be able to assist you
        The :meth:`pass_keywords` function makes
        overriding very convenient (just copy the method's body):

        .. code: python

            class NewOp(RDOperator):
                model_name = StringProperty(name="Enter model name:")
                base_segment_name = StringProperty(name="Enter root segment name:", default="")

                @classmethod
                def run(cls, model_name, base_segment_name):
                    return super().run(**cls.pass_keywords())

        .. warning:

            :term: `refactoring<Refactoring>` class attributes (i.e., the keywords) requires you modify both the
            overridden run function *and* your attributes.

        In addition, this method also does extensive error and exception handling writing everything to the log file
        (see :mod:`.logfile`).

        :param kwargs: The keyword arguments passed to the :ref:`Operator` (**must** match the names of the class's
            attributes (only of type :class:`bpy.types.Property).
        :return: The return values of :meth:`bpy.types.Operator.execute`.
        """
        try:
            # cls.logger.debug('get registered operator')
            return get_registered_operator(cls)(**kwargs)


        except TypeError as e:
            bad_kwargs = []
            for kwarg in kwargs.keys():
                if kwarg not in dir(cls):
                    bad_kwargs.append(kwarg)

            cls.logger.error('Exception when running operator {} ({}):'
                             '\n\tkeywords:\t{}\n\tBad keywords:\t{}'
                             '\n\tException:\t{}\n\tMessages:\n\t\t{}'.format(
                             cls.bl_idname, cls.__name__,
                             kwargs,
                             ', '.join(bad_kwargs), type(e).__name__,
                             '\n\t\t'.join(e.__str__().split('\n'))))
            InfoBox.global_messages.append(e.__str__())
            raise e

            # todo check for keyword arguments without default value

        except RuntimeError as e:
            cls.logger.error('Exception when running operator {} ({}):'
                             '\n\tException:\t{}\n\t{}\n'.format(cls.bl_idname, cls.__name__,
                             type(e).__name__, '\n\t'.join(e.__str__().split('\n'))))
            check, messages = Condition.check_conditions(*cls._pre_conditions[cls])
            cls.logger.info("Conditions set for this operator: {}\n\t{}\n\t{}".format(cls._pre_conditions[cls], check,
                            messages))
            InfoBox.global_messages.append(e.__str__())
            raise e
        except Exception as e:
            cls.logger.error('THIS CODE SHOULD NEVER BE EXECUTED: {}\n{}\n'.format(e, log_callstack(back_trace=True)))
            InfoBox.global_messages.append(e.__str__())
            raise e

    @classmethod
    def place_button(cls, layout, text=None, infoBox=None, **kwargs):
        """
        This is a convenience method that let's the developer create a button executing the operator from the gui.
        The results of the :meth:`poll` method (i.e., checking it's conditions) can be optionally passed to an
        :class:`.gui.InfoBox` instance such that a report for a group of operators can be displayed (i.e., why
        it is not executable)

        :param layout: the gui element to place the button (see :meth:`bpy.types.Panel.draw`)
        :param text: Optionally override the text in the ``bl_label`` attribute.
        :param infoBox: Optional instance of :class:`.gui.InfoBox`
        :param kwargs: Additional keyword arguments to :meth:`bpy.types.UILayout.operator`)
        :return: The operator instance (this can be used to set one of the class's attributes)
        """
        if infoBox and cls in cls._pre_conditions:
            # if not isinstance(infoBox, InfoBox):
            #    raise TypeError("Argument: infobox must be of type {} (not {})".format(InfoBox.__name__, type(infoBox)))

            check, messages = Condition.check_conditions(*cls._pre_conditions[cls])
            if not check:
                infoBox.add_message(messages)

        # Checkconditions
        # todo check KWargs
        if not text:
            text = cls.bl_label
        return layout.operator(cls.bl_idname, text=text, **kwargs)

    @staticmethod
    def OperatorLogger(func):
        """
        Decorator for the `bpy.types.Operator.execute` method (only for sub classes of :class:`RDOperator`).

        Performs logging and exception handling.
        """

        def op_logger(self, context):

            # `callargs['self']` parameter refers to the operator instance
            # This is done in order to avoid positional arguments.
            # That way, the decorator can be used as @OperationLogger instead of
            # @OperationLogger
            # callargs = inspect.getcallargs(func,*args)

            class_name = self.__class__.__name__
            id = self.__class__.bl_idname

            # Execute the Operator
            try:
                # self.logger.debug("Entering {}() from {}({}):\n{}".format(
                #                    func.__name__, id, class_name,
                #                    log_callstack()))

                result = func(self, context)
                # self.logger.debug("Leaving {}() {}({})".format(id, class_name, result))

                return result

            except Exception as e:
                InfoBox.global_messages.append(
                    "{}: {} ({})".format(type(e).__name__, e.__str__(), log_callstack_last(back_trace=True)))
                message = "Operator {} ({}) threw an exception:{}\n\t{}".format(id, class_name,
                                                                            type(e).__name__, e)
                self.logger.error("Operator {} ({}) threw an exception:\n ".format(id, class_name) + EXCEPTION_MESSAGE.format(
                                  type(e).__name__, e, log_callstack(), log_callstack(back_trace=True)))
                if isinstance(self, RDOperator):
                    self.report({'ERROR'}, message)
                    return {'FINISHED'}
                else:
                    # Menu has no report and must return None
                    return

        return op_logger

    @staticmethod
    def Preconditions(*conditions):
        """
        :term:`Class decorator<class decorator>` for :term:`operators<operator>`.

        Registers the conditions (of type :class:`.conditions.Condition`) for its subclasses. They will be
        checked within the :meth:`poll` and :meth:`place_button` methods.

        :param conditions: a number of subclasses of :class:`.conditions.Condition`.
        """

        def decorator(cls: RDOperator):  # Todo check why this check fails some times
            if not issubclass(cls, RDOperator):
                raise TypeError("Preconditions: Can only decorate sub classes of RDOperator.i \n{} \n{} \n{}\n{}".format(
                    cls.__name__,
                    cls.mro(), type(cls), conditions))

            cls._pre_conditions[cls] = conditions

            cls.__doc__ += "\n    **Preconditions**:\n\n{}".format("".join(
                '    * :class:`{}.{}`\n'.format(i.__module__, i.__name__) for i in conditions))

            # RDOperator.logger.debug("Decorating {}, \nArgs: {}\n {}, {}, {}".format(cls, args, issubclass(cls, RDOperator),
            #                        issubclass(cls, bpy.types.Operator), [RDOperator is i for i in cls.mro()]))
            # for i in cls.mro():
            #    print(i)
            return cls

        # RDOperator.logger.debug("Precondition:\nArgs: {}".format(args))
        if len(conditions) == 1 and issubclass(conditions[0], RDOperator):
            raise TypeError('Decorator Preconditions must be called with arguments of subclasses of Condition')
        else:
            if any([issubclass(i, RDOperator) for i in conditions]):
                raise TypeError('Decorator Preconditions must be called with arguments of subclasses of Condition {}'.format(
                             conditions))

            return decorator


    @staticmethod
    def Postconditions(*conditions):
        """
        Method decorator for the :meth:`bpy.types.Operator.execute` method. Works only with :term:`operators<operator>`
        derived :class:`RDOperator`.

        Checks whether post conditions are met after calling the operator. Reports an error message to the log file
        (see :mod:`.logfile`)

        :param conditions: a number of subclasses of :class:`.conditions.Condition`.
        """

        def decorator(func):
            def func_wrapper(self, context):
                result = func(self, context)
                check, messages = Condition.check_conditions(*conditions)
                if not check:
                    self.report({'ERROR'}, messages)
                    logger.error('Postcondition not met: {}\\n{}\n{}'.format(messages, log_callstack(), log_callstack(True)))
                    InfoBox.global_messages.append(messages)
                return result

            doc = "\n    **Postconditions**:\n\n{}".format("".join(
                '    * :class:`{}.{}`\n'.format(i.__module__, i.__name__) for i in conditions))
            func.__doc__ = func.__doc__ + doc if func.__doc__ else doc
            return func_wrapper

        return decorator
