def fib_rec(n):
    if n<2:
        return n
    else:
        return fib_rec(n-1) + fib_rec(n-2)

def fib_loop(n):
    series = [0, 1]
    i = 2

    while(i<=n):
        series.append(series[i-1]+series[i-2])
        i += 1
    return series[n]

def factorial_rec(n):
    if (n<1):
        return 1
    else:
        return n * factorial_rec(n-1)

def factorial_loop(n):
    product = 1

    for i in range(n):
        product = (product * (i+1))
    return product

print((fib_rec(9)))

