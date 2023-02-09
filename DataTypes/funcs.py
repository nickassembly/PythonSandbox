

"""
- The difference between arguments and parameters
- Positional and keyword arguments
- Default arguments
- Variable-length arguments (*args and **kwargs)
- Container unpacking into function arguments
- Local vs. global arguments
- Parameter passing (by value or by reference?)
"""

def print_name(name):
    print(name)

print_name('Alex')

def foo(a, b, c, d=4):
    print(a, b, c, d)

foo(c=1, b=2, a=3)
foo(1, b=2, c=3)

foo(1, 2, 3, 7)

def foo2(a, b, *args, **kwargs):
    print(a, b)
    for arg in args:
        print(arg)
    for key in kwargs:
        print(key, kwargs[key])

foo2(1, 2, 3, 4, 5, six=6, seven=7)

def foo3(*args, last):
    for arg in args:
        print(arg)
    print(last)

foo3(1, 2, 3, last=100)

def foo5(a, b, c):
    print(a, b, c)

my_dict= {'a':1, 'b':2, 'c':3}
foo5(*my_dict) # unpacking arguments


