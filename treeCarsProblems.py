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
        
    def _traverse_forward(self, node): #moves from lowest to highest value

        if node is not None:
            yield from self._traverse_forward(node.left)
            yield node.data
            yield from self._traverse_forward(node.right)
        
    def __reversed__(self):
    
        yield from self._traverse_backward(self.root)  # Start at the root

    def _traverse_backward(self, node): #moves from highest to lowest value
        """
        Create away for the tree to iterate backwards or from right to left
        """
        pass
            
    def average(self):
        """
        add up all the values in the tree then divide them by the length of tree to find the average
        """
        pass
            

# Sample Test Cases (may not be comprehensive) 
print("\n=========== PROBLEM 1 TESTS ===========")
tree = BST()
tree.insert(25000)
tree.insert(24899)
tree.insert(22199)
tree.insert(27890)
tree.insert(28001)
tree.insert(24321)
tree.insert(25031)
tree.insert(23789)
tree.insert(29000)
tree.insert(24399)

print("list from lowest to highest sales")
for x in tree:
    print(x)  
    
print("list from highest to lowest sales")
for x in reversed(tree):
    print(x)  
    
print("average of the sales")
print(tree.average())
aver = tree.average()
if aver > 25000:
    diff = aver - 25000
    print("The cars sold for over their 25000 price by an average of $", diff)
