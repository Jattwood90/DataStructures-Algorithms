"""
Deque - aka a double ended queue - this is an ordered collection of items similar to the queue
There are two ends, front and rear and the items remain positioned in the collection.

Deques as less restrictive than queue or stack, as objects can be removed or added to either front or rear

Methods and attribute

Deque() - creates new deque that is empty
addFront(item)
addRear(item)
removeFront(item)
removeRear(item) - all of these return a modified deque
isEmpty() - test to see if deque is empty
size() - checks the size of the deque
"""

class Deque(object):

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def addFront(self, item):
        self.items.append(item)

    def addRear(self, item):
        self.items.insert(0, item)

    def removeFront(self):
        self.items.pop()

    def removeRear(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)

d = Deque()

d.addFront('hello')
d.addRear('Hello World')

print(d.size())
