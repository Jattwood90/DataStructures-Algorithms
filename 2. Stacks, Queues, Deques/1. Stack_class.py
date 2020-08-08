"""Stacks: ordering principle is sometimes called LIFO, last-in first out
provides an ordering based on length of time in collection
Newer items are near the top, while older items are near the base.
"""

class Stack(object):

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == [] # returns a boolean response

    def push(self, items):
        self.items.append(items)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)

