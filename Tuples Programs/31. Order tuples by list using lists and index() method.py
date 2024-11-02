# Python3 code to demonstrate working of
# Order Tuples by List

# initializing list
test_list = [('Gfg', 3), ('best', 9), ('CS', 10), ('Geeks', 2)]

# printing original list
print("The original list is : " + str(test_list))

# initializing order list
ord_list = ['Geeks', 'best', 'CS', 'Gfg']

res=[]
x=[]
for i in test_list:
	x.append(i[0])
for i in ord_list:
	if i in x:
		res.append(test_list[x.index(i)])
# printing result
print("The ordered tuple list : " + str(res))
