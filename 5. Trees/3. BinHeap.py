"""
Think of this as a list with index values.

 0  5  9 11 14 18 19 21 33 17 27
[0][1][2][3][4][5][6][7][8][9][10]

To find left node we do P (index)*2, e.g. for 5, the left is 1 * 2 = 2[9]
Right node: P (index)*2+1

"""


class BinaryHeap():
	#tree must remained balanced
	def __init__(self):
		self.heapList = [0]
		self.currentSize = 0

	def percUp(self, i):
		#perculates upwards until the insertion value is lower then child nodes,
		#but larger than parent
		while i // 2 > 0:
		#floor division ensures there's no floats returned
			if self.heapList[i] < self.heapList[i // 2]:
				tmp = self.heapList[i // 2]
				self.heapList[i // 2] = self.heapList[i]
				self.heapList[i] = tmp
			i = i // 2

	def insert(self, k):
		self.heapList.append(k)
		self.currentSize = self.currentSize + 1
		self.percUp(self.currentSize)


	def percDown(self, i):
		while (i * 2) <= self.currentSize:
			mc = self..minChild(i)
			if self.heapList[i] > self.heapList[mc]:
				tmp = self.heapList[i]
				self.heapList[i] = self.heapList[mc]
				self.heapList[mc] = tmp
			i = mc

	def minChild(self, i):
		if i * 2 + 1 > self.currentSize:
			return i * 2
		else:
			if self.heapList[i*2] < self.heapList[i*2+1]:
				return i * 2
			else:
				return i * 2 + 1


	def delMin(self):
		retval = self.heapList[1]
		self.heapList[1] = self.heapList[self.currentSize]
		self.currentSize = self.currentSize - 1
		self.heapList.pop()
		self.percDown(1)
		return retval
		pass

	def isEmpty():
		pass

	def size():
		pass

	def buildHeap(self, alist):
		i = len(alist) // 2
		self.currentSize = len(alist)
		self.heapList = [0] + alist[:]
		while (i > 0):
			self.percDown(i)
			i = i - 1
		pass
		#builds a new heap from a list of keys

