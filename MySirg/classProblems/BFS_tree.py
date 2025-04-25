class Node:
    def __init__(self, val, left=None, right=None):
        self.val=val
        self.left=left
        self.right=right

class BinaryTree:
    def __init__(self, root=None):
        self.root=Node(root)

    def addNode(self, val):
        if not self.root:
            self.root=Node(val)
        else:
            self._addNode(self.root, val)

    def _addNode(self, node, val):
        if val<node.val:
            if node.left:
                self._addNode(node.left, val)
            else:
                node.left=Node(val)
        else:
            if node.right:
                self._addNode(node.right, val)
            else:
                node.right=Node(val)

    def bfs(self):
        if not self.root:
            return None
        else:
            self._bfs(self.root)

    def _bfs(self, node):
        queue=[]
        queue.append(node)
        while queue:
            node=queue.pop(0)
            print(node.val, end=" ")
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    def dfs(self):
        if not self.root:
            return None
        else:
            self._dfs(self.root)

    def _dfs(self, node):
        if node:
            print(node.val, end=" ")
            self._dfs(node.left)
            self._dfs(node.right)
        
bt=BinaryTree(5)
bt.addNode(3)
bt.addNode(7)
bt.addNode(2)
bt.addNode(4)
bt.addNode(6)
bt.addNode(8)
bt.bfs()
print()
bt.dfs()
print()




