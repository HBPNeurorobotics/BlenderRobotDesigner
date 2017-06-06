Extending the RobotDesigner
===========================

Plugin Structure
----------------


Adding new operators
--------------------

Automatically, detected. Take care on how to avoid circular dependencies.

Adding new properties
---------------------

New properties have to be listed explicitly in __init__.py because if they are nested
they have to be registered in a certain order.




