#Print numbers from 1 to 100 using while:
i = 1
while i <= 100:
    print(i)
    i += 1

#Print elements of list using while:
lst = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
i = 0
while i < len(lst):
    print(lst[i])
    i += 1

#Print numbers from 100 to 1 using while:
i = 100
while i >= 1:
    print(i)
    i -= 1

#Multiplication table of a number n using while:
n = int(input("Enter a number: "))
i = 1
while i <= 10:
    print(n, "x", i, "=", n * i)
    i += 1

#Search number x in tuple using while:
t = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
x = int(input("Enter number to search: "))
i = 0
found = False
while i < len(t):
    if t[i] == x:
        found = True
        break
    i += 1
print("Found" if found else "Not Found")

#Print list elements using loop:
lst = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
for i in lst:
    print(i)

#Search number x in tuple using for and range():
t = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
x = int(input("Enter number to search: "))
found = False
for i in range(len(t)):
    if t[i] == x:
        found = True
        break
print("Found" if found else "Not Found")

#Print numbers from 1 to 100:
for i in range(1, 101):
    print(i)

#Print numbers from 100 to 1:
for i in range(100, 0, -1):
    print(i)

#Multiplication table of number n:
n = int(input("Enter a number: "))
for i in range(1, 11):
    print(n, "x", i, "=", n*i)

#Sum of first n numbers (using while):
n = int(input("Enter n: "))
i = 1
sum = 0
while i <= n:
    sum += i
    i += 1
print("Sum =", sum)

#Factorial of number n (using for):
n = int(input("Enter a number: "))
fact = 1
for i in range(1, n+1):
    fact *= i
print("Factorial =", fact)