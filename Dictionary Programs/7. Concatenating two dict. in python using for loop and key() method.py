# code
# Python code to merge dictionary
def Merge(d1, d2):
    for i in d2.keys():
        d1[i]=d2[i]
    return d1
    
# Driver code
d1 = {'x': 10, 'y': 8}
d2 = {'a': 6, 'b': 4}
dict3 = Merge(d1, d2)
print(dict3)

# This code is contributed by Bhavya Koganti
