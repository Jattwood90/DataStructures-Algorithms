def find_missing(arr1, arr2):
    # check for neg num
    for i in arr2 and arr1:
        if i < 0:
            return "Negative number found"

    arr1.sort()
    arr2.sort()

    for k, v, in zip(arr1,arr2):
        if k != v:
            return k

    return arr1[-1]

# print(find_missing([1,2,3,4,5], [1,2,3,5]))

# hashtable solution
import collections

def finder(arr1, arr2):

    d = collections.defaultdict(int)

    for num in arr2:
        d[num] += 1
    for num in arr1:
        if d[num] ==0:
            return num
        else:
            d[num] -= 1



# use of truth tables/exclusive or (XOR) - no idea how this works
def finder3(arr1,arr2):
    result = 0

    for num in arr1+arr2:
        result^=num
        print(result)
    return result

print(finder3([1,2,3,4,5,5], [1,4,5,5]))
