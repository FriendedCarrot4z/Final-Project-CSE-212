import pygame
from pygame import mixer
pygame.mixer.init()

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
 
    def remove(self, value):
        """
        In here add the code to remove nodes from the linked list.
        """
        curr = self.head  # Start at the begining since this is a forward iteration.
        pass

    
    def replace(self, old_value, new_value):
        """
        In here add the code to replace data inside of a node with
        different data.
        """
        curr = self.head  # Start at the begining since this is a forward iteration.
        pass
        
                
        
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
        song = self.head
        pygame.mixer.music.load(song.data)
        pygame.mixer.music.play(0) 
        print(song.data)
        while yes:
            choice = input("n for next song, p for the last song, r to replace a song and s to start over and q to quit: ")  
            if choice == "n":
                song = song.next
                if song is None: 
                    song = self.head
                    pygame.mixer.music.load(song.data)
                    pygame.mixer.music.play(0)
                    print(song.data)
                else:
                    pygame.mixer.music.load(song.data)
                    pygame.mixer.music.play(0)
                    print(song.data)
                
            if choice == "p":
                song = song.prev
                if song is None:
                    song = self.tail   
                    pygame.mixer.music.load(song.data)
                    pygame.mixer.music.play(0)
                    print(song.data)
                else:
                    pygame.mixer.music.load(song.data)
                    pygame.mixer.music.play(0)
                    print(song.data)
            if choice == "r": 
                old = input("enter in the old song ")
                new = input("enter in the new song ")
                LinkedList.replace(self, old, new)
                print("replace")
            
            if choice == "x":
                re = input("Enter in the song you wish to remove")
                remove(re) 
            
            if choice == "s":
                pygame.mixer.music.rewind()
                pygame.mixer.music.play(0)
                print("rewinded ", song.data)
            
            if choice == "q":
                yes = False

    
# Sample Test Cases (may not be comprehensive) 

print("\n=========== PROBLEM 1 TESTS ===========")
ll = LinkedList()
ll.insert_head("Did you Think to Pray.wav")
ll.insert_tail("His Hands.wav")
ll.insert_tail("Im Trying to Be like Jesus.wav")
ll.insert_tail("Israel Israel God Is Calling.wav")
ll.insert_tail("Lord I Would Follow Thee.wav")
ll.insert_tail("Nearer My God to Thee.wav")
ll.insert_tail("O Come All Ye Faithful.wav")
ll.insert_tail("O Come Emmanuel - Christmas Version - ThePianoGuys.wav")
ll.insert_tail("Silent Night.wav")
ll.insert_tail("What Child Is This.wav")
ll.menu()

