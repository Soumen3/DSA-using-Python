from SinglyLinkedList import SLL

class Stack:
    def __init__(self):
        self.Mylist=SLL()
        self.item_count=0
    
    def is_empty(self):
        return self.Mylist.is_empty()
    
    def push(self, data):
        self.Mylist.insert_at_first(data)
        self.item_count+=1

    def pop(self):
        if not self.is_empty():
            self.Mylist.delete_first()
            self.item_count-=1

    def peek(self):
        if not self.is_empty():
            return self.Mylist.start.item
        else:
            raise Exception ("Stack is Empty")
    
    def size(self):
        return self.item_count
    


myStack = Stack()

print('1. For Push in the stack')
print('2. For Pop from the stack')
print('3. For peek from the stack')
print('4. For get the size of the stack')
print('0. For Exit.')

while True:
    choice = int(input("\nEnter your choice: "))
    match choice:
        case 1:
            value = eval(input("Enter a number to be pushed into the stack: "))
            myStack.push(value)
            print(f'{value} is pushed in the stack')
        case 2:
            try:
                result = myStack.pop()
                print("The element at top of the stack is popped")
            except Exception as e:
                print(e)
        case 3:
            try:
                result = myStack.peek()
                print(f"The element at top of the stack is {result}")
            except Exception as e:
                print(e)
        case 4:
            print(f'The size of the stack is {myStack.size()}')

        case 0:
            quit(0)

        case _:
            print('\nInvalid Choice\n')
