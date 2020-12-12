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

    #############
    # Problem 1 #
    #############
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

    #############
    # Problem 2 #
    #############
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

    #############
    # Problem 3 #
    #############
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

    #############
    # Problem 4 #
    #############
    def _get_height(self, node):
  
        if node is None:
            return 0
        else:
            left = self._get_height(node.left)
            right = self._get_height(node.right)
            
            if (left > right):
                return left + 1
            else:
                return right + 1
            
    def average(self):
        length = 0
        sum = 0
        
        for x in self:
            length += 1
            
        for x in self:
            sum += x
            
        return int(sum / length)
            
            
        

# NOTE: Funtions below are not part of the BST class above. 

def create_bst_from_sorted_list(sorted_list):
 
    bst = BST()  # Create an empty BST to start with 
    _insert_middle(sorted_list, 0, len(sorted_list)-1, bst)
    return bst

#############
# Problem 5 #
#############
def _insert_middle(sorted_list, first, last, bst):
  
    if first > last:
        return None
    middle = first + ((last - first) // 2)
    print(middle)
    bst.insert(sorted_list[middle])
    
    _insert_middle(sorted_list, first, middle - 1, bst )
    
    _insert_middle(sorted_list, middle + 1, last, bst)
       
    return

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
# for x in tree:
#     print(x)  # 1, 3, 5, 7, 10
print(tree.average())
# sorted_list = ([25000,24899,22199,27890,28001,24321,25031,23789,29000,24399])
# print("\n=========== PROBLEM 2 TESTS ===========")
# print(3 in tree) # True
# print(4 in tree) # False

# print("\n=========== PROBLEM 3 TESTS ===========")
# for x in reversed(tree):
#     print(x)  # 10, 7, 5, 3, 1

# print("\n=========== PROBLEM 5 TESTS ===========")
# tree = create_bst_from_sorted_list(sorted_list)# 7 .. any higher and its not balanced
