class Queue(list):

    def is_empty(self):
        return len(self)==0

    def enqueue(self, data):
        self.append(data)

    def dequeue(self):
        if not self.is_empty():
            data=self[0]
            self.remove(self[0])
            return data
        raise IndexError('Queue is empty')
    
    def get_front(self):
        if not self.is_empty():
            return self[0]
        raise IndexError('Queue is empty')
    
    def get_rear(self):
        if not self.is_empty():
            return self[-1]
        raise IndexError('Queue is empty')
    
    
    def size(self):
        return len(self)
    



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
