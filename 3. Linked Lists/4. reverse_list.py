"""
Create a function that takes the head of a linked list as its input, and
outputs a reversed version
"""

class Node(object):

    def __init__(self, value):
        self.value = value
        self.nextnode = None


def reverse(head):
    current = head
    previous = None

    while current:
        nextnode = current.nextnode

        # trick is to make sure nextnode is done before erasing it for current.

        current.nextnode = previous
        # in the first instance here, the variable prev = none is given to the head, thus making it the end node

        previous = current
        current = nextnode
    return previous

a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)

a.nextnode = b
b.nextnode = c
c.nextnode = d


reverse(a)
print(d.nextnode.value)
print(c.nextnode.value)
print(b.nextnode.value)
