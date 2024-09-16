def product_recursive(numbers):
    # base case: list is empty
    if not numbers:
        return 1
    # recursive case: multiply first element by product of the rest of the list
    return numbers[0] * product_recursive(numbers[1:])
list1 = [1, 2, 3]
product = product_recursive(list1)
print(product)  # Output: 6

list2 = [3, 2, 4]
product = product_recursive(list2)
print(product)  # Output: 24
