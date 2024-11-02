import itertools

# initializing tuples
test_tuple1 = (4, 5)
test_tuple2 = (7, 8)

# printing original tuples
print("The original tuple 1 : " + str(test_tuple1))
print("The original tuple 2 : " + str(test_tuple2))

# generating all pair combinations of 2 tuples using list comprehension
res = [(a, b) for a in test_tuple1 for b in test_tuple2] + [(a, b) for a in test_tuple2 for b in test_tuple1]

# printing result
print("All pair combinations of 2 tuples : " + str(res))
#This code is contributed by Jyothi pinjala.
