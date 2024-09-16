def multiply_list(list1):
    # Initialize product to 1
    product = 1
    
    # Iterate through each element in the list
    for element in list1:
        product *= element
    
    return product

# Example
list1 = [1, 2, 3, 4, 5]
result = multiply_list(list1)
print(result)
