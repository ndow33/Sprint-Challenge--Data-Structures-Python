from reverse import Node

class RingBuffer:
    def __init__(self, capacity):
        self.head = None
        self.capacity = capacity
 
    def append(self, item):

        # is there a head 
        if self.head is None:
            # create a new node
            node = Node(item)
            # make the new node the head
            self.head = node
            # have the new node point to itself
            self.head.next_node = self.head
        else:
            # create a new node
            node = Node(item)
            # set current equal to head
            current = self.head
            # make a counter
            counter = 1
            # while the next node is not the head...
            while current.next_node is not self.head:
                # move down the list
                current = current.next_node
                # add to counter 
                counter += 1
            # once the next node is the head, 
            # change the next node to being the new node
            current.next_node = node
            # and make the next node of the new node
            # the head
            node.next_node = self.head
            # check to see if the counter is greater than or equal to capacity
            while counter >= self.capacity:
                # while it is, set the last node's next node 
                # to the node after the head node
                node.next_node = self.head.next_node
                # set the head to the last node's next node
                self.head = node.next_node
                # decrease counter by 1
                counter -= 1

         

    def get(self):
        current = self.head
        counter = 0
        data = []
        # if there is only one node...
        if self.head is self.head.next_node:
            data.append(self.head.value)
            return data
        while current is not None and counter < self.capacity:
            data.append(current.value)
            current = current.next_node
            counter +=1
        return data
        