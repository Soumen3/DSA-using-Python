"""     Graph implementation using adjacency list     """

from QueueUsingSLL import Queue
from StackUsingList import Stack

class Graph:
    def __init__(self, vertices):
        self.vertex_count=vertices
        self.adj_list = {e:[] for e in range(vertices)}   # A dictionary to store graph


    def add_edge(self, u, v, weight=1):
        ''' Adds an edge between two vertices of the graph'''
        if 0 <= u < self.vertex_count and 0 <= v < self.vertex_count:
            self.adj_list[u].append((v,weight))                      # Adding a directed edge from u to v
            self.adj_list[v].append((u,weight))
        else:
            raise ValueError("The vertex must be present")

    def remove_edge(self, u,v):
        ''' Removes an edge between two vertices of the graph'''
        if 0 <= u < self.vertex_count and 0 <= v < self.vertex_count:
            try:
                self.adj_list[u]= [(vertex, weight) for vertex, weight in self.adj_list[u] if vertex!=v]
                self.adj_list[v]= [(vertex, weight) for vertex, weight in self.adj_list[v] if vertex!=u]
            except Exception:
                print(f"Edge not found")
        else:
            raise ValueError("The vertex must be present")
        
    def has_edge(self, u, v):
        if 0 <= u < self.vertex_count and 0 <= v < self.vertex_count:
            return any(vertex==v for vertex, e in self.adj_list[u])
        else:
            raise ValueError("The vertex must be present")
        
    def print_adj_list(self):
        ''' Prints the adjacency list representation of the graph '''
        # print(self.adj_list)
        for lst in self.adj_list:
            print(f'Vertex {lst}: {self.adj_list[lst]} ')
            # print(f'V{lst}: {['V'+str(e) for e in self.adj_list[lst]]} ')


    def BFS(self, source):
        if 0 <= source < self.vertex_count:
            bfsResult=[]
            queue=Queue()
            visited = [False] * self.vertex_count
            queue.enqueue(source)
            visited[source] = True
            while not queue.is_empty():
                node = queue.dequeue()
                bfsResult.append(node)
                neighbours=[ i for i in self.adj_list[node] ]
                print(neighbours)
                for neighbour in neighbours:
                    if not visited[neighbour[0]]:
                        queue.enqueue(neighbour[0])
                        visited[neighbour[0]] = True
            return bfsResult
        
        else:
            raise ValueError("Enter valid vertex!")
        

    def DFS(self, source):
        if 0 <= source < self.vertex_count:
            dfsResult=[]
            stack=Stack()
            visited = [False] * self.vertex_count
            stack.push(source)
            visited[source] = True
            while not stack.is_empty():
                node = stack.pop()
                dfsResult.append(node)
                neighbours=[i for i in self.adj_list[node]]
                for neighbour in neighbours:
                    if not visited[neighbour[0]]:
                        stack.push(neighbour[0])
                        visited[neighbour[0]]=True
            
            return dfsResult

        else:
            raise ValueError("Enter a valid vertex!")

        
        
# Driver code

g=Graph(5)
g.add_edge(0,1)
g.add_edge(0,2)
g.add_edge(1,4)
g.add_edge(2,4)
g.add_edge(2,3)
g.add_edge(4,3)

g.print_adj_list()

bfs=g.BFS(0)
print("The Breadth First Traversal is:")
for e in bfs:
    print(f'V{e}',end=' ')
print()

dfs=g.DFS(0)
print("The Depth First Traversal is:")
for e in dfs:
    print(f'V{e}',end=' ')