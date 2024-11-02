# initializing tuple
test_tuple = ([5, 6], [6, 7, 8, 9], [3])

# printing original tuple
print("The original tuple : " + str(test_tuple))

# Flatten tuple of List to tuple
# Using list comprehension and extend()
res_list = []
[res_list.extend(sublist) for sublist in test_tuple]
res = tuple(res_list)

# printing result
print("The flattened tuple : " + str(res))
