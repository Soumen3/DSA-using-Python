class Node:
    def __init__(self, item=None, left=None, right=None):
        self.item=item
        self.left=left
        self.right=right


class BST:
    def __init__(self):
        self.root=None
    
    def is_empty(self):
        return self.root==None
    
    def insert(self, data):
        newNode=Node(data)
        if self.is_empty():
            self.root=newNode
        else:
            temp=self.root
            while temp != None:
                if temp.item > data:
                    if temp.left == None:
                        temp.left = newNode
                        break
                    temp=temp.left
                elif temp.item < data:
                    if temp.right == None:
                        temp.right= newNode
                        break
                    temp= temp.right
        print(f'{data} is inserted in the tree')

    def search(self, data):
        temp= self.root
        while temp!=None:
            if data > temp.item:
                temp=temp.right
            elif data < temp.item:
                temp=temp.left
            else:
                return temp
        else:
            return None
        
    def preorder(self, root=None):
        temp=root
        
        if temp == None:
            return
        print(temp.item,end=' ')
        self.preorder(temp.left)
        self.preorder(temp.right)


    def inorder(self, root=None):
        temp=root
        
        if temp == None:
            return
        self.inorder(temp.left)
        print(temp.item,end=' ')
        self.inorder(temp.right)


    def postorder(self, root=None):
        temp=root
        
        if temp == None:
            return
        self.postorder(temp.left)
        self.postorder(temp.right)
        print(temp.item,end=' ')

            
    # def deleteNode(self, data):
    #     deleteNode=self.searchDeletenode(self.root, data)
    #     if deleteNode == None:
    #         raise IndexError("The node is not found!")
    #     else:
    #         if deleteNode.item > data:
    #             deleteNode.left = None
            

    # def searchDeletenode(root, data):
    #     if root == None:
    #         return None
    #     temp= root
    #     preTemp=root
    #     while temp!=None:
    #         if data > temp.item:
    #             preTemp=temp
    #             temp=temp.right
    #         elif data < temp.item:
    #             preTemp=temp
    #             temp=temp.left
    #         else:
    #             return preTemp
    #     else:
    #         return None
                

        


bst= BST()

bst.insert(50)
bst.insert(30)
bst.insert(10)
bst.insert(40)
bst.insert(35)
bst.insert(80)
bst.insert(70)
bst.insert(60)
bst.insert(55)
bst.insert(67)
bst.insert(75)
bst.insert(100)
bst.insert(90)

bst.inorder(bst.root)


# print('1. for insert element')
# print("2. for search element")
# print('3. for display elements in preorder')
# print('4. for display elements in inorder')
# print('5. for display elements in postorder')
# print("0. for exit")

# while(True):
#     ch=int(input("\nEnter your choice: "))
#     match(ch):
#         case 1:
#             data= eval(input("Enter the data: "))
#             bst.insert(data)
#         case 2:
#             data= eval(input("Enter the data: "))
#             node=bst.search(data)
#             if node != None:
#                 print('Element found')
#             else:
#                 print("Element not found")
#         case 3:
#             bst.preorder(bst.root)
#         case 4:
#             bst.inorder(bst.root)
#         case 5:
#             bst.postorder(bst.root)
#         case 0:
#             print('Thank You!')
#             quit(0)


            
            

