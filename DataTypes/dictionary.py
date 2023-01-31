# Dictionary: key-value pairs, unordered, mutable

mydict = {"name": "Nick", "age": 43, "city": "Gonzales"}
print(mydict)

mydict2 = dict(name="Mary", age=27, city="Boston")
print(mydict2)

value = mydict["name"]
print(value)


mydict["email"] = "nick@xyz.com"
print(mydict)

del mydict["name"]
print(mydict)
mydict.pop("age")
print(mydict)

if "city" in mydict:
    print(mydict["city"])

for key in mydict:
    print(key)

for key, value in mydict.items():
    print(key, value)

# both dictionaries point to the same dictionary inside memory
mydict_cpy = mydict
print(mydict_cpy)

mydict_cpy["email"] = "nick@xyz.com"
print(mydict_cpy)
print(mydict)


#merge 2 dictionaries
my_dict3 = {"name":"Nick", "age":43, "email":"nick@xyz.com"}
my_dict_4 = dict(name="Mary", age=34, city="Boston")

my_dict3.update(my_dict_4)
print(my_dict3)

# key types - can use any immutable type
my_dict5 = {3: 9, 6: 36, 9: 81}
print(my_dict5)

#when using values like this, use value to access, not index numbers
value = my_dict5[3]
print(value)


