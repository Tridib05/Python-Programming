def sumOfSeries(n):
    sum = 0
    for i in range(1, n + 1):
        sum += i * i * i

    return sum


# Driver Function
n = 5
print(sumOfSeries(n))



def sumOfSeries(n):
    x = (n * (n + 1) / 2)
    return (int)(x * x)



# Driver Function
n = 5
print(sumOfSeries(n))


def sumOfSeries(n):
    x = 0
    if n % 2 == 0:
        x = (n / 2) * (n + 1)
    else:
        x = ((n + 1) / 2) * n

    return (int)(x * x)


# Driver Function
n = 5
print(sumOfSeries(n))