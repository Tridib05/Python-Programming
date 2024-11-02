# Python3 code to demonstrate working of
# Adding Tuple to List and vice - versa

# initializing list and tuple
test_list = [5, 6, 7]
test_tup = (9,10)

# printing original list
print("The original list is : " + str(test_list))

# Adding Tuple to List 
test_list.extend(list(test_tup))
# printing result
print("The container after addition : " + str(test_list))

#*********************************************************

# initializing list and tuple
test_list = [1,2,3,4]
test_tup=(5,6)

# printing original tuple
print("The original tuple is : " + str(test_tup))

#Adding list to tuple
test_tup=list(test_tup)
test_tup.extend(test_list)
test_tup=tuple(test_tup)
# printing result
print("The container after addition : " + str(test_tup))
