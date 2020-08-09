"""
Write a function that takes a head node and an integer value n, and then returns the nth to the last node
in the linked list
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.nextnode = None



def nthnode(n, head):
    left_pointer = head
    right_pointer = head

    for i in range(n-1):

        if not right_pointer.nextnode:
            raise LookupError('Error: n is larger than the linked list')

        right_pointer = right_pointer.nextnode

    while right_pointer.nextnode:

        left_pointer = left_pointer.nextnode
        right_pointer = right_pointer.nextnode

    return left_pointer

a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)

a.nextnode = b
b.nextnode = c
c.nextnode = d
d.nextnode = e

print(nthnode(2, a).value)

