# Define the list to be used for the demonstration
test_list = [1, 4, 5, 7, 8]

# Calculate the length of the list using a list comprehension and the sum function
# The list comprehension generates a sequence of ones for each element in the list
# The sum function then sums all the ones to give the length of the list
length = sum(1 for _ in test_list)

# Print the length of the list
print("Length of list using list comprehension is:", length)
