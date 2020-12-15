import pygame
from pygame import mixer
pygame.mixer.init()

class Priority_Queue:

    class Node:

        def __init__(self, song, priority):
            self.song = song
            self.priority = priority
        def __str__(self):
            return "{} {}".format(self.song, self.priority)

    def __init__(self):
        self.queue = []

    def enqueue(self, song, priority):
        new_node = Priority_Queue.Node(song, priority)
        self.queue.append(new_node)
        
    def dequeue(self):
        """
        In here create the base case for the dequeue and how to return and remove
        a song in the queue after it plays
        """
        pass
        # Find the index of the item with the highest priority to remove
        high_pri_index = 0
        for index in range(0, len(self.queue)):
            if self.queue[index].priority < self.queue[high_pri_index].priority:
                high_pri_index = index
        # Remove and return the item with the highest priority
        pass
        
    def __len__(self):
        return len(self.queue)

    def __str__(self):
        """
        Here you will add the code to make place the songs in the queue into a string
        """
        pass
    
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
