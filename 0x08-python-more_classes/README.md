# 0x08-python-more_classes
## Object Oriented Programming

### classes
- The `self`
  Class methods have only one specific difference from ordinary functions - they must have an extra first name that has to be added to the beginning of the parameter list, but you do not give a value for this parameter when you call the method, Python will provide it. This particular variable refers to the object itself, and by convention, it is given the name self.
- The `__init__` method
  The __init__ method is run as soon as an object of a class is instantiated (i.e. created). The method is useful to do any initialization (i.e. passing initial values to your object) you want to do with your object. Notice the double underscores both at the beginning and at the end of the name.

- Class And Object Variables
  1. Class variables are shared - they can be accessed by all instances of that class. There is only one copy of the class variable and when any one object makes a change to a class variable, that change will be seen by all the other instances.
  2. Object variables are owned by each individual object/instance of the class. In this case, each object has its own copy of the field i.e. they are not shared and are not related in any way to the field by the same name in a different instance. An example will make this easy to understand

- The `__repr__` method
  Instance method that returns an “official” string representation of an instance

- The `__str__` method
  Instance method that returns an “informal” and nicely printable string representation of an instance

- The `__doc__` method
  The string documentation of an object (based on docstring)