# collections: Counter, namedtuple, OrderedDict, defaultdict, deque
from collections import Counter, defaultdict
from collections import namedtuple
from collections import OrderedDict
from collections import deque

a = "aaaabbbbccc"
my_counter = Counter(a)
print(my_counter)
print(my_counter.items())
print(my_counter.keys())
print(my_counter.values())
print(my_counter.most_common())

print(list(my_counter.elements())) # give iterable over elements

Point = namedtuple('Point', 'x,y')
pt = Point(1, -4)
print(pt.x, pt.y)

ordered_dict = OrderedDict()
ordered_dict['a'] = 1
ordered_dict['b'] = 2
ordered_dict['c'] = 3
ordered_dict['d'] = 4
ordered_dict['e'] = 5
print(ordered_dict)

d = deque()
d.append(1)
d.append(2)

d.appendleft(3)
d.extend([4,5,6])
print(d)

d.rotate(1)

