"""
"""
import webbrowser

class LinkedList:

    class Node:

        def __init__(self, data):
 
            self.data = data
            self.next = None
            self.prev = None

    def __init__(self):

        self.head = None
        self.tail = None

    def insert_head(self, value):
 
        # Create the new node
        new_node = LinkedList.Node(value)  
        
        # If the list is empty, then point both head and tail
        # to the new node.
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        # If the list is not empty, then only self.head will be
        # affected.
        else:
            new_node.next = self.head # Connect new node to the previous head
            self.head.prev = new_node # Connect the previous head to the new node
            self.head = new_node      # Update the head to point to the new node

    
    def insert_tail(self, value):
        new_node = LinkedList.Node(value)  
        if self.tail is None:
            self.head = new_node
            self.tail = new_node
        # If the list is not empty, then only self.head will be
        # affected.
        else:
            new_node.prev = self.tail # Connect new node to the previous head
            self.tail.next = new_node # Connect the previous head to the new node
            self.tail = new_node  

    def remove_head(self):


        # If the list has only one item in it, then set head and tail 
        # to None resulting in an empty list.
        if self.head == self.tail:
            self.head = None
            self.tail = None
        # If the list has more than one item in it, then only self.head
        # will be affected.
        elif self.head is not None:
            self.head.next.prev = None  # Disconnect the second node from the first node
            self.head = self.head.next  # Update the head to point to the second node


    def remove_tail(self):

        if self.head == self.tail:
            self.head = None
            self.tail = None
        # If the list has more than one item in it, then only self.head
        # will be affected.
        elif self.tail != None:
            self.tail.prev.next = None  # Disconnect the second node from the first node
            self.tail = self.tail.prev

    def insert_after(self, value, new_value):

        # Search for the node that matches 'value' by starting at the 
        # head of the list.
        curr = self.head
        while curr is not None:
            if curr.data == value:
                # If the location of 'value' is at the end of the list,
                # then we can call insert_tail to add 'new_value'
                if curr == self.tail:
                    self.insert_tail(new_value)
                # For any other location of 'value', need to create a 
                # new node and reconenct the links to insert.
                else:
                    new_node = LinkedList.Node(new_value)
                    new_node.prev = curr       # Connect new node to the node containing 'value'
                    new_node.next = curr.next  # Connect new node to the node after 'value'
                    curr.next.prev = new_node  # Connect node after 'value' to the new node
                    curr.next = new_node       # Connect the node containing 'value' to the new node
                return # We can exit the function after we insert
            curr = curr.next # Go to the next node to search for 'value'

 
    def remove(self, value):

        curr = self.head  # Start at the begining since this is a forward iteration.
        while curr is not None:
            if curr.data == value:    
                curr.prev.next = curr.next
                curr.next.prev = curr.prev
            curr = curr.next
                

    
    def replace(self, old_value, new_value):

        curr = self.head  # Start at the begining since this is a forward iteration.
        while curr is not None:
            if curr.data == old_value:    
                curr.data = new_value
                
            curr = curr.next
        
                
        
    def __iter__(self):

        curr = self.head  # Start at the begining since this is a forward iteration.
        while curr is not None:
            yield curr.data  # Provide (yield) each item to the user
            curr = curr.next # Go forward in the linked list


    def __reversed__(self):

        curr = self.tail  # Start at the begining since this is a forward iteration.
        while curr is not None:
            yield curr.data  # Provide (yield) each item to the user
            curr = curr.prev
         # Replace this when you implement your solution

    def __str__(self):

        output = "Websites["
        first = True
        for value in self:
            if first:
                first = False
            else:
                output += ", "
            output += str(value)
        output += "]"
        return output
    
    def menu(self):
        yes = True
        website = self.head
        webbrowser.open(website.data)
        while yes:
            print("Please choose what you would like to do with the websites ")
            choice = input("n for next website, p for previous, d for delete and if you want to replace on enter r ")
            
            if choice == "n":
                website = website.next
                if website is None:
                    website = self.head
                    webbrowser.open(website.data)
                else:
                    webbrowser.open(website.data)
            
            if choice == "p":
                website = website.prev
                if website is None:
                    website = self.tail
                    webbrowser.open(website.data)
                else:
                    webbrowser.open(website.data)
            if choice == "r": 
                old = input("enter in the old url ")
                new = input("enter in the new url ")
                LinkedList.replace(self, old, new)
                print("replace")

    
# Sample Test Cases (may not be comprehensive) 
print("\n=========== PROBLEM 1 TESTS ===========")
ll = LinkedList()
ll.insert_tail("https://www.churchofjesuschrist.org/?lang=eng")
ll.insert_tail("https://www.churchofjesuschrist.org/study/scriptures?lang=eng&platform=web")
ll.insert_tail("https://www.churchofjesuschrist.org/study/scriptures/bofm?lang=eng")
ll.insert_tail("https://www.churchofjesuschrist.org/study/scriptures/bofm/2-ne/1?lang=eng")
ll.insert_tail("https://www.churchofjesuschrist.org/study/scriptures/bofm/2-ne/2?lang=eng")
ll.insert_tail("https://www.churchofjesuschrist.org/media/video/2020-08-0100-the-miracle-of-hope?lang=eng&collectionId=c2fcab35e519460680b1e15ab8ec2c0d")
ll.insert_tail("https://www.churchofjesuschrist.org/media/collection/gospel-art-images?lang=eng")
ll.insert_tail("https://www.churchofjesuschrist.org/media/collection/especially-for-youth-songs?lang=eng&collectionId=175c76f66b1d2b6846bd9d1b870394ec5af813f6")
ll.menu()
