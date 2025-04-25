"""     Graph implementation using adjacency matrix     """

from QueueUsingSLL import Queue
from StackUsingList import Stack

class Graph:
    def __init__(self, vertices):
        self.vertex_count=vertices
        self.adj_matrix=[[0]*vertices for _ in range(vertices)]

    def add_edge(self, u,v, weight=1):
        if 0 <= u < self.vertex_count and 0 <= v < self.vertex_count :
            self.adj_matrix[u][v] = weight
            # Since it is undirected graph so we need to make symmetric
            self.adj_matrix[v][u]=weight
        else:
            print("Vertex not valid")
    
    def remove_edge(self, u,v):
        if 0<=u<self.vertex_count and 0<=v<self.vertex_count:
            self.adj_matrix[u][v]=0
            self.adj_matrix[v][u]=0
        else:
            print("Invalid Vertex")
    
    def has_edge(self, u,v):
        if 0<=u<self.vertex_count and 0<=v<self.vertex_count:
            return self.adj_matrix[u][v]!=0
        else:
            raise ValueError('Both the vertices must be present')
    
    def print_adj_matrix(self):
        print ("Adjancency Matrix: ")
        for i in self.adj_matrix:
            # print ([j for j in self.adj_matrix[i]])
            print(" ".join(map(str, i)))


    def BFS(self, source):
        if 0 <= source < self.vertex_count:
            bfsResult=[]
            queue=Queue()
            visited = [False] * self.vertex_count
            queue.enqueue(source)
            visited[source] = True
            while not queue.is_empty():
                nodeData = queue.dequeue()
                bfsResult.append(nodeData)
                neighbours=[vertex for vertex in range(self.vertex_count) if self.adj_matrix[nodeData][vertex]!=0]
                for neighbour in neighbours:
                    if not visited[neighbour]:
                        queue.enqueue(neighbour)
                        visited[neighbour] = True

            return bfsResult   
         
        else:
            raise ValueError ("Enter a valid vertex!")

    def DFS(self, source):
        if 0 <= source < self.vertex_count:
            dfsResult=[]
            stack=Stack()
            visited = [False] * self.vertex_count
            stack.push(source)
            visited[source] = True
            while not stack.is_empty():
                nodeData = stack.pop()
                dfsResult.append(nodeData)
                neighbours=[vertex for vertex in range(self.vertex_count) if self.adj_matrix[nodeData][vertex]!=0]
                for neighbour in neighbours:
                    if not visited[neighbour]:
                        stack.push(neighbour)
                        visited[neighbour]=True
            
            return dfsResult

        else:
            raise ValueError("Enter a valid vertex!")
            

g = Graph(5)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 4)
g.add_edge(2, 4)
g.add_edge(2, 3)
g.add_edge(2, 0)
g.add_edge(3, 4)

g.print_adj_matrix()

bfs=g.BFS(0)
print("The Breadth First Traversal is:")
for e in bfs:
    print(f'V{e}',end=' ')
print()

dfs=g.DFS(0)
print("The Depth First Traversal is:")
for e in dfs:
    print(f'V{e}',end=' ')