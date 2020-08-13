# Google 5 ways of fibonacci in python (technobeans)

# Recursively
def fib_rec(n):
    # base case
    if n ==0 or n==1:
        return n
    # recursive case
    else:
        return fib_rec(n-1) + fib_rec(n-2)

# Iterative
def fib_it(n):
    a, b = 0, 1

    for i in range(n):
        a,b = b, a + b
    #nice pythonic solution for one line
    return a

# dynamic programming
n = 10
cache = [None]*(n+1)
# hardcoded n, not ideal but momoization is a more efficient use of memory

def fib_dyn(n):
    # base case
    if n ==0 or n ==1:
        return n

    # check cache
    if cache[n] != None:
        return cache[n]

    # keep setting cache
    cache[n] = fib_dyn(n-1) + fib_dyn(n-2)

    return cache[n]

print(fib_dyn(12))


