#using lambda function
lst = [20, 10, 20, 4, 100]
print(max(lst, key=lambda value: int(value)) )

#using reduce function
from functools import reduce
lst = [20, 10, 20, 4, 100]
largest_elem = reduce(max, lst)
print(largest_elem)

#using heapq.nlargest()
import heapq
# list of numbers
list1 = [10, 20, 4, 45, 99]
# finding the largest element using heapq.nlargest()
largest_element = heapq.nlargest(1, list1)[0]
# printing the largest element
print("Largest element is:", largest_element)



