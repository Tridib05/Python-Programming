# Initializing list
test_list = [1, 6, 3, 5, 3, 4]

result = any(item in test_list for item in test_list)
print("Does string contain any list element : " +str(bool(result)))
