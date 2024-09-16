# Define the test list
test_list = [5, 6, [], 3, [], [], 9]
# Print the original list
print("The original list is : " + str(test_list))
# Counter variable 'i' to keep track of the current index
i = 0
# While loop to go through all elements of the list
while i < len(test_list):
	# If the current element is an empty list, remove it from the list
	if test_list[i] == []:
		test_list.pop(i)
	# Else, increment the counter variable
	else:
		i += 1
# Reassign the result to the original list after removing all empty lists
res = test_list
# Print the result
print("List after empty list removal : " + str(res))


#This code is contributed by Jyothi pinjala.
