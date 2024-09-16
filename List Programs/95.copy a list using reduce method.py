from functools import reduce

def clone_list(li1):
	return reduce(lambda x, y: x + [y], li1, [])

# Driver Code
li1 = [4, 8, 2, 10, 15, 18]
li2 = clone_list(li1)
print("Original List:", li1)
print("After Cloning:", li2)
#This code is contributed by Jyothi pinjala.
