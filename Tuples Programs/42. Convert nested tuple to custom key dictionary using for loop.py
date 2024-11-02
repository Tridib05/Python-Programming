# initializing tuple 
test_tuple = ((4, 'Gfg', 10), (3, 'is', 8), (6, 'Best', 10)) 

# initializing keys 
keys = ['key', 'value', 'id']

# initializing result dictionary
res = []

# iterate over the tuple and construct the dictionary
for sub in test_tuple:
	sub_dict = {}
	for i in range(len(keys)):
		sub_dict[keys[i]] = sub[i]
	res.append(sub_dict)

# printing result 
print("The converted dictionary : " + str(res)) 
