
from collections import defaultdict

def add_adjacency(graph, v1, v2):
    graph[v1].add(v2)
    graph[v2].add(v1)
    
graph = defaultdict(set) 
add_adjacency(graph, 1,2)
graph[3] = set()
add_adjacency(graph, 4,6)
add_adjacency(graph, 5,6)
add_adjacency(graph, 6,7)
add_adjacency(graph, 6,8)
def count(graph):

   print(graph)
   visited = set()
   count = 0
   largest = 0
   for vrtx in graph:
       if vrtx in visited: continue
       visited.add(vrtx)
       q = [vrtx]
       res = None
       size = 1
       while len(q):
           v = q.pop(0)
           res = v
           for x in list(graph[v]):
               if x in visited: continue
               visited.add(x)
               q.append(x) 
               size += 1
       print(size)
       largest = max(size, largest or size)
       count += 1
       print("end", res)
   return count, largest

print(count(graph))
print(count({
    0: [8,1,5],
    1: [0],
    5: [0, 8],
    8: [0,5],
    2: [3,4],
    3: [2,4],
    4: [3,2]
    }))
   

