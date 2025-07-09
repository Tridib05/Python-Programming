#Input user’s first name & print its length:
name = input("Enter your first name: ")
print("Length =", len(name))


#Find the occurrence of ‘$’ in a string:
s = input("Enter a string: ")
print("Count of $ =", s.count('$'))


#Check if a number is odd or even:
n = int(input("Enter a number: "))
print("Even" if n % 2 == 0 else "Odd")


#Find the greatest of 3 numbers:
a = int(input("A: "))
b = int(input("B: "))
c = int(input("C: "))
print("Greatest =", max(a, b, c))

#Check if a number is a multiple of 7 or not:
n = int(input("Enter a number: "))
print(n % 7 == 0)