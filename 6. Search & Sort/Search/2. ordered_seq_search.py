def ordered_seq_search(arr, ele):

	#input array must be ordered/sorted

	position = 0
	found = False
	stopped = False

	while position < len(arr) and not found and not stopped:

		if arr[position] == ele:
			found = True

		else:

			if arr[position] > ele:
				stopped = True
			else:
				position += 1

	return found

print(ordered_seq_search([1,2,3,4,5,6,7,8,9], 10))