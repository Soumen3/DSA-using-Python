

class PriorityQueue:
    def __init__(self):
        self.queue=[]

    def is_empty(self):
        return len(self.queue)==0

    def enqueue(self, data, priority):
        index=0
        while index<len(self.queue) and self.queue[index][1]<=priority:
            index+=1
        self.queue.insert(index,(data,priority))

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)[0]        
        else:
            raise IndexError('Priority Queue is empty')

    def size(self):
        return len(self.queue)
    

print("1. For enqueue.")
print("2. For dequeue.")
print("3. For get the size.")
print("0. For exit.")

myQueue= PriorityQueue()
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
