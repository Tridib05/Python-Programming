#using lambda function
list1 = [-10, 21, 4, -45, -66, 93, -11] 
pos_nos = list(filter(lambda x: (x >= 0), list1))
print("Positive numbers in the list:", *pos_nos)

#using enumerate function
l=[12, -7, 5, 64, -14]
print([a for j,a in enumerate(l) if a>=0])

#using operator.ge()
list1 = [-10, 21, 4, -45, -66, 93, -11]
import operator
pos_nos = []
for i in list1:
    if operator.ge(i,0):
        pos_nos.append(i)
print("Positive numbers in the list: ", pos_nos)
