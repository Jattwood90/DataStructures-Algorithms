# find the largest continuous sum in an array. If all numbers are positive, then simply return the sum.

def largest_sum(arr):
    if len(arr) == 0:
        return 0
    max_sum = current = arr[0] # sets two variables as the first element of the list

    for num in arr[1:]:
        current = max(current+num, num)
        max_sum = max(max_sum, current)
    return max_sum

print(largest_sum([1,3,-1,5,6,-10])) # 14


