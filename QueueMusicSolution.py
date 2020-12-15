"""
"""
import pygame
from pygame import mixer
pygame.mixer.init()

class Priority_Queue:
    """
    This queue follows the same FIFO process except that higher priority
    nodes will be dequeued before lower priority nodes.  Nodes of the same
    priority will follow the same FIFO process.
    """

    class Node:
        """
        Each node is the queue will have both a song and a priority.
        """

        def __init__(self, song, priority):
            """
            Initialize a new node
            """
            self.song = song
            self.priority = priority
        def __str__(self):
            """
        Display a single node
        """
            return "{} {}".format(self.song, self.priority)

    def __init__(self):
        """ 
        Initialize an empty priority queue
        """
        self.queue = []

    def enqueue(self, song, priority):
        """
        Add a new song to the queue with an associated priority.  The
        node is always added to the back of the queue irregardless of 
        the priority.
        """
        new_node = Priority_Queue.Node(song, priority)
        self.queue.append(new_node)
        

    def dequeue(self):
        """
        Remove the next song from the queue based on the priority.  The 
        highest priority item will be removed.  In the case of multiple
        songs with the same high priority, the one closest to the front
        (in traditional FIFO order) will be removed.  Priority songs are
        interpreted as higher numbers have higher priority.  For example, 
        10 is a higher priority than 5.
        """
        if len(self.queue) == 0:  # Verify the queue is not empty
            print("end of play list")
            return False
        # Find the index of the item with the highest priority to remove
        high_pri_index = 0
        for index in range(0, len(self.queue)):
            if self.queue[index].priority < self.queue[high_pri_index].priority:
                high_pri_index = index
        # Remove and return the item with the highest priority
        song = self.queue[high_pri_index].song
        del self.queue[high_pri_index]
        return song
        
    def __len__(self):
        """
        Support the len() function
        """
        return len(self.queue)

    def __str__(self):
        """ 
        Suppport the str() function to provide a string representation of the
        priority queue.  This is useful for debugging.  If you have a 
        Priority_Queue object called pq, then you run print(pq) to see the 
        contents.
        """
        result = "["
        for node in self.queue:
            result += str(node)  # This uses the __str__ from the Node class
            result += ", "
        result += "]"
        return result
    
    def Play(self):
        true = True
        song = self.dequeue()
        pygame.mixer.music.load(song)
        pygame.mixer.music.play(0)
        print(song)
        print("If the song ends, press any key to jump to the next song")
        while true:
            Input = input("p to pause music, u to resume music, r to restart music, e to exit out ")
            #use keyboard commands instead of inputs
            while pygame.mixer.music.get_busy() == False:
                if len(self.queue) == 0:
                    true = False
                song = self.dequeue()
                pygame.mixer.music.load(song)
                pygame.mixer.music.play(0)
                print(song)
                
            if Input == "p":
                pygame.mixer.music.pause()
            
            if Input == "u":
                pygame.mixer.music.unpause()
                
            if Input == "r":
                pygame.mixer.music.rewind()
                pygame.mixer.music.play(0)
                print("rewind")
        
            if Input == "e":
                true = False
              
priority = Priority_Queue()
priority.enqueue("Silent Night.wav", 1)
priority.enqueue("What Child Is This.wav", 2)
priority.enqueue("Did you Think to Pray.wav", 3)
priority.enqueue("His Hands.wav", 4)
priority.enqueue("Im Trying to Be like Jesus.wav", 5)
priority.enqueue("Israel Israel God Is Calling.wav", 6)
priority.enqueue("Lord I Would Follow Thee.wav", 7)
priority.enqueue("Nearer My God to Thee.wav", 8)
priority.enqueue("O Come All Ye Faithful.wav", 9)
priority.enqueue("O Come Emmanuel - Christmas Version - ThePianoGuys.wav", 10)

priority.Play()
