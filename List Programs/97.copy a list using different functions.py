#using enumerate
lst = [4, 8, 2, 10, 15, 18] 
li_copy = [i for a,i in enumerate(lst)] 
print("Original List:", lst) 
print("After Cloning:", li_copy) 

#using map function
lst = [4, 8, 2, 10, 15, 18]
li_copy = map(int, lst)
print("Original List:", lst)
print("After Cloning:", *li_copy)
