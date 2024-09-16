# Python3 code to demonstrate
# matrix creation of n * n

# initializing N
N = 4

# printing dimension
print("The dimension : " + str(N))

# using list comprehension
# matrix creation of n * n
x=N*N
y=[]
for i in range(1,x+1):
	y.append(i)
res=[]
i=0
while(i<len(y)):
	a=y[i:i+N]
	res.append(a)
	i+=N
# print result
print("The created matrix of N * N: " + str(res))
