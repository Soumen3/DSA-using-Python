"""     Doubly Linked List      """

class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev
        

class DoublyLinkedList:
    def __init__(self):
        self.start=None

    def is_empty(self):
        return self.start is None
    
    def insert_at_first(self, data=None):
        node=Node(data)
        node.prev=None
        if self.start is None:
            node.next=None
            self.start=node
        else:
            node.next=self.start
            self.start.prev=node
            self.start=node
        

    def insert_at_last(self, data=None):
        node=Node(data)
        node.next=None
        if self.is_empty():
            node.prev=None
            self.start=node
        else:
            cur=self.start
            while cur.next!=None:
                cur=cur.next
            node.prev=cur
            cur.next=node
        
    
    def search(self, data=None):
        cur=self.start
        while cur is not None:
            if cur.data==data:
                return cur
            cur=cur.next
        return None

    def insert_after(self, addr=None, data=None):
        if addr is not None:
            new_node=Node(data=data,prev=addr, next=addr.next)
            if addr.next is not None:
                addr.next.prev=new_node
            addr.next=new_node
        
            
            
    def display(self):
        cur = self.start
        while cur is not None:
            print(cur.data, end=" -> ")
            cur=cur.next
        print(None)
    

    def delete_first(self):
        if self.start is not None:
            if self.start.next is None:
                self.start=None
            else:
                self.start=self.start.next
                self.start.prev=None

    def delete_last(self):
        if self.start is not None:
            if self.start.next is None:
                self.start=None
            else:
                cur=self.start
                while cur.next is not None:
                    cur=cur.next
                cur.prev.next=None
            
    def delete_item(self, data):
        if self.start is not None:
            if self.start.data==data:
                if self.start.next is None:
                    self.start=None
                else:
                    cur=self.start
                    while cur.data != data:
                        cur=cur.next
                    cur.prev.next=cur.next
                    if cur.next is not None:
                        cur.next.prev=cur.prev


    def __iter__(self):
        return DLLIterator(self.start)






class DLLIterator:
    def __init__(self,start):
        self.current=start
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if not self.current :
            raise StopIteration
        data=self.current.data
        self.current=self.current.next
        return data
    


mylist=DoublyLinkedList()
    
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
            val = int (input ("Enter value to be inserted: "))
            mylist.insert_at_first(val)

        case 2:
            print ("Insertion at the end")
            val = int (input ("Enter value to be inserted: "))
            mylist.insert_at_last(val)
            
        case 3:
            print ("Insertion after a given node")
            key = int (input ("Enter the value of the node after which you want to insert:"))
            val = int (input ("Enter value to be inserted: "))
            mylist.insert_after(mylist.search(key),val)
            
        case 4:
            print ("Searching in Doubly Linked List")
            key = int (input ("Enter the element to be searched:"))
            result = mylist.search(key)
            if result is None:
                print ("Element is not present in Doubly Linked List")
            else:
                print ("Element found")
            
        case 5:
            print ("Displaying Doubly Linked List")
            mylist.display()
            
        case 6:
            print ("Deletion from front")
            mylist.delete_first()
            
        case 7:
            print ("Deletion from rear")
            mylist.delete_last()
            
        case 8:
            print ("Delete a specified node")
            key = int (input ("Enter the value of the node to be deleted:"))
            mylist.delete_item(key)
            
        case 9:
            print ("Reversing Doubly Linked list")
            mylist.reverse()
            
        case 0:
            quit(0)
            

        # case:
        #     print("Invalid choice, please enter again.")
            

