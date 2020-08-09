class Node(object):

    def __init__(self, value):

        self.value = value
        self.next_node = None
        


# Analogy is that there are two runners, one which is faster than the other. If they lap each other we know there's
# an infinite loop, otherwise None value will be found.

def cycle(Node):
    
    marker1 = Node
    marker2 = Node
    
    while marker2 != None and marker2.next_node != None:
        
        marker1 = marker1.next_node
        marker2 = marker2.next_node.next_node
        
        if marker2 == marker1:
            return True
        
    return False