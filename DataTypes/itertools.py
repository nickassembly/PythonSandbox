# itertools: product, permutations, combinations, accumulate, groupby, and infinite iterators
from itertools import product
from itertools import permutations
from itertools import combinations, combinations_with_replacement
from itertools import accumulate
import operator

from itertools import groupby
from itertools import count, cycle, repeat


a = [1, 2]
b = [3]
prod = product(a, b, repeat=2)
print(list(prod))

c = [1,2,3]
perm = permutations(c)
print(list(perm))

d = [1, 2, 3, 4]
comb = combinations(d, 2) # 2nd arg is length
print(list(comb))
comb_wr = combinations_with_replacement(d, 2)
print(list(comb_wr))

e = [1, 2, 3, 4]
acc = accumulate(e, func=operator.mul)
print(e)
print(list(acc))


def smaller_than_3(x):
    return x < 3

f = [1, 2, 3, 4]
group_obj = groupby(f, key=smaller_than_3)
for key, value in group_obj:
    print(key, list(value))

persons = [{'name': 'Tim', 'age': 25}, {'name': 'Dan', 'age': 25}, {'name': 'Lisa', 'age': 27}, {'name': 'Claire', 'age': 28}]

person_obj = groupby(persons, key=lambda x: x['age'])
for key, value in person_obj:
    print(key, list(value))

a = [1, 2, 3]

for i in count(10):
    print(i)
    if i == 15:
        break

# for i in cycle(a):
#     print(i)

