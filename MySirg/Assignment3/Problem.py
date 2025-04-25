class Node:
    def __init__(self, item=None, next=None):
        self.item=item
        self.next=next

class SLL:
    def __init__(self,start=None):
        self.start=start
    
    def is_empty(self):
        return self.start==None
        
    def insert_at_start(self, item):
        if self.is_empty():
            self.start=Node(item)
        else:
            node=Node(item,self.start)
            self.start=node

    def insert_at_last(self, item):
        if self.is_empty():
            self.start=Node(item)
        else:
            temp=self.start
            while temp.next!=None:
                temp=temp.next
            temp.next=Node(item)
    
    def search(self, value):
        if self.is_empty():
            print("The list is empty")
        else:
            temp=self.start
            count=0
            while temp!=None:
                count+=1
                if temp.item==value:
                    return count
                temp=temp.next
            else:
                return 0

    def insert_after(self, item, value):
        temp=self.start
        while temp!=None:
            if temp.item==item:
                break
            temp=temp.next
        else:
            print("Element is not found")
        
        node=Node(value)
        node.next=temp.next
        temp.next=node


    def display(self):
        if self.is_empty():
            print("The list is empty")
        else:
            print("The list is:")
            temp=self.start
            while(temp!=None):
                print(temp.item, end=' ')
                temp=temp.next

    def delete_first(self):
        if self.is_empty():
            print("The list is already empty")
        else:
            self.start=self.start.next
            print("\nThe first element is deleted")
        
    def delete_last(self):
        if self.is_empty():
            print("The list is already empty")
        elif self.start.next==None:
            self.start=None
        else:
            temp=self.start
            while temp.next.next:
                temp=temp.next
            temp.next=None
        print("\nThe last element is deleted")

    def delete_element(self, value):
        if self.is_empty():
            print("The list is already empty")
        elif self.start.next is None:
            if self.start.item==value:
                self.start=None
        else:
            temp=self.start
            while temp.next.item!=value:
                temp=temp.next
            else:
                print("Element not found")
            temp.next=temp.next.next
        print(f"\n{value} is deleted")
            

lst=SLL()
lst.insert_at_start(39)
lst.insert_at_start(38)
lst.insert_at_start(37)
lst.insert_at_start(36)
lst.insert_at_start(35)

lst.insert_at_last(40)
lst.insert_at_last(41)
lst.insert_at_last(42)
lst.insert_at_last(43)
lst.insert_at_last(44)

lst.insert_after(40, 90)
lst.insert_after(41, 91)
lst.insert_after(44, 81)
lst.insert_after(35, 88)

position=lst.search(39)
if position:
    print(f"The element is found at {position} position")
else:
    print("The element is not found")
lst.display()
lst.delete_first()
lst.display()
lst.delete_last()
lst.display()
lst.delete_element(90)
lst.display()
print("\nThe list is empty") if lst.is_empty() else print("\nThe list is not empty")