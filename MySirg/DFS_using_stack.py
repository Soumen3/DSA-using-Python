from collections import defaultdict
edges = [[0,1],[0,2],[1,3],[3,5],[5,4],[4,3]]

graph=defaultdict(list)

for u,v in edges:
    graph[u].append(v)
    graph[v].append(u)

print(graph)

def dfs(start, graph):
    visited=set()
    stack=[]
    stack.append(start)
    while stack:
        current=stack.pop()
        if current not in visited:
            print(current, end=" ")
            visited.add(current)
            for i in graph[current]:
                stack.append(i)


dfs(0,graph)