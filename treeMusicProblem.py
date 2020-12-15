class BST:
    
    class Node:

        def __init__(self, data):

       
            self.data = data
            self.left = None
            self.right = None

    def __init__(self):

        self.root = None

    def insert(self, data):

        if self.root is None:
            self.root = BST.Node(data)
        else:
            self._insert(data, self.root)  # Start at the root

    def _insert(self, data, node):

        if data != node.data:
            if data <= node.data:
                # The data belongs on the left side.
                if node.left is None:
                    # We found an empty spot
                    node.left = BST.Node(data)
                else:
                    # Need to keep looking.  Call _insert
                    # recursively on the left sub-tree.
                    self._insert(data, node.left)
            elif data >= node.data:
                # The data belongs on the right side.
                if node.right is None:
                    # We found an empty spot
                    node.right = BST.Node(data)
                else:
                    # Need to keep looking.  Call _insert
                    # recursively on the right sub-tree.
                    self._insert(data, node.right)

    def __in__(self, data):

        return self._contains(data, self.root)  # Start at the root

    def _contains(self, data, node):
 
        pass

    def __iter__(self):

        yield from self._traverse_forward(self.root)  # Start at the root
        
    def _traverse_forward(self, node):

        if node is not None:
            yield from self._traverse_forward(node.left)
            yield node.data
            yield from self._traverse_forward(node.right)
        
    def __reversed__(self):
    
        yield from self._traverse_backward(self.root)  # Start at the root

    def _traverse_backward(self, node):

        if node is not None:
            yield from self._traverse_backward(node.right)
            yield node.data
            yield from self._traverse_backward(node.left)
             # Replace this when you implement your solution

    def get_height(self):

        if self.root is None:
            return 0
        else:
            return self._get_height(self.root)  # Start at the root

    def _get_height(self, node):
        """
        Here you will add the code to find the height of the tree
        You will use recursion to find the height
        """
        pass
            
    def average(self): #places all the items in the tree together
        length = 0
        sum = " "
        
        for x in self:
            length += 1 #total number of items in the tree
            
        for x in self:
            sum += x + ' '
            
        return sum, length 

# Sample Test Cases (may not be comprehensive) 
print("\n=========== PROBLEM 1 TESTS ===========")
tree = BST()
tree.insert("country")
tree.insert("rock")
tree.insert("pop")
tree.insert("rap")
tree.insert("metal")
tree.insert("k-pop")
tree.insert("blues")
tree.insert("jazz")
tree.insert("folk")
tree.insert("loli-fi")

print("the lowest to highest song level")
for x in tree:
    print(x)  

print("the lowest to highest song level")
for x in reversed(tree):
    print(x)  

print("list of songs and the length of the tree")
print(tree.average())

print("height of the tree")
print(tree.get_height())
