# Python3 code to demonstrate working of
# Flatten tuple of List to tuple
def flatten_tuple(tup):
	if not tup:
		return ()
	elif isinstance(tup[0], list):
		return flatten_tuple(tup[0]) + flatten_tuple(tup[1:])
	else:
		return (tup[0],) + flatten_tuple(tup[1:])

# initializing tuple

test_tuple = ([5, 6], [6, 7, 8, 9], [3])

# printing original tuple
print("The original tuple : " + str(test_tuple))

# Flatten tuple of List to tuple
res = flatten_tuple(test_tuple)
# printing result
print("The flattened tuple : " + str(res))
