# Python3 code to demonstrate
# matrix creation of n * n
# using nested for loops

# initializing N
N = 4

# printing dimension
print("The dimension : " + str(N))

# initializing empty matrix
res = []
for i in range(N):
    row = []
    for j in range(N):
	    row.append(1 + N * i + j)
res.append(row)

# print result
print("The created matrix of N * N: " + str(res))
#This code is contributed by Jyothi pinjala.
