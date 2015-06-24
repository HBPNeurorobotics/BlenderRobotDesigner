'''Property Definitions (bpy.props)
   This module defines properties to extend blenders internal data, the result of these functions is used to assign properties to classes registered with blender and can't be used directly.
   
'''


def BoolProperty(name="", description="", default=False, options={'ANIMATABLE'}, subtype='NONE', update=None, get=None, set=None):
   '''Returns a new boolean property definition.
      
      Arguments:
      @name (string): Name used in the user interface.
      @description (string): Text used for the tooltip and api documentation.
      @options (set): Enumerator in ['HIDDEN', 'SKIP_SAVE', 'ANIMATABLE', 'LIBRARY_EDITABLE'].
      @subtype (string): Enumerator in ['UNSIGNED', 'PERCENTAGE', 'FACTOR', 'ANGLE', 'TIME', 'DISTANCE', 'NONE'].
      @update (function): function to be called when this value is modified,This function must take 2 values (self, context) and return None.
      *Warning* there are no safety checks to avoid infinite recursion.
      

   '''

   pass

def BoolVectorProperty(name="", description="", default=(False, False, False), options={'ANIMATABLE'}, subtype='NONE', size=3, update=None, get=None, set=None):
   '''Returns a new vector boolean property definition.
      
      Arguments:
      @name (string): Name used in the user interface.
      @description (string): Text used for the tooltip and api documentation.
      @default (sequence): sequence of booleans the length of *size*.
      @options (set): Enumerator in ['HIDDEN', 'SKIP_SAVE', 'ANIMATABLE', 'LIBRARY_EDITABLE'].
      @subtype (string): Enumerator in ['COLOR', 'TRANSLATION', 'DIRECTION', 'VELOCITY', 'ACCELERATION', 'MATRIX', 'EULER', 'QUATERNION', 'AXISANGLE', 'XYZ', 'COLOR_GAMMA', 'LAYER', 'NONE'].
      @size (int): Vector dimensions in [1, and 32].
      @update (function): function to be called when this value is modified,This function must take 2 values (self, context) and return None.
      *Warning* there are no safety checks to avoid infinite recursion.
      

   '''

   pass

def CollectionProperty(items, type="", description="", options={'ANIMATABLE'}):
   '''Returns a new collection property definition.
      
      Arguments:
      @type (class): A subclass of bpy.types.PropertyGroup.
      @name (string): Name used in the user interface.
      @description (string): Text used for the tooltip and api documentation.
      @options (set): Enumerator in ['HIDDEN', 'SKIP_SAVE', 'ANIMATABLE', 'LIBRARY_EDITABLE'].

   '''

   pass

def EnumProperty(items, name="", description="", default="", options={'ANIMATABLE'}, update=None, get=None, set=None):
   '''Returns a new enumerator property definition.
      
      Arguments:
      @name (string): Name used in the user interface.
      @description (string): Text used for the tooltip and api documentation.
      @default (string or set): The default value for this enum, A string when *ENUM_FLAG*is disabled otherwise a set which may only contain string identifiers
      used in *items*.
      
      @options (set): Enumerator in ['HIDDEN', 'SKIP_SAVE', 'ANIMATABLE', 'ENUM_FLAG', 'LIBRARY_EDITABLE'].
      @items (sequence of string triples or a function): sequence of enum items formatted:[(identifier, name, description, icon, number), ...] where the identifier is used
      for python access and other values are used for the interface.
      Note the item is optional.
      For dynamic values a callback can be passed which returns a list in
      the same format as the static list.
      This function must take 2 arguments (self, context)
      WARNING: Do not use generators here (they will work the first time, but will lead to empty values
      in some unload/reload scenarii)!
      
      @update (function): function to be called when this value is modified,This function must take 2 values (self, context) and return None.
      *Warning* there are no safety checks to avoid infinite recursion.
      

   '''

   pass

def FloatProperty(name="", description="", default=0.0, min=sys.float_info.min, max=sys.float_info.max, soft_min=sys.float_info.min, soft_max=sys.float_info.max, step=3, precision=2, options={'ANIMATABLE'}, subtype='NONE', unit='NONE', update=None, get=None, set=None):
   '''Returns a new float property definition.
      
      Arguments:
      @name (string): Name used in the user interface.
      @description (string): Text used for the tooltip and api documentation.
      @options (set): Enumerator in ['HIDDEN', 'SKIP_SAVE', 'ANIMATABLE', 'LIBRARY_EDITABLE'].
      @subtype (string): Enumerator in ['UNSIGNED', 'PERCENTAGE', 'FACTOR', 'ANGLE', 'TIME', 'DISTANCE', 'NONE'].
      @unit (string): Enumerator in ['NONE', 'LENGTH', 'AREA', 'VOLUME', 'ROTATION', 'TIME', 'VELOCITY', 'ACCELERATION'].
      @update (function): function to be called when this value is modified,This function must take 2 values (self, context) and return None.
      *Warning* there are no safety checks to avoid infinite recursion.
      

   '''

   pass

