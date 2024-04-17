from SinglyLinkedList import SLL

class Queue(SLL):
    def is_Empty(self):
        return self.is_empty()
    
    def enqueue(self, data):
        self.insert_at_last(data)

    def dequeue(self):
        if not self.is_Empty():
            data= self.start.item
            self.delete_first()
            return data
        else:
            raise IndexError("Queue is Empty")

    def get_front(self):
        if not self.is_Empty():
            return self.start.item
        else:
            raise IndexError("Queue is Empty")
    
    def get_rear(self):
        if not self.is_Empty():
            temp=self.start
            while temp is not None:
                if temp.next is not None:
                    temp=temp.next
                else: break
            return temp.item
        else:
            raise IndexError("Queue is Empty")
    
    def size(self):
        if not self.is_Empty():
            temp=self.start
            count=0
            while temp is not None:
                count+=1
                temp=temp.next
                
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
