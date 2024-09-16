from collections import deque

original_list = [4, 8, 2, 10, 15, 18]

copied_list = deque(original_list)
copied_list = list(copied_list)

print("Original List:", original_list)

print("After Cloning:", copied_list)
