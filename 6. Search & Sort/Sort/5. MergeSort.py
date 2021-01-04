"""Merge sort is a recursive algorithm that continually
splits a list in half.
If the list is empty or has one item, it is sorted by definition
as this is the base case.
Otherwise, if the list has more than one item, it'll split
the list and recursively invoke a merge sort on both halves."""


def merge_sort(arr):
    #base case check
    if len(arr) > 1:
        mid = len(arr) // 2
        #dividing of list
        lefthalf = arr[:mid]
        righthalf = arr[mid:]

        merge_sort(lefthalf)
        merge_sort(righthalf)

        i = 0
        j = 0
        k = 0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                arr[k] = lefthalf[i]
                i = i + 1
            else:
                arr[k] = righthalf[j]
                j = j + 1
            k = k + 1

        while i < len(lefthalf):
            arr[k] = lefthalf[i]
            i = i + 1
            k = k + 1

        while j < len(righthalf):
            arr[k] = righthalf[j]
            j = j + 1
            k = k + 1

        #For visualisation purposes
        print('Merging: ', arr)

arr = [11,2,5,4,7,6,8,1,23]
merge_sort(arr)
print(arr)