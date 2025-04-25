class Node:
    def __init__(self, data=None, next=None):
        self.data=data
        self.next=next

class SLL:
    def __init__(self):
        self.start=None

    def is_empty(self):
        return self.start==None
    
    def insert_at_first(self, data):
        # if self.is_empty():
        #     self.start=Node(data)
        # else:
        #     node=Node(data)
        #     node.next=self.start
        #     self.start=node
        n=Node(data, self.start)
        self.start=n

    def _insertLast(self, root, data):
        if root.next==None:
            root.next=Node(data)
            return
        self._insertLast(root.next, data)
        

    def insert_at_last(self, data):
        if self.is_empty():
            self.start=Node(data)
        else:
            self._insertLast(self.start, data)

    
    def print_list(self):
        temp=self.start
        while temp is not None:
            print(temp.data, end=' ')
            temp=temp.next
        print()

    
    def insert_after(self, data, n):
        node=Node(data)
        temp=self.start
        while temp.data != n or temp is not None:
            temp=temp.next
        if temp is None:
            print('Node not found')
        else:
            node.next=temp.next
            temp.next=node
        
    def insert_before(self, data, n):
        node = Node(data)
        if n==self.start.data:
            self.insert_at_first(data)
            return
        temp=self.start
        while temp.next.data != n or temp.next is not None:
            temp=temp.next
        if temp.next is None:
            print('Node not found')
        else:
            node.next=temp.next
            temp.next=node

    def delete_first(self):
        if self.is_empty():
            print('List is empty')
        else:
            self.start=self.start.next
            
    def delete_last(self):
        if self.is_empty():
            print('List is empty')
        elif self.start.next is None:
            self.start=None
        else:
            temp=self.start
            while temp.next.next is not None:
                temp=temp.next
            temp.next=None

    def delete_node(self, n):
        if self.is_empty():
            print('List is empty')
        elif self.start.data==n:
            self.delete_first()
        else:
            temp=self.start
            while temp.next.data != n or temp.next is not None:
                temp=temp.next
            if temp.next is None:
                print('Node not found')
            else:
                temp.next=temp.next.next

            



s=SLL()
s.insert_at_first(10)
s.insert_at_first(20)
s.insert_at_first(30)
s.insert_at_last(40)
s.insert_at_last(50)
s.insert_at_last(60)
s.print_list()