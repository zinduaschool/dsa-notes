##Linked Lists
class Node:
    def __init__(self, data):
        self.data = data
        self.next_node = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, data):
        my_node = Node(data)
        my_node.next_node = self.head
        self.head = my_node

    def counting(self, data):
        #beginning = self.head -> the beginning
        #count = 0 -> counter variable
        #while beginning:
            #count +=1
            #beginning = beginning.next_node
        #return count
        pass