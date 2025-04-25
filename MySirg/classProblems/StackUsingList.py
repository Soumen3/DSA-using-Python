class Stack:
    def __init__(self):
        self.items=[]
    def is_empty(self):
        return (len(self.items)==0)
    def push(self,data):
        self.items.append(data)
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("Stack is Empty")
    
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("Stack is Empty")
    
    def size(self):
        return len(self.items)
    


"""Commenting out this portion because of Extending of this class in another programme"""
    
# s1=Stack()
# s1.push(1)
# s1.push(2)
# s1.push(3)
# s1.push(4)
# s1.push(5)
# s1.push(6)

# print("Top element is: ",s1.peek())
# print("removed element is: ",s1.pop())
# print("Top element is: ",s1.peek())

