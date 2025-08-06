what is dunder in python?
In Python, "dunder" is slang for "double underscore" and refers to special methods or attributes whose names start and end with two underscores, such as _init_ or _str_. 
These are also called magic methods.

Dunder methods enable objects to interact with Python's built-in functions and operators. For example:
- _init_ sets up new objects (like a constructor).
- _add_ allows you to define behavior for the + operator.
- _str_ lets you control how your object is printed.
- _len, __getitem_, etc., let you support len(), indexing, and more functions.

These methods form a contract between your class and the Python interpreter, letting custom classes behave like built-in types. You typically do not call dunder methods directly—they are invoked implicitly by Python when needed.
Python dunder methods are the special predefined methods having two prefixes and two suffix underscores in the method name. Here, the word dunder means double under (underscore). These special dunder methods are used in case of operator overloading ( they provide extended meaning beyond the predefined meaning to an operator). Some of the examples of most common dunder methods in use are __int__,__new__, __add__, __len__, and __str__ method.