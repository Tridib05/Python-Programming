# Python3 code to demonstrate
# Matrix Product

# initializing list
test_list = [[1, 4, 5], [7, 3], [4], [46, 7, 3]]

# printing original list
print("The original list : " + str(test_list))
res = 1
for i in test_list:
	for j in i:
		res *= j

# print result
print("The total element product in lists is : " + str(res))