def clear_list(lst):
    lst = [item for item in lst if False]
    return lst

input_list = [2, 3, 5, 6, 7]
output = clear_list(input_list)
print(output)  # Output: []
