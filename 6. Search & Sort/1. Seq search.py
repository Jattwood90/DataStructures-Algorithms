def seq_search(arr, ele):

	position = 0
	found = False

	while position < len(arr) and not found:

		if arr[position] == ele:
			found = True

		else:
			position += 1

		return found
