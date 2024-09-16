# Initialize the size of the matrix
n = 4

# Create the matrix using a list comprehension and the enumerate() function
matrix = [[i * n + j for j in range(1, n+1)] for i, _ in enumerate(range(n))]

# Print the matrix
print("The created matrix of N * N: "+ str(matrix))
#This code is contributed by Edula Vinay Kumar Reddy
