# This is a common interview problem. The solution is O(n) complexity

class Queue2Stacks(object):

    def __init__(self):

        self.instack = []
        self.outstack = []

    def enqueue(self,element):
        self.instack.append(element)

    def dequeue(self):
        if not self.outstack: #checks if outstack is empty
             while self.instack: #this checks if the instack is empty
                self.outstack.append(self.instack.pop())
        return self.outstack.pop()

"""
Pseudo code

create two stacks: stack1, stack2
push elements into stack1
this is the enqueue function (entering the queue)
check if stack1 is empty
if it isn't, pop the last element and push it into stack2
repeat until stack1 is empty
this is the dequeue function (leaving the queue)
once stack1 is empty, check if stack2 is empty
if it isn't, pop the last element and return it
repeat until stack2 is empty
"""
