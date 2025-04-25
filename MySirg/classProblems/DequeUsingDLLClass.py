
from DoublyLinkedList import DLL

class Deque():
    def __init__(self):
        self.deque = DLL()
    
    def is_empty(self):
        return self.deque.start == None
    
    def insert_front(self, data):
        self.deque.insert_at_start(data)

    def insert_rear(self, data):
        self.deque.insert_at_last(data)
    
    def delete_front(self):
        if not self.is_empty():
            data=self.get_front()
            self.deque.delete_first()
            return data
        else:
            raise IndexError('Deque is empty!')
        
    def delete_rear(self):
        if not self.is_empty():
            data=self.get_rear()
            self.deque.delete_last()
            return data
        else:
            raise IndexError('Deque is empty!')
        
    def get_front(self):
        if not self.is_empty():
            return self.deque.start.item
        else:
            raise IndexError('Deque is empty!')
        
    def get_rear(self):
        if not self.is_empty():
            temp=self.deque.start
            while temp.next != None:
                temp=temp.next
            return temp.item
        else:
            raise IndexError('Deque is empty!')
        
    def size(self):
        if not self.is_empty():
            count=0
            temp=self.deque.start
            while temp.next != None:
                temp=temp.next
                count+=1
            return count+1
        else:
            return 0
        
myDeque=Deque()

print('1. Insert from front.')
print('2. Insert from rear.')
print('3. Delete from front.')
print('4. Delete from rear.')
print('5. Get the element at the front of the deque.')
print('6. Get the element at the rear of the deque.')
print('7. Get the size of the deque.')
print('0. For exit.')

while True:
    choice = int(input('Enter your choice: '))
    if choice==0:
        break
    elif choice == 1:
        myDeque.insert_front(int(input("Enter the data: ")))
    elif choice == 2:
        myDeque.insert_rear(int(input("Enter the data: ")))
    elif choice==3:
        try:
            print(myDeque.delete_front()," is popped")
        except Exception as e:
            print(e)
    elif choice == 4:
        try:
            print(myDeque.delete_rear()," is popped")
        except Exception as e:
            print(e)
    elif choice == 5:
        try:
            print("Front element is",myDeque.get_front())
        except Exception as e:
            print (e)
    elif choice ==6:
        try:
            print("Rear element is",myDeque.get_rear())
        except Exception as e:
            print (e)
    elif choice ==7:
        print("Size of Deque is ",myDeque.size())
    else:
        print("Invalid Choice")