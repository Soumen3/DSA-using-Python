
class Node:
    def __init__(self, data=None, priority=None, next=None):
        self.data = data
        self.priority = priority
        self.next=next

class priorityQueue:
    def __init__(self):
        self.start = None
    def is_empty(self):
        return self.start== None
    
    def enqueue(self, data, priority):
        if  self.is_empty():
            newNode = Node(data, priority)
            self.start=newNode
        else:
            current = self.start
            while (current.next != None and current.next.priority < priority):
                current = current.next
                
            newNode = Node(data, priority)
            if current == self.start:
                newNode.next = self.start
                self.start = newNode
            else:
                newNode.next = current.next
                current.next = newNode

    def dequeue(self):
        if not self.is_empty():
            temp = self.start
            self.start = self.start.next
            return temp.data
        else:
            raise IndexError("Queue is empty!")
    
    def size(self):
        count = 0
        temp = self.start
        while temp!=None:
            count +=1
            temp = temp.next
        return count



   

print("1. For enqueue.")
print("2. For dequeue.")
print("3. For get the size.")
print("0. For exit.")

myQueue= priorityQueue()
while True:
    choice=int(input("\nEnter your choice: "))
    match(choice):
        case 1:   
            num = int(input("\nEnter a number to be added in queue: "))
            prio = int(input("\nEnter its priority level: "))
            myQueue.enqueue(num,prio)
            print("\nAdded successfully!")
        case 2:
            try:
                result = myQueue.dequeue()
                print("\nRemoved element from queue: ",result)
            except Exception as e:
                print("\n",e,"\n")
        case 3:
            print("\nSize of the queue: ",myQueue.size())
        case 0:
            print("\nThank You")
            quit()
            
        case _:
            print("\nInvalid Choice!! Please enter again.\n")
