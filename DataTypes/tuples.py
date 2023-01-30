# Tuple: ordered, immutable, allows duplicate elements

mytuple = ("Max", 28, "Boston")
print(mytuple)

mytuple = tuple(["Nick", 43, "Louisiana"])
print(mytuple)

item = mytuple[1]
print(item)

item = mytuple[-1] #refers to last item
print(item)

for i in mytuple:
    print(i)

if ("Nick" in mytuple):
    print("Yes")
else:
    print("No")

my_tuple = ('a', 'p', 'p', 'l', 'e')
print(len(my_tuple))

print(my_tuple.count('p'))
print(my_tuple.index('p'))

# tuple to list and vice versa
my_list = list(my_tuple)
print(my_list)

my_tuple2 = tuple(my_list)
print(my_tuple2)

#slicing a tuple

a = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

b = a[2:5]
print(b)


# unpacking

my_tuple2 = "Max", 28, "Boston"
name, age, city = my_tuple2
print (name)
print(age)
print(city)

# Differences between Tuples and lists (size comparison)
import sys
my_list = [0, 1, 2, "hello", True]
my_tuple = (0, 1, 2, "hello", True)
print(sys.getsizeof(my_list), "bytes")
print(sys.getsizeof(my_tuple), "bytes")

#iteration is more efficient than lists
import timeit
print(timeit.timeit(stmt="[0,1,2,3,4,5]", number=1000000))
print(timeit.timeit(stmt="(0,1,2,3,4,5)", number=1000000))



