"""Instead of breaking the list into sublists, like insertion sort,
the shell sort uses an increment 'i' to create a sublist by choosing
all items that are 'i' items apart."""

def shell_sort(arr):
    sublistcount = len(arr) // 2

    # While we still have sub lists
    while sublistcount > 0:
        for start in range(sublistcount):
            # Use a gap insertion
            gap_insertion_sort(arr, start, sublistcount)

        #Comment out if you don't want to see it visualised each step
        print('After increments of size: ', sublistcount)
        print('List is: ',arr)

        sublistcount = sublistcount // 2


def gap_insertion_sort(arr, start, gap):
    for i in range(start + gap, len(arr), gap):

        currentvalue = arr[i]
        position = i

        # Using the Gap
        while position >= gap and arr[position - gap] > currentvalue:
            arr[position] = arr[position - gap]
            position = position - gap

        # Set current value
        arr[position] = currentvalue

arr = [45,67,23,45,21,24,7,2,6,4,90,5,65,36,2,745,7,97,45,8,96,44,23,12]
shell_sort(arr)
print(arr)