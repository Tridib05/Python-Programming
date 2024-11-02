# Creates a sorted dictionary (sorted by key)
from collections import OrderedDict

d = {'ravi': '10', 'rajnish': '9', 'abc': '15'}
d1 = OrderedDict(sorted(d.items()))
print(d1)
