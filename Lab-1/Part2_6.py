import timeit

def pow2(n):
    return 2 ** n

runs1 = 10000
time_pow2 = timeit.timeit(lambda: pow2(10000), number=runs1)

print("Timing pow2(10000)")
print("Total time for", runs1, "runs:", time_pow2, "seconds")
print("Average time per run:", time_pow2 / runs1, "seconds")
print()


def pow2_for(n):
    result = []
    for i in range(n+1):
        result.append(2 ** i)
    return result


def pow2_listcomp(n):
    return [2 ** i for i in range(n+1)]



runs2 = 1000
time_for = timeit.timeit(lambda: pow2_for(1000), number=runs2)
time_list = timeit.timeit(lambda: pow2_listcomp(1000), number=runs2)

print("Timing generation up to pow2(1000)")
print("For loop total time:", time_for, "seconds")
print("For loop average:", time_for / runs2, "seconds")
print()
print("List comprehension total time:", time_list, "seconds")
print("List comprehension average:", time_list / runs2, "seconds")