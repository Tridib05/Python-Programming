# Define a function to count the number of elements in a list using recursion
def count_elements_recursion(lst):
    # Base case: if the list is empty, return 0
    if not lst:
        return 0
    # Recursive case: add 1 to the count of the remaining elements in the list
    return 1 + count_elements_recursion(lst[1:])


# Test the function with a sample list
lst = [1, 2, 3, 4, 5]
print("The length of the list is:", count_elements_recursion(lst))

# Output: The length of the list is: 5
