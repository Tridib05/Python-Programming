#using lambda function
n="geeks for geek"
s=n.split(" ") 
l=list(filter(lambda x: (len(x)%2==0),s)) 
print(l)

#using list comprehension
n="geeks for geek"
s=n.split(" ")
print([x for x in s if len(x)%2==0])

#using enumerate function
n="geeks for geek"
s=n.split(" ")
print([x for i,x in enumerate(s) if len(x)%2==0])
