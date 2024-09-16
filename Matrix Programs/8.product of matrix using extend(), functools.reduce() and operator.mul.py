# Python3 code to demonstrate
# Matrix Product

# initializing list
import operator
from functools import reduce
test_list = [[1, 4, 5], [7, 3], [4], [46, 7, 3]]

# printing original list
print("The original list : " + str(test_list))

x = []
for i in test_list:
	x.extend(i)

res = reduce(operator.mul, x, 1)

# print result
print("The total element product in lists is : " + str(res))
