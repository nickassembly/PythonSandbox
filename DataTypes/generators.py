import sys
# generate items lazily and more memory efficient

def mygenerator():
    yield 1
    yield 2
    yield 3

g = mygenerator()

value = next(g)
print(value)

value = next(g)
print(value)

def countdown(num):
    print('Starting')
    while num > 0:
        yield num
        num -= 1

cd = countdown(4)

value = next(cd)
print(value)

print(next(cd))

def firstn(n):
    nums = []
    num = 0
    while num < n:
        nums.append(num)
        num += 1
    return nums

# firstn as generator, don't need to save all numbers in an array, more memory efficient
def firstn_generator(n):
    num = 0
    while num < n:
        yield num
        num += 1


print(sys.getsizeof(firstn(1000000)))
print(sys.getsizeof(firstn_generator(1000000)))

def fibonacci(limit):
    # 0 1 1 2 3 5 8 ...
    a, b = 0, 1
    while a < limit:
        yield a 
        a, b = b, a + b

fib = fibonacci(30)
for i in fib:
    print(i)


mygenerator = (i for i in range(10) if i % 2 == 0)
for i in mygenerator:
    print(i)

