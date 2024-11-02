# creating a list
list1 = [1, 2, 5, 6]

# creating an empty list to store the result
res = []

# iterating through each value in the list
for val in list1:
	# creating a tuple of the value and its cube
	tup = (val, val**3)
	# adding the tuple to the result list
	res.append(tup)

# print the result
print(res)
