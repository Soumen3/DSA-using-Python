class Node:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        self.height = 1

class HeightBalancedTree:
    def __init__(self):
        self.root = None

    def get_height(self, node):
        if not node:
            return 0
        return node.height    


    def _balance(self, node, val):
        balance_factor = self.get_height(node.left) - self.get_height(node.right)
        
        if balance_factor > 1:
            if val < node.left.val:
                return self._rotate_right(node)
            else:
                node.left = self._rotate_left(node.left)
                return self._rotate_right(node)
        elif balance_factor < -1:
            if val > node.right.val:
                return self._rotate_left(node)
            else:
                node.right = self._rotate_right(node.right)
                return self._rotate_left(node)


    def _rotate_right(self,node):
        new_root=node.left
        node.left=new_root.right
        new_root.right=node
        node.height=1+max(self.get_height(node.left),self.get_height(node.right))
        new_root.height=1+max(self.get_height(new_root.left),self.get_height(new_root.right))
        return new_root
    
    def _rotate_left(self, node):
        new_root=node.right
        node.right=new_root.left
        new_root.left=node
        node.height=1+max(self.get_height(node.left),self.get_height(node.right))
        new_root.height=1+max(self.get_height(new_root.left),self.get_height(new_root.right))
        return new_root
    
    def insert(self, val):
        self.root = self._insert(self.root, val)

        
    def _insert(self, node, val):
        if not node:
            return Node(val)
        
        if val < node.val:
            node.left = self._insert(node.left, val)
        else:
            node.right = self._insert(node.right, val)

        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))

        balance = self.get_height(node.left) - self.get_height(node.right)

        if balance > 1 or balance < -1:
            return self._balance(node, val)

        return node

    def preorder(self, node):
        if node:
            print(node.val, end=' ')
            self.preorder(node.left)
            self.preorder(node.right)


tree=HeightBalancedTree()

tree.insert(10)
tree.insert(20)
tree.insert(30)
tree.insert(40)
tree.insert(50)
tree.insert(25)
tree.insert(70)
tree.insert(60)
tree.insert(80)

tree.preorder(tree.root)