# List of numbers
list1 = [-10, 21, -4, -45, -66, 93]
num = 0

# Using while loop     
while num < len(list1):
    # Checking condition
    if list1[num] >= 0:
        print(list1[num], end=" ")
    
    # Increment num 
    num += 1
