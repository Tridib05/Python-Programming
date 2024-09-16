# Initial list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Elements to remove
to_remove = [3, 5, 7]

# Using filter to remove elements
numbers = list(filter(lambda x: x not in to_remove, numbers))

# Output the modified list
print("Modified list:", numbers)
