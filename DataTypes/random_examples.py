import random
import secrets 
import numpy as np

a = random.random()
b = random.uniform(1, 10)
c = random.randint(1, 10)
print(a)
print(b)
print(c)

d = random.normalvariate(0, 1)
print(d)

mylist = list("ABCDEFGH")
a = random.sample(mylist, 3)
print(a)

random.shuffle(mylist)
print(mylist)

random.seed(1)
print(random.random())
print(random.randint(1,10))

random.seed(2)
print(random.random())
print(random.randint(1,10))

#secrets used for security
# takes more time but generates a true random number

a2 = secrets.randbelow(10)
print(a2)

b2 = secrets.randbits(4)
# generate a rand number with 4 bits
print(b2)

d = secrets.choice(mylist)
print(d)

e = np.random.rand(3, 3) #produces a 3 by 3 array
print(e)

np.random.seed(1) #use numpy random seed method instead of regular seed method
