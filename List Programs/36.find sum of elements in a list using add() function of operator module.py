# Python 3 program to find the sum of all elements in the
# list using add function of operator module

from operator import*
list1 = [12, 15, 3, 10]
result = 0
for i in list1:
# Adding elements in the list using
# add function of operator module
	result = add(i, result)
# printing the result
print(result)
