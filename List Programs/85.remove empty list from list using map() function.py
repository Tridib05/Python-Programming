# Initializing list
test_list = [5, 6, [], 3, [], [], 9]

# printing original list
print("The original list is : " + str(test_list))

# Remove empty List from List
# using map() function
res = list(map(lambda x: x if x != [] else None, test_list))
res = [x for x in res if x != None]

# printing result
print("List after empty list removal : " + str(res))
#This code is contributed by Vinay Pinjala.
