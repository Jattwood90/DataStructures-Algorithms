"""
Definition:
A tree consists of a set of nodes and a set of edges that connect pairs of nodes. A tree has to have the following properties:
 - One node of the tree designated as the root node.
 - Every node n, except the root node, is connected by an edge from exactly one other node p, where p
    is the parent of n.
 - A unique path traverses from the root to each node.
 - If each node in th etree has a maximum of two children, we say that the tree is a binary tree.

"""

# List representation [root, left-sub, right-sub] - Normally you wouldn't use this, OOP is instead better.

def binarytree(r):
    return [r, [],[]]

def insertLeft(root, newbranch):
    t = root.pop(1)

    if len(t) > 1:
        root.insert(1, [newbranch, t, []])
    else:
        root.insert(1,[newbranch, [],[]])
    return root

def insertRight(root, newbranch ):
    t = root.pop(2)

    if len(t) > 1:
        root.insert(2, [newbranch,[],t])
    else:
        root.insert(2,[newbranch,[],[]])

    return root

def getRootVal(root):
    return root[0]

def setRootVal(root, newVal):
    root[0] = newVal

def getLeftChild(root):
    return root[1]

def getRightChild(root):
    return root[2]

r = binarytree(3)
insertLeft(r, 4)
insertRight(r, 6)
insertRight(r, 7)

print(r)

