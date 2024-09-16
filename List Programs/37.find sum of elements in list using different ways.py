#using enumerate function
list1 = [12, 15, 3, 10];s=0
for i,a in enumerate(list1): 
    s+=a 
print(s)

#using list comprehension 
list1 = [12, 15, 3, 10]
s=[i for i in list1] 
print(sum(s))

#using lambda function
list1 = [12, 15, 3, 10]
print(sum(list(filter(lambda x: (x),list1))))

#using add operator
import operator
list1 = [12, 15, 3, 10] ;s=0
for i in list1:
    s=s+operator.add(0,i)
print(s)


