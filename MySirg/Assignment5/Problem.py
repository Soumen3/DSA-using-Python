"""     Circular Linked List        """

class Node:
    def __init__(self, item=None, next=None):
        self.item=item
        self.next=next

class CLL:
    def __init__(self,last=None):
        self.last=last

    def is_empty(self):
        return self.last is None

    def insert_at_start(self, item=None):
        newNode=Node(item=item)
        if self.last is None:
            newNode.next,self.last=newNode,newNode
        else:
            newNode.next=self.last.next
            self.last.next=newNode

    def insert_at_last(self, item=None):
        newNode=Node(item=item)
        if self.last is None:
            newNode.next,self.last=newNode,newNode
        else:
            newNode.next=self.last.next
            self.last.next=newNode
            self.last=newNode

    def search(self, data=None):
        if self.last is not None:
            if data is not None:
                cur=self.last
                if cur.item==data: 
                    return cur
                while cur.next is not self.last:
                    if cur.item == data:
                        return cur
                    cur=cur.next
    
    def insert_after(self, ref=None, data=None):
        if self.last is not None and ref is not None:
            newNode=Node(item=data)
            if ref == self.last:
                newNode.next=self.last.next
                self.last.next=newNode
                self.last=newNode
            else:
                cur=self.last.next
                while cur != ref and cur != self.last:
                    cur=cur.next
                if cur != self.last:
                    newNode.next=cur.next 
                    cur.next=newNode
    
    def display(self):
        if self.last is not None:
            cur=self.last.next
            while cur is not self.last:
                print(cur.item, end=' -> ')
                cur=cur.next
            print(self.last.item, end=' -> ')

        else:
            print("\nThe list is empty\n")

    def delete_first(self):
        if self.last is not None:
            if self.last==self.last.next:
                self.last=None
            else:
                self.last.next=self.last.next.next
    
    def delete_last(self):
        if self.last is not None:
            if self.last==self.last.next:
                self.last=None
            else:
                cur=self.last.next
                while cur.next is not self.last:
                    cur=cur.next 
                cur.next=self.last.next
                self.last=cur

    def delete_item(self, item=None):
        if self.last is not None:
            if self.last.item==item:
                if self.last==self.last.next:
                    self.last=None
                else:
                    cur=self.last.next
                    while cur.next is not self.last:
                        cur=cur.next 
                    cur.next=self.last.next
                    self.last=cur
            elif self.last.next.item==item:
                self.last.next=self.last.next.next
            else:
                cur=self.last.next.next 
                while cur.next is not self.last and cur.next.item != item:
                    cur=cur.next 
                cur.next=cur.next.next
                


mylist=CLL()
    
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
            mylist.insert_at_start(val)

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
            print("The list is empty ") if mylist.is_empty() else print("The list is not empty")
            
        case 0:
            quit(0)
            

        # case:
        #     print("Invalid choice, please enter again.")