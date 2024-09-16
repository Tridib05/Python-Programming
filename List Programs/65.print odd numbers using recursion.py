# Python program to print
# odd numbers in a list using recursion


def oddnumbers(list, n=0):
    # base case
    if n == len(list):
        exit()
    if list[n] % 2 != 0:
        print(list[n], end=" ")
    # calling function recursively
    oddnumbers(list, n+1)


list1 = [10, 21, 4, 45, 66, 93, 11]
print("odd numbers in the list:", end=" ")
oddnumbers(list1)
