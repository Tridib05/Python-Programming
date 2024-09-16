# importing copy module
import copy

# initializing list 1 
li1 = [1, 2, [3,5], 4]

# using deepcopy for deepcopy 
li3 = copy.deepcopy(li1) 
print(li3)
