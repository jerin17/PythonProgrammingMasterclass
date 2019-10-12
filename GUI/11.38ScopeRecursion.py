def fact(n):
    """calculate n! iteratively"""
    res = 1
    for j in range(1, n):
        if n > 1:
            res *= n
            n -= 1
    return res


def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)


def fib(n):
    if n == 0:
        res = 0
    elif n == 1:
        res = 1
    else:
        a = 0
        b = 1
        print(a)
        print(b)
        # c = a + b
        for x in range(n-1):
            c = a + b
            res = c
            print(res)
            a, b = b, c


def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)


print(fact(5))
fib(10)
print()
for i in range(10):
    print(fact(i))
print()
for i in range(10, 20):
    print(fact(i))
print()
for i in range(11):
    print(fibonacci(i))
