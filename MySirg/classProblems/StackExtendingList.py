
class StackExtendingList(list):
    def is_empty(self):
        return len(self) == 0
    
    def push(self, item):
        self.append(item)

    def pop(self):
        if not self.is_empty():
            return super().pop()
        else:
            raise IndexError( "Stack is empty")


    def peek(self):
        if not self.is_empty():
            return self[-1]
        else:
            return "Stack is empty"

    def size(self):
        return len(self)

    # Overriding list methods to prevent access to non-stack methods
    def sort(self, *args, **kwargs):
        raise AttributeError("Stack does not support sorting.")

    def reverse(self):
        raise AttributeError("Stack does not support reversal.")

    # Override other list methods not supported by the stack as needed

# Example usage:
stack = StackExtendingList()
stack.push(1)
stack.push(2)
stack.push(3)
print(stack.pop())
print(stack.peek())
print(stack)  # Output: [1, 2, 3] - Only stack methods are accessible
# stack.sort()  # Raises AttributeError: Stack does not support sorting.
