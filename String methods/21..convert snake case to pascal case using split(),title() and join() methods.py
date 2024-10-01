# Python3 code to demonstrate working of
# Convert Snake case to Pascal case

# initializing string
test_str = 'geeksforgeeks_is_best'

# printing original string
print("The original string is : " + test_str)

# Convert Snake case to Pascal case
x=test_str.split("_")
res=[]
for i in x:
	i=i.title()
	res.append(i)
res="".join(res)
# printing result
print("The String after changing case : " + str(res))
