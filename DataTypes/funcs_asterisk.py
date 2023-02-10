# * * * * * 
zeros = [0, 1] * 10
print(zeros)

def foo(a, b, *args, **kwargs):
    print(a)
    for arg in args:
        print(arg)

    for key in kwargs:
        print(key, kwargs[key])

def foo2(a, b, c):
    print(a, b, c)

foo(1, 2, 3, 4, 5, six=6, seven=7)

my_list = [0, 1, 2]
foo2(*my_list)

# * can be used for unpacking containers
numbers = [1, 2, 3, 4, 5, 6]

*beginning, last= numbers
print(beginning)
print(last)

my_tuple = (1, 2, 3)
my_list2 = [4, 5, 6]
my_set = {7,8,9}

new_list = [*my_tuple, *my_list, *my_set]
print(new_list)