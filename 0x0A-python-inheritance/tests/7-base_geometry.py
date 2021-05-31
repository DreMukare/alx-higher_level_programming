==========================
How to use 7-base_geometry
==========================

This modue defines class BaseGeometry

::
    >>> BaseGeometry = __import__('7-base_geometry').BaseGeometry
    >>> bg = BaseGeometry()
    >>> type(bg)
    <class '7-base_geometry.BaseGeometry'>
::

Testing both functions

For area:
>>> bg.area()
Traceback (most recent call last):
    ...
Exception: area() is not implemented

Correct value for integer validator
>>>bg.integer_validator('age', 23)

Wrong second parameter
>>>bg.integer_validator('age', '17')
Traceback (most recent call last)
    ...
TypeError: age must be an integer

>>>bg.integer_validator('age', 'yes')
Traceback (most recent call last)
    ...
TypeError: age must be an integer

>>> bg.integer_validator('age', True)
Traceback (most recent call last)
    ...
TypeError: age must be an integer

>>> bg.integer_validator('age', 6.9)
Traceback (most recent call last)
    ...
TypeError: age must be an integer

>>> bg.integer_validator('age', float('inf'))
Traceback (most recent call last)
    ...
TypeError: age must be an integer

>>> bg.integer_validator('age', float('nan'))
Traceback (most recent call last)
    ...
TypeError: age must be an integer

Testing wrong value
>>> bg.integer_validator('age', -5)
Traceback (most recent call last)
    ...
ValueError: age must be greater than 0

>>> bg.integer_validator('age', 0)
Traceback (most recent call last)
    ...
ValueError: age must be greater than 0

No arguments
>>> bg.integer_validator()
Traceback (most recent call last)
    ...
TypeError: integer_validator() missing 2 required positional arguments: 'name' and 'value'

One argument
>>> bg.integer_validator('name')
Traceback (most recent call last)
    ...
TypeError: integer_validator() missing 1 required positional argument: 'value'

Extra arguments
>>> bg.integer_validator('name', 34, 'eys')
Traceback (most recent call last)
    ...
TypeError: integer_validator() takes 2 positional arguments but 3 were given

Module docstring
>>> doc = BaseGeometry = __import__('7-base_geometry').__doc__
>>> len(doc) > 1
True
