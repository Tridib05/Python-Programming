#using lambda function
lst = [20, 10, 20, 1, 100]
print(min(lst, key=lambda value: int(value)) )

#using enumerate function
lst = [20, 10, 20, 1, 100] 
a,i = min((a,i) for (i,a) in enumerate(lst))
print(a)

#using reduce function
from functools import reduce
lst = [20, 10, 20, 15, 100]
print(reduce(min,lst) )

