from DoublyLinkedList import DLL

class Deque(DLL):

    def is_empty(self):
        return self.start==None
    
    def insert_front(self, data):
        self.insert_at_start(data)
    
    def insert_rear(self, data):
        self.insert_at_last(data)

    def delete_front(self):
        if not self.is_empty():
            data=self.start.item
            self.delete_first()
            return data
        else:
            raise Exception("Deque is empty!")
    
    def delete_rear(self):
        if not self.is_empty():
            data=self.get_rear()
            self.delete_last()
            return data
        else:
            raise Exception("Deque is empty!")
        
    def get_front(self):
        if not self.is_empty():
            return self.start.item
        else:
            raise Exception("Deque is empty!")
            
    def get_rear(self):
        if not self.is_empty():
            temp=self.start
            while temp.next!=None:
                temp=temp.next
            return temp.item
        else:
            raise Exception("Deque is empty!")
        
    def size(self):
        count = 0
        current = self.start
        while current != None:
            count += 1
            current = current.next
        return count
    
        
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