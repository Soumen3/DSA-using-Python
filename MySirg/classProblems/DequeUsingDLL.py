class Node:
    def __init__(self, item=None, prev=None, next=None):
        self.item = item
        self.prev = prev
        self.next = next

class Deque:
    def __init__(self):
        self.start = None
    
    def is_empty(self):
        return self.start==None
    
    def insert_front(self, data):
        if not self.is_empty():
            new_node=Node(data)
            new_node.next=self.start
            self.start.prev=new_node
            self.start=new_node
        else:
            new_node = Node(data)
            self.start = new_node

    def insert_rear(self, data):
        if not self.is_empty():
            temp=self.start
            while (temp.next != None ):
                temp = temp.next
            new_node=Node(data)
            new_node.prev=temp
            temp.next=new_node
        else:
            new_node = Node(data)
            self.start = new_node

    def delete_front(self):
        if not self.is_empty():
            del_node = self.start
            self.start = self.start.next
            if self.start!=None :
                self.start.prev = None
            return del_node.item
        else:
            raise IndexError("Deque is empty!")
    
    def delete_rear(self):
        if not self.is_empty():
            temp=self.start
            while (temp.next != None ):
                temp = temp.next
            del_node = temp
            temp.prev.next = None
            return del_node.item
        else:
            raise IndexError("Deque is empty!")
    
    def get_front(self):
        if not self.is_empty():
            return self.start.item
        else:
            raise IndexError("Deque is empty!")
    
    def get_rear(self):
        if not self.is_empty():
            temp=self.start
            while (temp.next != None ):
                temp = temp.next
            return temp.item
        else:
            raise IndexError("Deque is empty!")
        
    def size(self):
        count = 0
        temp = self.start
        while (temp != None):
            count += 1
            temp = temp.next
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