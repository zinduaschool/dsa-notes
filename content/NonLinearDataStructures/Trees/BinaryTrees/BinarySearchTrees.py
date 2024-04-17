'''
Implementation of the BinarySearch Tree using Python
Creating Nodes of a binarySearchTree and the various operations
'''
''

class Node:
    '''
    Node class, this will act as the constructor,
    param1/prop1: the instance will take in a  (value) that will act as the data inside the node

    prop2: right_pointer, this will be an optional property for the node since it expects 
    to have a chile node, the right pointer will point to the right child node
    
    prop3: left_pointer, this will be an optional property for the node since it expects 
    to have a chile node, the right pointer will point to the right child node
    '''
    def __init__(self, value): #constructor to instanciate node
        self.value = value #value/data
        self.right_pointer = None #right pointer
        self.left_pointer = None #left pointer



class BinaryTree:
    '''
    The BinaryTree
    prop1: Has a root property that will be the beginning or the base node of the BinaryTree, initially set to None
    '''
    def __init__(self):
        self.root = None


    def insert(self, value):
        '''
        Insert function to insert new nodes inside the binaryTree created
        '''
        if not self.root:   #determines if the root node is empty
            self.root = BinaryTree(value) #adds a new root node if empty
        else:
            self.insert_recursively(self.root, value) #inserts new children using recursive helper function
        


    def _insert_recursively(self, node, value):
        '''
        Recursive helper function that recursively insert new nodes/children to already existing nodes
        Inserts in an order in that the left child nodes are less than the parent nodes 
        '''
        if value < node.value: #checks if the value inserted is less than the parent node
            if node.left: #checks if the parent node is having a left child/pointer
                self._insert_recursively(node.left, value) #recursively inserting the new nodes with the same logic on the left
            else: #if there's no left child/pointer
                node.left = BinaryTree(value) #insert a new node on the left of the parent
        elif value > node.value:
            #does the same recursive call on the right side
            if node.right:
                self._insert_recursively(node.right, value)
            else:
                node.right = BinaryTree(value)


