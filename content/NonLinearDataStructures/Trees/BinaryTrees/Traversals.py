import BinarySearchTrees

binaryTree=BinarySearchTrees.BinaryTree

class Traversals(binaryTree):
    '''
    The class is dedicated to provide various traversal algorithms for the binary tree
    The class inherits from the BinaryTree class and uses the root property to traverse the tree
    '''
    def __init__(self):
        super().__init__()


    #Inorder Traversal -> Returns the nodes in the order of left child, parent node and right child
    def inorder_traversal(self):
        result=[]
        self._inorder_traversal_recursively(self.root,result)
        return result
    
    def _inorder_traversal_recursively(self,node,result):
        '''
        The traversal algorithm that visits the left child, then the parent node and finally the right child
        '''
        if node:
            self._inorder_traversal_recursively(node.left,result)
            result.append(node.value)
            self._inorder_traversal_recursively(node.right,result)



    #Preorder Traversal -> Returns the nodes in the order of parent node, left child and right child
    def preorder_traversal(self):
        result = []
        self._preorder_traversal_recursively(self.root, result)
        return result

    def _preorder_traversal_recursively(self, node, result):
        '''
        The traversal algorithm that visits the parent node first, then the left child and finally the right child
        '''
        if node:
            result.append(node.value)
            self._preorder_traversal_recursively(node.left, result)
            self._preorder_traversal_recursively(node.right, result)



    #Postorder Traversal -> Returns the nodes in the order of left child, right child and parent node
    def postorder_traversal(self):
        result = []
        self._post_order_traversal_recursively(self.root, result)
        return result

    def _post_order_traversal_recursively(self, node, result):
        '''
        The traversal algorithm that visits the left child, then the right child and finally the parent node
        '''
        if node:
            self._post_order_traversal_recursively(node.left, result)
            self._post_order_traversal_recursively(node.right, result)
            result.append(node.value)


'''
Creating the Tree instance
'''
tree = Traversals()
tree.insert(5)
tree.insert(3)
tree.insert(7)
tree.insert(1)
tree.insert(4)

if __name__ == '__main__':
    print(f"In Order  Traversal: ->{tree.inorder_traversal()}")
    print(f"PreOrder  Traversal: ->{tree.preorder_traversal()}")
    print(f"PostOrder Traversal: ->{tree.postorder_traversal()}")
