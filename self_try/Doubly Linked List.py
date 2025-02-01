class Node:
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next

class DLL:
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head is None
    
    def insert_at_start(self, data):
        node=Node(data,prev=None, next=self.head)
        if self.is_empty():
            self.head = node
            self.tail = node
        else:
            self.head.prev=node
            self.head=node

    def insert_at_end(self, data):
        node=Node(data=data, prev=self.tail, next=None)
        if self.is_empty():
            self.head = node
            self.tail = node
        else:
            self.tail.next=node
            self.tail=node

    def insert_before(self, data, node):
        if self.is_empty():
            print("The list is already empty!")
            return
        temp=self.head
        while temp is not None:
            if temp.data == node:
                break
            temp=temp.next

        if temp is None:
            print("The node is not found!")
            return
        

        if self.head is temp:
            self.insert_at_start(data)
        else:
            newNode=Node(data)
            newNode.next=temp
            newNode.prev=temp.prev
            temp.prev.next=newNode
            temp.prev=newNode

    def insert_after(self, data, node):
        if self.is_empty():
            print("The list is already empty!")
            return
        
        temp=self.head
        while temp is not None:
            if temp.data == node:
                break
            temp=temp.next

        if temp is None:
            print("The node is not found!")
            return
        
        if self.tail is temp:
            self.insert_at_end(data)
        else:
            newNode=Node(data)
            newNode.next=temp.next
            newNode.prev=temp
            temp.next.prev=newNode
            temp.next=newNode

    def delete_first(self):
        if self.is_empty():
            print("List is already empty!")
            return
        
        self.head=self.head.next
        if not self.head:
            self.tail=self.head
        else:
            self.head.prev=None

    def delete_last(self):
        if self.is_empty():
            print("List is already empty!")
            return
        
        self.tail=self.tail.prev
        if not self.tail:
            self.head=self.tail
        else:
            self.tail.next=None

    def delete_item(self, key):
        if self.is_empty():
            print("List is already empty!")
            return
        temp=self.head
        while temp:
            if temp.data==key:
                break
            temp=temp.next
        
        if not temp:
            print("Node is not found!")
            return

        if temp is self.head:
            self.delete_first()
        elif temp is self.tail:
            self.delete_last()
        else:
            temp.prev.next=temp.next 
            temp.next.prev=temp.prev

    
    def printList(self):
        if self.is_empty():
            print("The list is already empty!")
            return
        temp=self.head
        while temp is not None:
            print(temp.data, end=" ")
            temp=temp.next

            
    def printReverseList(self):
        if self.is_empty():
            print("The list is already empty!")
            return
        temp=self.tail
        while temp is not None:
            print(temp.data, end=" ")
            temp=temp.prev




lst=DLL()
lst.insert_at_start(10)
lst.delete_first()
lst.insert_at_start(12)
lst.delete_first()
lst.insert_at_start(20)

lst.insert_at_start(30)

lst.insert_at_end(40)
lst.insert_at_end(50)
lst.insert_at_end(60)

lst.insert_before(15, 20)
lst.insert_before(5, 30)

lst.insert_after(25, 60)
lst.insert_after(35, 50)

lst.printList()
print()
# lst.printReverseList()

lst.delete_first()
lst.delete_last()
lst.printList()
print()
lst.delete_item(40)
lst.printList()


