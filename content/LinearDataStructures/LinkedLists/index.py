##Linked Lists
class Node:
    def __init__(self, data):
        self.data = data
        self.next_node = None

class LinkedList:
    def __init__(self):
        self.head = None

    # def add(self, data):
    #     my_node = Node(data)
    #     my_node.next_node = self.head
    #     self.head = my_node

    def reverse_linked_list(self, head):
        prev_node = None
        curr_node = head

        while curr_node:
            next_node = curr_node.next_node
            curr_node.next_node = prev_node
            prev_node = curr_node
            curr_node = next_node

        return prev_node

node1 = Node(10)
node2 = Node(20)
node3 = Node(30)

linked_list = LinkedList()
linked_list.head = node1
linked_list.head.next_node = node2
linked_list.head.next_node.next_node = node3


# while linked_list.head:
#     print(linked_list.head.data, end="\n")
#     linked_list.head = linked_list.head.next_node

reversed = LinkedList().reverse_linked_list(linked_list.head)

while reversed:
    print(reversed, end="\n")
    reversed.head = reversed.head.next_node