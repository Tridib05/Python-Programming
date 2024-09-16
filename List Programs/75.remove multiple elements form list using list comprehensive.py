# Initial list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Elements to remove
to_remove = [3, 5, 7]

# Removing elements using list comprehension
numbers = [num for num in numbers if num not in to_remove]

# Output the modified list
print("Modified list:", numbers)
