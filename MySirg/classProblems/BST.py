class Node:
    def __init__(self, item=None, left=None, right=None):
        self.item=item
        self.left=left
        self.right=right


class BST:
    def __init__(self):
        self.root=None
    
    # using recursion
    def insert(self, data):
        self.root=self.rinsert(self.root, data)
    
    # recursive function 
    def rinsert(self, root,data):
        if root is None:
            return Node(data)
        if data < root.item:
            root.left=self.rinsert(root.left, data)
        elif data > root.item:
            root.right=self.rinsert(root.right, data)

        return root

    # using recursion
    def search(self, data):
        return self.rsearch(self.root, data)
    
    # recursive function 
    def rsearch(self, root, data):
        if root is None or root.item == data:
            return root
        if data<root.item:
            return self.rsearch(root.left, data)
        else:
            return self.rsearch(root.right, data)
        

    # using recursion
    def inorder(self):
        result=[]
        self.rinorder(self.root, result)
        return result
    
    # recursive function 
    def rinorder(self, root, result):
        if root:
            self.rinorder(root.left, result)
            result.append(root.item)
            self.rinorder(root.right, result)
        
    
    # using recursion
    def preorder(self):
        result=[]
        self.rpreorder(self.root, result)
        return result
        
    # recursive function 
    def rpreorder(self, root, result):
        if root:
            result.append(root.item)
            self.rpreorder(root.left, result)
            self.rpreorder(root.right, result)
        
    
    # using recursion
    def postorder(self):
        result=[]
        self.rpostorder(self.root, result)
        return result
        
    # recursive function 
    def rpostorder(self, root, result):
        if root:
            self.rpostorder(root.left, result)
            self.rpostorder(root.right, result)
            result.append(root.item)

    
    def minValue(self, root):
        current = root
        while(current.left is not None):
            current = current.left
        return current.item
        
    def maxValue(self, root):
        current = root 
        while(current.right is not None):
            current = current.right
        return current.item
    
    # using recursion 
    def delete(self, data):
        self.root=self.rdelete(self.root, data)

    # the recursion function 
    def rdelete(self, root, data):
        if root is None:
            return root
        
        if data < root.item:
            root.left=self.rdelete(root.left, data)
        elif data > root.item:
            root.right=self.rdelete(root.right, data)
        else:
            # node has no child or only right child 
            if root.left is None:
                return root.right
            
            # Node has only left child
            elif root.right is None:
                return root.left
            
            # node has both children so find the minimum value in the right subtree and replace it with the root's value
            root.item=self.minValue(root.right)
            # Delete the minimum value of the right subtree
            root.right=self.rdelete(root.right, root.item)
        return root
    
    def size(self):
       return len (self.inorder())



bst= BST()


print('1. for insert element')
print("2. for search element")
print('3. for display elements in preorder')
print('4. for display elements in inorder')
print('5. for display elements in postorder')
print('6. for delete Node')
print('7. for get the number of nodes')
print("0. for exit")

while(True):
    ch=int(input("\nEnter your choice: "))
    match(ch):
        case 1:
            data= eval(input("Enter the data: "))
            bst.insert(data)
        case 2:
            data= eval(input("Enter the data: "))
            node=bst.search(data)
            if node != None:
                print('Element found')
            else:
                print("Element not found")
        case 3:
            result=bst.preorder()
            print(result)
        case 4:
            result=bst.inorder()
            print(result)
        case 5:
            result=bst.postorder()
            print(result)
        case 6:
            data= eval(input("Enter the data to be delete: "))
            bst.delete(data)
            print("Data deleted..")
        case 7:
            n = bst.size()
            print ("Number of Nodes : ", n)

        case 0:
            print('Thank You!')
            quit(0)


            
            

