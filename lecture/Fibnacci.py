import timeit
def fibonacci(n, a = 0, b = 1):
    if n == 0:
        return a
    else:
        return fibonacci(n-1, b, a + b)



time1 = timeit.timeit(lambda : fibonacci(35), number=1)
print(time1)