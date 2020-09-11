class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

    def reverse_list(self, node, prev=None):
        # are there any nodes in the list?
        if node is None:
            return
        # set p to current node    
        p = node
        # set q to next node
        q = p.next_node

        if q is None:
            # we have reached the end of the list
            # set the last node to head.
            self.head = p
            return
        # if q is not none, iterate recursively
        q = self.reverse_list(q)

        p.next_node.next_node = p
        p.next_node = None

        # set the head equal to the last digit

        
        
