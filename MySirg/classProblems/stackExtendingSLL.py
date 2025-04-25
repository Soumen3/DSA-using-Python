from SinglyLinkedList import *

class Stack(SLL):
    def __init__(self):
        super().__init__(None)
        self.item_count=0

    def is_empty(self):
        return super().is_empty()

    def push(self, data):
        super().insert_at_first(data)
        self.item_count+=1

    def pop(self):
        if not self.is_empty():
            data= self.start.item
            super().delete_first()
            self.item_count-=1
            return data
        else:
            raise Exception("Stack is empty")

    def peek(self):
        if not self.is_empty():
            return super().start.item
        else:
            raise Exception ("Stack is Empty")
        
    def size(self):
        return self.item_count
    


    def insert_at_last(self):
        raise Exception("You can't use this method in stack")
    def insert_after(self):
        raise Exception("You can't use this method in stack")
    def search(self):
        raise Exception("You can't use this method in stack")
    def print_list(self):
        raise Exception("You can't use this method in stack")
    def delete_last(self):
        raise Exception("You can't use this method in stack")
    def delete_item(self):
        raise Exception("You can't use this method in stack")
    


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
                print(f"The element at top of the stack is {result}")
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
