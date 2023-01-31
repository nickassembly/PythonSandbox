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




