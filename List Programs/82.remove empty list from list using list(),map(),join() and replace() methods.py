# Python3 code to Demonstrate Remove empty List

# Initializing list
test_list = [5, 6, [], 3, [], [], 9]

# printing original list
print("The original list is : " + str(test_list))
x=list(map(str,test_list))
y="".join(x)
y=y.replace("[]","")
y=list(map(int,y))

# printing result
print("List after empty list removal : " + str(y))
