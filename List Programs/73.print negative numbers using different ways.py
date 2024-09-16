#using lambda fucntion
list1 = [-10, 21, 4, -45, -66, 93, -11]
neg_nos = list(filter(lambda x: (x < 0), list1))
print("Negative numbers in the list: ", *neg_nos)

#using enumerate function
l=[12, -7, 5, 64, -14]
print([a for j,a in enumerate(l) if a<0])
