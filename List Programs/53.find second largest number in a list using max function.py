def find_second_largest(numbers):
    largest = max(numbers)
    numbers.remove(largest)
    return max(numbers)

# Example usage
numbers = [10, 20, 4, 45, 99]
second_largest = find_second_largest(numbers)
print("The second largest number is:", second_largest)
