"""         Doubley Linked List         """

class Node:
    def __init__(self, prev=None, item=None, next=None):
        self.prev=prev
        self.item=item
        self.next=next

class DLL:
    def __init__(self,start=None):
        self.start=start

    def is_empty(self):
        return self.start is None
    
    def insert_at_start(self,data):
        newNode=Node(prev=None,item=data,next=self.start)
        if not self.is_empty():
            self.start.prev=newNode
        self.start=newNode

    def insert_at_last(self, data):
        temp=self.start
        if self.start is not None:
            while temp.next is not None:
                temp=temp.next
        newNode=Node(prev=temp, item=data,next=None)
        if temp==None:
            self.start=newNode
        else:
            temp.next=newNode

    def search(self,data):
        temp=self.start
        while temp is not None:
            if temp.item==data:
                return temp
            temp=temp.next
        return None
    

    def insert_after(self, temp, data):
        if temp!= None:
            newNode=Node(item=data, prev=temp, next=temp.next)
            if temp.next is not None:
                temp.next.prev=newNode
            temp.next=newNode
        
    def print_list(self):
        temp=self.start
        while temp is not None :
            print(temp.item, end=' ')
            temp=temp.next
        
    def delete_first(self):
        if self.start is not None:
            self.start=self.start.next
            if self.start is None:
                self.start.prev=None
                
    def delete_last(self):
        if self.start is None:
            pass
        elif self.start.next is None:
            self.start=None
        else:
            temp=self.start
            while temp.next is not None:
                temp=temp.next
            temp.prev.next=None
    
    def delete_item(self,data):
        if self.start is None:
            pass
        else:
            temp=self.start
            while temp.next is not None:
                if temp.item==data:
                    if temp.next is not None:
                        temp.next.prev=temp.prev
                    if temp.prev is not None:
                        temp.prev.next= temp.next
                    else:
                        self.start=temp.next
                    break
                temp=temp.next

    def __iter__(self):
        return DLLIterator(self.start)
    
class DLLIterator:
    def __init__(self, start):
        self.current=start
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if not self.current:
            raise StopIteration
        data= self.current.item
        self.current=self.current.next
        return data



mylist=DLL()
mylist.insert_at_start(10)
mylist.insert_at_last(20)
mylist.insert_after(mylist.search(10),15)
for x in mylist:
    print(x, end=' ')