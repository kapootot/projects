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

print((factorial_rec(24)))
print((factorial_loop(24)))