def pairs(lst, num):
    p = []
    for i in lst:
        for n in lst:
            if i + n == num:
                p.append([i, n])

    return p

#Solution
def pairs2(arr, k):

    if len(arr) < 2:
        return False

    # sets for tracking. This is a frequently used technique
    seen = set()
    output = set()

    for num in arr:
        target = k - num
        if target not in seen:
            seen.add(num)
        else:
            output.add(((min(num, target), max(num, target))))
    # return len(output) OR
    print('\n'.join(map(str,list(output))))

print(pairs2([1,2,3,4,5], 5))
