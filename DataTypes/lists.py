# Lists: ordered, mutable, allows duplicate elements

# takes a portion starting at 1st index and stopping at 5th index (non inclusive of the 5th index)
mylist = [1,2,3,4,5,6,7,8,9]
a = mylist[1:5] 
print(a)

# no start index specified, goes from beginning -- stops at 5th index
b = mylist[:5] 
print(b)

# no stop index specified, goes to end -- starts at 1st index (2nd element)
c = mylist[1:]
print(c)

#step index, goes from beginning to end with 1 step
mylist2 = [1,2,3,4,5,6,7,8,9]
d = mylist2[::1]
print(d)

# negative index - this example reverses the list
neg_d = mylist2[::-1]
print(neg_d)

# takes every 2nd item
d2 = mylist2[::2] 
print(d2)

#copying lists
list_org = ["banana", "cherry", "apple"]

list_cpy = list_org # bad way to copy, better to use .copy()

# list comprehension
new_list = [1,2,3,4,5,6]
b = [i*i for i in new_list]

print(new_list)
print(b)




