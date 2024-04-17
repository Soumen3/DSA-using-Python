from SinglyLinkedList import  SLL

class Queue:
    def __init__(self):
        self.queue=SLL()

    def is_empty(self):
        return self.queue.is_empty()
    
    def dequeue(self):
        if not self.is_empty():
            data=self.queue.start.item
            self.queue.delete_first()
            return data
        else:
            raise IndexError('Queue is empty')
        
    def enqueue(self, data):
        self.queue.insert_at_last(data)

    def get_front(self):
        if not self.is_empty():
            return self.queue.start.item
        else:
            raise IndexError('Queue is empty')
        
    def get_rear(self):
        if not self.is_empty():
            temp=self.queue.start
            while temp!=None:
                if temp.next!=None:
                    temp=temp.next
                else:
                    break
            return temp.item
        else:
            raise IndexError('Queue is empty')
        
    def size(self):
        if not self.is_empty():
            temp=self.queue.start
            count=0
            while temp!=None:
                temp=temp.next
                count+=1
            return count
        else:
            return 0
        


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
                print(f"The element at front of the queue  {result} is dequeued")
            except Exception as e:
                print(e)
        case 3:
            try:
                result = myQueue.get_front()
                print(f"The element at front of the queue is {result}")
            except Exception as e:
                print(e)
        case 4:
            try:
                result = myQueue.get_rear()
                print(f"The element at rear of the queue is {result}")
            except Exception as e:
                print(e)
        case 5:
            print(f'The size of the queue is {myQueue.size()}')

        case 0:
            quit(0)

        case _:
            print('\nInvalid Choice\n')
