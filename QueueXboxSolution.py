"""
Queue music and dequeue music in a list
Add music to a linked list
Use a linked list to go back and for through website history
Use queue to see who order their Xbox first
Binary search trees use to see how many trucks sold above value and below value

"""

class Priority_Queue:

    class Node:
        
        def __init__(self, person, priority):
            self.person = person
            self.priority = priority

    def __init__(self):
        self.queue = []

    def enqueue(self, person, priority):
        new_node = Priority_Queue.Node(person, priority)
        self.queue.append(new_node)

    def dequeue(self):
        if len(self.queue) == 0:  # Verify the queue is not empty
            print("The queue is empty.")
            return None
        # Find the index of the item with the highest priority to remove
        high_pri_index = 0
        for index in range(0, len(self.queue)):
            if self.queue[index].priority < self.queue[high_pri_index].priority:
                high_pri_index = index
        # Remove and return the item with the highest priority
        person = self.queue[high_pri_index].person
        priority = self.queue[high_pri_index].priority
        del self.queue[high_pri_index]
        return "{} {}".format(person, priority)
        
    def __len__(self):
        return len(self.queue)

# Test 1
# Scenario: 
# Expected Result: 
print("People in line for Xbox ")

# Defect(s) Found: 
priority = Priority_Queue()
priority.enqueue("Jed", 2)
priority.enqueue("Ted", 4)
priority.enqueue("Sid", 1)
priority.enqueue("Jill", 6)
priority.enqueue("Joe", 7)
priority.enqueue("Sally", 5)
priority.enqueue("Ashley", 9)
priority.enqueue("Jon", 8)
priority.enqueue("Clark", 3)
priority.enqueue("Bruce", 1)

print(priority.dequeue())
print(priority.dequeue())
print(priority.dequeue())
print(priority.dequeue())
print(priority.dequeue())
print(priority.dequeue())
print(priority.dequeue())
print(priority.dequeue())
print(priority.dequeue())
print(priority.dequeue())
print("=================")