def FloatVectorProperty(name="", description="", default=(0.0, 0.0, 0.0), min=sys.float_info.min, max=sys.float_info.max, soft_min=sys.float_info.min, soft_max=sys.float_info.max, step=3, precision=2, options={'ANIMATABLE'}, subtype='NONE', size=3, update=None, get=None, set=None):
   '''Returns a new vector float property definition.
      
      Arguments:
      @name (string): Name used in the user interface.
      @description (string): Text used for the tooltip and api documentation.
      @default (sequence): sequence of floats the length of *size*.
      @options (set): Enumerator in ['HIDDEN', 'SKIP_SAVE', 'ANIMATABLE', 'LIBRARY_EDITABLE'].
      @subtype (string): Enumerator in ['COLOR', 'TRANSLATION', 'DIRECTION', 'VELOCITY', 'ACCELERATION', 'MATRIX', 'EULER', 'QUATERNION', 'AXISANGLE', 'XYZ', 'COLOR_GAMMA', 'LAYER', 'NONE'].
      @unit (string): Enumerator in ['NONE', 'LENGTH', 'AREA', 'VOLUME', 'ROTATION', 'TIME', 'VELOCITY', 'ACCELERATION'].
      @size (int): Vector dimensions in [1, and 32].
      @update (function): function to be called when this value is modified,This function must take 2 values (self, context) and return None.
      *Warning* there are no safety checks to avoid infinite recursion.
      

   '''

   pass

def IntProperty(name="", description="", default=0, min=-sys.maxint, max=sys.maxint, soft_min=-sys.maxint, soft_max=sys.maxint, step=1, options={'ANIMATABLE'}, subtype='NONE', update=None, get=None, set=None):
   '''Returns a new int property definition.
      
      Arguments:
      @name (string): Name used in the user interface.
      @description (string): Text used for the tooltip and api documentation.
      @options (set): Enumerator in ['HIDDEN', 'SKIP_SAVE', 'ANIMATABLE', 'LIBRARY_EDITABLE'].
      @subtype (string): Enumerator in ['UNSIGNED', 'PERCENTAGE', 'FACTOR', 'ANGLE', 'TIME', 'DISTANCE', 'NONE'].
      @update (function): function to be called when this value is modified,This function must take 2 values (self, context) and return None.
      *Warning* there are no safety checks to avoid infinite recursion.
      

   '''

   pass

def IntVectorProperty(name="", description="", default=(0, 0, 0), min=-sys.maxint, max=sys.maxint, soft_min=-sys.maxint, soft_max=sys.maxint, options={'ANIMATABLE'}, subtype='NONE', size=3, update=None, get=None, set=None):
   '''Returns a new vector int property definition.
      
      Arguments:
      @name (string): Name used in the user interface.
      @description (string): Text used for the tooltip and api documentation.
      @default (sequence): sequence of ints the length of *size*.
      @options (set): Enumerator in ['HIDDEN', 'SKIP_SAVE', 'ANIMATABLE', 'LIBRARY_EDITABLE'].
      @subtype (string): Enumerator in ['COLOR', 'TRANSLATION', 'DIRECTION', 'VELOCITY', 'ACCELERATION', 'MATRIX', 'EULER', 'QUATERNION', 'AXISANGLE', 'XYZ', 'COLOR_GAMMA', 'LAYER', 'NONE'].
      @size (int): Vector dimensions in [1, and 32].
      @update (function): function to be called when this value is modified,This function must take 2 values (self, context) and return None.
      *Warning* there are no safety checks to avoid infinite recursion.
      

   '''

   pass

def PointerProperty(type="", description="", options={'ANIMATABLE'}, update=None):
   '''Returns a new pointer property definition.
      
      Arguments:
      @type (class): A subclass of bpy.types.PropertyGroup.
      @name (string): Name used in the user interface.
      @description (string): Text used for the tooltip and api documentation.
      @options (set): Enumerator in ['HIDDEN', 'SKIP_SAVE', 'ANIMATABLE', 'LIBRARY_EDITABLE'].
      @update (function): function to be called when this value is modified,This function must take 2 values (self, context) and return None.
      *Warning* there are no safety checks to avoid infinite recursion.
      

   '''

   pass

def RemoveProperty(cls, attr):
   '''Removes a dynamically defined property.
      
      Arguments:
      @cls (type): The class containing the property (must be a positional argument).
      @attr (string): Property name (must be passed as a keyword).

      Note: Typically this function doesn't need to be accessed directly.Instead use del cls.attr
      
   '''

   pass

def StringProperty(name="", description="", default="", maxlen=0, options={'ANIMATABLE'}, subtype='NONE', update=None, get=None, set=None):
   '''Returns a new string property definition.
      
      Arguments:
      @name (string): Name used in the user interface.
      @description (string): Text used for the tooltip and api documentation.
      @options (set): Enumerator in ['HIDDEN', 'SKIP_SAVE', 'ANIMATABLE', 'LIBRARY_EDITABLE'].
      @subtype (string): Enumerator in ['FILE_PATH', 'DIR_PATH', 'FILE_NAME', 'NONE'].
      @update (function): function to be called when this value is modified,This function must take 2 values (self, context) and return None.
      *Warning* there are no safety checks to avoid infinite recursion.
      

   '''

   pass

