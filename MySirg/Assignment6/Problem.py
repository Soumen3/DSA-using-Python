"""     Circular Doubly Linked List     """

class Node:
    def __init__(self, prev=None, item=None, next=None):
        self.prev=prev
        self.item=item
        self.next=next


class CDLL:
    def __init__(self,start=None):
        self.start=start
        

    def is_empty(self):
        return self.start is None

    def insert_at_start(self,data):
        newNode=Node(item=data)
        if self.is_empty():
            newNode.next=newNode
            newNode.prev=newNode
            self.start=newNode
        else:
            newNode.prev=self.start.prev
            newNode.next=self.start
            self.start.prev.next=newNode
            self.start.prev=newNode
            self.start=newNode
    
    def insert_at_last(self,data):
        if self.is_empty():
            self.insert_at_start(data)
        else:
            newNode=Node(item=data)
            newNode.prev=self.start.prev
            newNode.next=self.start
            self.start.prev.next=newNode
            self.start.prev=newNode

    def search(self,data):
        if not self.is_empty():
            temp=self.start
            if temp.next==temp:
                if temp.item==data:
                    return temp
                else: return None
            else:
                while temp.next != self.start:
                    if temp.item==data:
                        return temp
                    temp= temp.next
                if temp.item==data:
                    return temp
                else: return None

    def insert_after(self, temp=None, data=None):
        if not self.is_empty() and temp!=None:
            if temp.next==self.start:
                self.insert_at_last(data)
            else:
                newNode = Node(item=data)
                newNode.prev = temp
                newNode.next = temp.next
                temp.next.prev = newNode
                temp.next = newNode
                
    def printList(self):
        if not self.is_empty():
            temp=self.start
            while temp.next != self.start:
                print(temp.item,end=' -> ')
                temp=temp.next
            print(temp.item)
    
    def delete_first(self):
        if not self.is_empty():
            if self.start== self.start.next:
                self.start=None
            else:
                self.start.prev.next=self.start.next
                self.start.next.prev=self.start.prev
                self.start=self.start.next
    
    def delete_last(self):
        if not self.is_empty():
            if self.start== self.start.next:
                self.start=None
            else:
                self.start.prev.prev.next=self.start
                self.start.prev=self.start.prev.prev
    
    def delete_item(self, temp):
        if self.start != None and temp != None:
            if (temp == self.start):
                self.delete_first()
            elif (temp == self.start.prev):
                self.delete_last()
            else:
                temp.prev.next = temp.next
                temp.next.prev = temp.prev

    def __iter__(self):
        if self.is_empty():
            return CDLLIterator(None)
        return CDLLIterator(self.start)
    

class CDLLIterator:
    def __init__(self,start):
        self.current=start
        self.temp=start

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current is None:
            raise StopIteration("No more items")
        item=self.current.item
        self.current=self.current.next
        if self.current==self.temp:
            self.current=None
            return item
        return item
    



mylist=CDLL()

    
print('1 for insert at first')
print('2 for insert at last')
print('3 for insert after')
print('4 for search')
print('5 for display list')
print('6 for delete first')
print('7 for delete last')
print('8 for delete specific')
print('9 for check empty')
print('0 for exit')

while True:
    choice = int (input("Enter your choice: "))
    match choice:
        case 1:
            print ("Insertion at the beginning")
            val = eval (input ("Enter value to be inserted: "))
            mylist.insert_at_start(val)

        case 2:
            print ("Insertion at the end")
            val = eval (input ("Enter value to be inserted: "))
            mylist.insert_at_last(val)
            
        case 3:
            print ("Insertion after a given node")
            key = eval (input ("Enter the value of the node after which you want to insert:"))
            val = eval (input ("Enter value to be inserted: "))
            mylist.insert_after(mylist.search(key),val)
            
        case 4:
            print ("Searching in Doubly Linked List")
            key = eval (input ("Enter the element to be searched:"))
            result = mylist.search(key)
            if result is None:
                print ("Element is not present in Doubly Linked List")
            else:
                print ("Element found")
            
        case 5:
            print ("Displaying Doubly Linked List")
            mylist.printList()
            
        case 6:
            print ("Deletion from front")
            mylist.delete_first()
            
        case 7:
            print ("Deletion from rear")
            mylist.delete_last()
            
        case 8:
            print ("Delete a specified node")
            key = eval (input ("Enter the value of the node to be deleted:"))
            mylist.delete_item(mylist.search(key))
            
        case 9:
            print("The list is empty ") if mylist.is_empty() else print("The list is not empty")
            
        case 0:
            print("Your list is: ")
            for i in mylist:
                print(i,end=" ")
            quit(0)
            

        # case:
        #     print("Invalid choice, please enter again.")
                