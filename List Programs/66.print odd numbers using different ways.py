#using pass
lst = [10, 21, 4, 45, 66, 93, 11]
for i in lst:
    if i % 2 == 0:
        pass
    else:
        print(i, end=" ")

#using enumerate function
list1 = [2, 7, 5, 64, 14] 
for a,i in enumerate(list1):
  if i%2!=0:
    print(i,end=" ")

#using bitwise & operator
list1 = [9,5,4,7,2]

for ele in list1:
  if ele & 1: 
    print(ele,end=" ") 

#using bitwise | operator
list1 = [9,5,4,7,2]
for ele in list1:
  if ele | 1==ele: 
    print(ele,end=" ") 
    
#using filter function
def is_odd(number):
   return number % 2 == 1

def print_odd_numbers(numbers):
  odd_numbers = list(filter(is_odd, numbers))
  return odd_numbers

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(print_odd_numbers(numbers))
 


 


 

