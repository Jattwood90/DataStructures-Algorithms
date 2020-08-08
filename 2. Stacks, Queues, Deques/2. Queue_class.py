"""
Queues - ordered collection of items. Additions - rear, Removals - front. First come, first served
Enqueue - term describes when we add a new item to the rear of the queue
Dequeue - term describes removing the front item from the queue

Method to the Class:
 - Queue() creates a new queue that is empty. Needs no parameters and is empty
  - enqueue(item) adds a new item to the rear of the queue. Needs no parameters and returns nothing
   - dequeue() removes the front item from the queue. Needs no parameters and returns the item. Queue is modified.
    - isEmpty() tests to see whether the queue is empty. Returns a boolean value
    - size() returns the numbers of items in the queue. Needs no parameters and returns an integer.
"""

class Queue(object):

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

q = Queue()
q.enqueue(1)
q.dequeue()
print(q.isEmpty())
