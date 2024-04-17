
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self, start=None,next=None):
        self.start = start
        self.next=next
        self.item_count = 0

    def is_empty(self):
        return self.item_count == 0

    def push(self, data):
        newNode = Node(data)
        if not self.is_empty():
            newNode.next = self.start
            self.start = newNode
        else:
            self.start = newNode
        self.item_count += 1

    def pop(self):
        if self.is_empty():
            raise Exception('Empty Stack')
        else:
            popped_node = self.start
            self.start = popped_node.next
            self.item_count -= 1
            return popped_node.data

    def peek(self):
        if self.is_empty():
            raise Exception('Empty stack')
        else:
            return self.start.data

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
