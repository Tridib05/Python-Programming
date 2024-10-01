# Python 3 code to demonstrate 
# Least Frequent Character in String
# collections.Counter() + min()
from collections import Counter

# initializing string 
test_str = "GeeksforGeeks"

# printing original string
print ("The original string is : " + test_str)

# using collections.Counter() + min() to get 
# Least Frequent Character in String
res = Counter(test_str)
res = min(res, key = res.get) 

# printing result 
print ("The minimum of all characters in GeeksforGeeks is : " + str(res))
