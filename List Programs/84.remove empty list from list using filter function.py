# Python3 code to Demonstrate Remove empty List

# Initializing list
test_list = [5, 6, [], 3, [], [], 9]

# printing original list
print("The original list is : " + str(test_list))

# Remove empty List from List
res = filter(None, test_list)

# printing result
print("List after empty list removal : " ,res)
