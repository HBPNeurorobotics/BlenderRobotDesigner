robot_designer_plugin.export.urdf.urdf_dom module
=================================================

Introduction
^^^^^^^^^^^^

This module is generated automatically by the `generateDS.py <https://pypi.python.org/pypi/generateDS>`_ package/script.
Generation, in general, can be invoked by:

.. code-block:: bash

    robot_designer_plugin/export/urdf $   pip install generateds==2.14a
    robot_designer_plugin/export/urdf $   generateDS.py -f -o "urdf_dom.py" ../../../resources/urdf.xsd
    robot_designer_plugin/export/urdf $   2to3 urdf_dom.py -w

.. warning::

    However, there are currently some limitations. Because of skipped support of ``xml.etree.cElementTree``,
    we require version ``2.14a0``. This limitation will be resolved in future versions, when pre-compiled
    binaries (i.e., ``lxml``) are provided with the plugin. Further the following step is required in order to work with
    python 3 and the missing ``lxml`` package.

.. code-block:: bash

    robot_designer_plugin/export/urdf $   sed -i "\.encode(ExternalEncoding)//g"

.. warning::

    Missing ``lxml`` also raised an error when extended types are used in :doc:`../../resources/urdf.xsd`.
    This can be resolved by modifying the ``find_attr_value`` function in the auto generated file (commented lines):

.. code-block:: python

    def find_attr_value_(attr_name, node):
        attrs = node.attrib
        attr_parts = attr_name.split(':')
        value = None
        if len(attr_parts) == 1:
            value = attrs.get(attr_name)
        # elif len(attr_parts) == 2:
        #     prefix, name = attr_parts
        #     namespace = node.nsmap.get(prefix)
        #     if namespace is not None:
        #         value = attrs.get('{%s}%s' % (namespace, name, ))
        return value

