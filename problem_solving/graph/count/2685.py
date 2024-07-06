from collections import defaultdict

class Solution:
    def is_complete(self, graph, start, visited):
        q = [start]
        last_pop = None
        while len(q):
            last_pop = q.pop(0)
            for x in graph[last_pop]:
                if not x in visited:
                    q.append(x)
                    visited.add(x)
        return True if start == last_pop else False

    def countCompleteComponents(self,edges):
        graph, visited = defaultdict(set), set()
        count = 0
        def add_adjacency(graph, v1, v2):
            graph[v1].add(v2)
            graph[v2].add(v1)

        for (x, y) in edges:
            add_adjacency(graph, x, y)
        print(graph)

        for vrtx in graph:
            if vrtx in visited: continue
            if self.is_complete(graph, vrtx, visited):
                print(vrtx)
                count += 1

        return count

# print(Solution().countCompleteComponents([[0,1],[0,2],[1,2],[3,4]]))
print(Solution().countCompleteComponents( [[0,1],[0,2],[1,2],[3,4],[3,5]]))

