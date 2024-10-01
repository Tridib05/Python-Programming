# Python3 code to demonstrate working of
# Words Frequency in String Shorthands
# Using dictionary comprehension + operator.countOf() + split()

import operator as op

# Initializing string
test_str = 'Gfg is best . Geeks are good and Geeks like Gfg'

# Printing original string
print("The original string is : " + str(test_str))
listString = test_str.split()

# Words Frequency in String Shorthands
# Using dictionary comprehension + operator.countOf()
res = {key: op.countOf(listString, key) for key in listString}

# Printing the result
print("The words frequency : " + str(res))
