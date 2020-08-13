
# Create cache for known results
factorial_memo = {}

def factorial(k):

    if k < 2:
        return 1

    if not k in factorial_memo:
        factorial_memo[k] = k * factorial(k-1)

    return factorial_memo[k]

print(factorial(21))

# Class version of the above

class Memoize:
    def __init__(self, f):
        self.f = f
        self.memo = {} # cache for memo
        
    def __call__(self, *args):
        if not args in self.memo:
            self.memo[args] = self.f(*args)
        return self.memo[args]


# function required for implementing the class
def factorial(k):
    
    if k < 2: 
        return 1
    
    return k * factorial(k - 1)

factorial = Memoize(factorial)
