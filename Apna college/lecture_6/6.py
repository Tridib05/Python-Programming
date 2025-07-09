#WAF to print the elements of a list in a single line:
def print_list(lst):
    print(*lst)
print_list([1, 2, 3, 4])


#WAF to find the factorial of n:
def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result
print(factorial(5)) 


#WAF to print the length of a list:
def list_length(lst):
    print("Length =", len(lst))
list_length([10, 20, 30])


#WAF to convert USD to INR (assume 1 USD = 83 INR):
def usd_to_inr(usd):
    inr = usd * 83
    print("INR =", inr)
usd_to_inr(10) 


#Recursive function to calculate sum of first n natural numbers:
def sum_n(n):
    if n == 1:
        return 1
    return n + sum_n(n - 1)
print(sum_n(5))  


#Recursive function to print all elements in a list:
def print_elements(lst, index=0):
    if index < len(lst):
        print(lst[index])
        print_elements(lst, index + 1)
print_elements(["a", "b", "c"])