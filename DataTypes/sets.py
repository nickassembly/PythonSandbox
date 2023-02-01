# Sets: unordered, mutable, no duplicates

myset = {1, 2, 3, 1, 2} # will only print unique
print(myset)

myset2 = {"h", "e", "l", "l", "o"}
print(myset2)

myset3 = set()
myset3.add(1)
myset3.add(2)
myset.add(3)

myset.remove(3)
myset.discard(4) # does not throw an error when not finding element

print(myset)

if 1 in myset:
    print("yes")


# Union and Intersection
odds = {1, 3, 5, 7, 9}
evens = {0, 2, 4, 6, 8}
primes = {2, 3, 5, 7}

u = odds.union(evens) # combine odds and evens w/o duplication
print(u)

i = odds.intersection(primes) # would give you all numbers that are both odd and prime
print(i)

setA = {1,2,3,4,5,6,7,8,9}
setB = {1,2,3,10,11,12}

diff = setA.difference(setB) 
print(diff)

semDiff = setB.symmetric_difference(setA)
print(semDiff)

# modify sets in place
setA.update(setB) # updates set by adding elements found in another set (without duplication)
print(setA)

setA.intersection_update(setB) #updates set by only keeping elements found in both sets
print(setA)

setA.difference_update(setB) #updates set by removing elements found in another set
print(setA)

#subsets and supersets
setC = {1,2,3,4,5,6}
setD = {1,2,3}

print(setA.issubset(setB))
print(setB.issubset(setA))
print(setA.issuperset(setB))






