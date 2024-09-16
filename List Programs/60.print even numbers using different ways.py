#using enumerate
list1 = [2, 7, 5, 64, 14]
for a, i in enumerate(list1):
    if i % 2 == 0:
        print(i, end=" ")

#using pass
list1 = [2, 7, 5, 64, 14]
for i in list1:
    if (i % 2 != 0):
        pass
    else:
        print(i, end=" ")

#using not and bitwise & operator 
list1=[39,28,19,45,33,74,56] 
for element in list1:
  if not element&1:
    print(element,end=' ')

#using bitwise | operator
list1=[39,28,19,45,33,74,56]
for element in list1:
    if  element|1 != element: 
        print(element,end=' ')

#using reduce method
from functools import reduce
list1 = [39,28,19,45,33,74,56]
even_numbers = reduce(lambda x, y: x + [y] if y % 2 == 0 else x, list1, [])
for num in even_numbers:
    print(num, end=" ")