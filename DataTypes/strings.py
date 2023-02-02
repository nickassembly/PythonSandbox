# Strings: ordered, immutable, text representation

my_string = 'Hello World, I\'m a programmer'
print(my_string)

my_string2 = 'Hello World'
char = my_string2[-2] # 2nd to last
print(char)

substring = my_string[1:5]
substring2 = my_string[::2] # stop index takes every 2nd character (- to reverse)
print(substring)
print(substring2)

greeting = "Hello"
name = "Tom"
sentence = greeting + " " + name
print(greeting)

for i in greeting:
    print(i)

if 'e' in greeting:
    print('yes')
else:
    print('no')

my_string = '     Hello World      '
my_string = my_string.strip() # removes white space, need to reassign because strings are immutable
print(my_string)

print(my_string.upper())
print(my_string.startswith('Hello'))

print(my_string.find('pp')) #will return -1 if it doesn't find

print(my_string.replace('World', "Keller"))

my_string_list = 'how are you doing'
my_list = my_string_list.split() # default delimiter is a space
print(my_list)

new_string = ' '.join(my_list) # concatenate list back to string
print(new_string)

my_list2 = ['a'] * 6
print(my_list2)

# bad - creates multiple strings, expensive operation
my_string = ''
for i in my_list2:
    my_string += i 
print(my_string)

# good (use this to concatenate strings)
my_string = ''.join(my_list2)
print(my_string)

# formatting 
# %, .format(), f-Strings

var = "Tom"
my_string = "The variable is %s" % var
print(my_string)

var2 = 3
my_string2 = "The int variable is %d" % var2
print(my_string2)

var3 = 3.234234234
my_string3 = "The float variable is %f" % var3
print(my_string3)

oldWay = 3.4234234
my_string4 = "The variable is {:.2f}".format(oldWay) # {:.2f} specific digits after decimal
print(my_string4)

newWay = 3.4234234
var2 = 6
my_string5 = f"The variable is {newWay} and {var2}" # new way
print(my_string5)

