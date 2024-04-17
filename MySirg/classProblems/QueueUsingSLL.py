class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = self.rear = None


    def is_empty(self):
        return self.rear==None
    
    # Adding element to the queue
    def enqueue(self, data=None):
        if data is not None:
            newNode=Node(data)
            if self.is_empty():
                self.front=self.rear=newNode
            else:
                self.rear.next=newNode
                self.rear=newNode
        else:
            raise ValueError("None can't be add at the queue")

    # Removing element from the queue
    def dequeue(self):
        if not self.is_empty():
            tempData = self.front.data
            self.front = self.front.next
            if (self.front == None):
                self.rear = None
            return tempData
        else:
            raise IndexError('Queue is empty')
            
    def get_front(self):
        if not self.is_empty():
            return self.front.data
        else:
            raise IndexError('Queue is empty')
    
    def get_rear(self):
        if not self.is_empty():
            return self.rear.data
        else:
            raise IndexError('Queue is empty')
    
    def size(self):
        count = 0
        current = self.front
        while current != None:
            count += 1
            current = current.next
        return count
    



    

if __name__=="__main__":
    myQueue = Queue()

    print('1. For Enqueue in the queue')
    print('2. For Dequeue from the queue')
    print('3. For View Front from the queue')
    print('4. For View Rear from the queue')
    print('5. For get the size of the queue')
    print('0. For Exit.')

    while True:
        choice = int(input("\nEnter your choice: "))
        match choice:
            case 1:
                value = eval(input("Enter a number to be pushed into the queue: "))
                myQueue.enqueue(value)
                print(f'{value} is pushed in the queue')
            case 2:
                try:
                    result = myQueue.dequeue()
                    print(f"The element at top of the queue is {result}")
                except Exception as e:
                    print(e)
            case 3:
                try:
                    result = myQueue.get_front()
                    print(f"The element at top of the queue is {result}")
                except Exception as e:
                    print(e)
            case 4:
                try:
                    result = myQueue.get_rear()
                    print(f"The element at top of the queue is {result}")
                except Exception as e:
                    print(e)
            case 5:
                print(f'The size of the queue is {myQueue.size()}')

            case 0:
                quit(0)

            case _:
                print('\nInvalid Choice\n')
