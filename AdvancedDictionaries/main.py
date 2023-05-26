from collections import defaultdict


mylist = [1, 2, 3, 4, 5, 1, 2]

counter = defaultdict(int)

for element in mylist:
    counter[element] += 1

print(counter)

grouped_words = defaultdict(list)

words = ["apple", "banana", "carrot", "avacado", "brocoli", "orange"]

for word in words:
    grouped_words[word[0]].append(word)

tuple_list = [("A", 10), ("B", 20), ("C", 30), ("D", 40), ("E", 50), ("A", 60)]

grouped_data = defaultdict(list)

for key, value in tuple_list:
    grouped_data[key].append(value)

print(grouped_data)

# extend dictionaries


class MyDeafultDict(defaultdict):
    def __missing__(self, key):
        self[key] = value = len(key)
        return value


test = MyDeafultDict()

print(test["hello"])

constant_deafult_dict = defaultdict(lambda: "hello world")

print(constant_deafult_dict["hello"])
