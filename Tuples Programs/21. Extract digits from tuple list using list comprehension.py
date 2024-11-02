# Initializing list
test_list = [(15, 3), (3, 9), (1, 10), (99, 2)]

# Printing original list
print("The original list is : " + str(test_list))

# Extracting digits from Tuple list using list comprehensions
temp = ''.join([str(i) for sublist in test_list for i in sublist])
result = set(temp)
result = [int(i) for i in result]
# Printing result
print("The extracted digits : " + str(list(result)))
#This code is contributed by Vinay Pinjala.
