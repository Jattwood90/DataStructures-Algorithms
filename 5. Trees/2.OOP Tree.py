class BinaryTree(object):

    def __init__(self, rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self, newNode):

        if self.leftChild == None:
            self.leftChild = BinaryTree(newNode)
            #no left child, so adding to tree

        else:
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t
            #existing left child is pushed down the list

    def insertRight(self, newNode):

        if self.rightChild == None:
            self.rightChild = BinaryTree(newNode)

        else:
            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t

    def getRightChild(self):
        return self.rightChild

    def getLeftChild(self):
        return self.leftChild

    def setRootVal(self,obj):
        self.key = obj

    def getRootVal(self):
        return self.key


    #tree traversing functions
    def preorder(self):
        print(self.key)
        if self.leftChild:
            self.leftChild.preorder()
        if self.rightChild:
            self.rightChild.preorder()

    def postorder(BinaryTree):
        if BinaryTree != None:
            postorder(BinaryTree.getLeftChild())
            postorder(BinaryTree.getRightChild())
            print(tree.getRootVal())

    def inorder(BinaryTree):
        if BinaryTree != None:
            inorder(BinaryTree.getLeftChild())
            print(BinaryTree.getRootVal())
            inorder(BinaryTree.getRightChild())

 


r = BinaryTree('a')
r.insertLeft('b')
