from functools import reduce

# Lambda arguments: expression

add10 = lambda x: x + 10
print(add10(5))

mult = lambda x, y: x*y
print(mult(2,7))


points2D = [(1, 2), (15, 1), (5, -1), (10, 4)]

points2D_sorted = sorted(points2D, key=lambda x: x[1]) # lambda sorts according to 2nd index (y)
points2D_sorted2 = sorted(points2D, key=lambda x: x[0] + x[1]) 

print(points2D)
print(points2D_sorted)

#map(func, seq)
a = [1, 2, 3, 4, 5]
b = map(lambda x: x*2, a)
print(list(b))

c = [x*2 for x in a]
print(c)

#filter(func, seq) 
c = [1, 2, 3, 4, 5, 6]
d = filter(lambda x: x%2==0, c)
print(list(d))

#reduce(func, seq) - applies function to elements and returns a single value

e = [1, 2, 3, 4]
product_a = reduce(lambda x, y: x*y, a)
print(product_a)




