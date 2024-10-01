# Using Counter() + split()

from collections import Counter

# initializing string
test_str = 'Gfg is best . Geeks are good and Geeks like Gfg'

# printing original string
print("The original string is : " + str(test_str))

# Words Frequency in String Shorthands
# using Counter() + split()
res = Counter(test_str.split())

# Printing result
print("The words frequency : " + str(dict(res)))
