from collections import defaultdict
# edges = [[0,1],[0,2],[1,3],[3,5],[5,4],[4,3]]
edges = [[4,3],[1,4],[4,8],[1,7],[6,4],[4,2],[7,4],[4,0],[0,9],[5,4]]

graph=defaultdict(list)

for u,v in edges:
    graph[u].append(v)
    graph[v].append(u)

print(graph)

def dfs(graph, start, visited):
    if start not in visited:
        print(start, end=" ")
        visited.add(start)
        for neighbour in graph[start]:
            dfs(graph, neighbour, visited)

visited=set({})
dfs(graph, 5, visited)




# leetcode 1971


# from collections import defaultdict
# class Solution:
#     def dfs(self, graph, start, visited, destination):
#         if start not in visited:
#             if start==destination:
#                 return True
#             visited.add(start)
#             for neighbours in graph[start]:
#                 if self.dfs(graph,neighbours,visited,destination):
#                     return True

#     def validPath(self, n, edges, source, destination) :
#         if [source,destination] in edges or [destination,source] in edges:
#             return True
        
#         graph=defaultdict(list)

#         for u,v in edges:
#             graph[u].append(v)
#             graph[v].append(u)

#         print(graph)
#         visited=set()
#         return True if self.dfs(graph, source, visited, destination) else False

# obj=Solution()
    
# print(obj.validPath(10, [[4,3],[1,4],[4,8],[1,7],[6,4],[4,2],[7,4],[4,0],[0,9],[5,4]], 5, 9))