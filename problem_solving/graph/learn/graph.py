class Graph:
    def __init__(self):
        self.adjacency = {}
 
    # a node is a vertex
    def add_vertex(self, vrtx_name):
        if not self.adjacency.get(vrtx_name):
            self.adjacency[vrtx_name] = []

    def add_edge(self, key1, key2):
        def rec(key1, key2, depth):
            if key1 in self.adjacency:
                self.adjacency[key1].append(key2)
            #if depth == 0:
            #    rec(key2, key1, 1)
            if key2 in self.adjacency:
                self.adjacency[key2].append(key1)
        return rec(key1, key2, 0)
    def remove_edge(self, key1, key2):
        if key1 in self.adjacency:
            filtered = filter(lambda x: x != key2, self.adjacency[key1])
            self.adjacency[key1] = list(filtered) 
        if key2 in self.adjacency:
            filtered = filter(lambda x: x != key1, self.adjacency[key2])
            self.adjacency[key2] = list(filtered)
    def remove_vertex(self, vrtx):
        while len(self.adjacency):
            key = self.adjacency[vrtx].pop()
            self.remove_edge(vrtx, key)
        del self.adjacency[vrtx] 


    def neighbors(self, vrtx):
        keys = self.adjacency
        return keys.get(vrtx, []) 

    def dfs_rec(self, start_vrtx):
        visited, res = set(), []
        def dfs(vrtx):
            if not vrtx: return
            res.append(vrtx)
            visited.add(vrtx)
            
            for key in self.neighbors(vrtx):
                if not key in visited:
                    dfs(key)
            return res

        return dfs(start_vrtx)
        
    def dfs_itter(self, start_vrtx):
        visited, res, stack = set(), [], [start_vrtx]
        while len(stack):
            vertex = stack.pop()
            if vertex in visited: continue
            visited.add(vertex)
            res.append(vertex)
            for v in self.neighbors(vertex):
                stack.append(v)
        return res
        
    def bfs(self, start_vrtx):
        visited, res, q = set(), [], [start_vrtx]

        while len(q):
            vrtx = q.pop(0)
            if vrtx in visited: continue
            res.append(vrtx)
            visited.add(vrtx)
            for x in self.neighbors(vrtx):
                q.append(x)

        return res



if __name__ == "__main__":
    gr = Graph()
    gr.add_vertex("paris")
    gr.add_vertex("london")
    gr.add_vertex("milan")
    gr.add_vertex("tokyo")
    gr.add_vertex("kyoto")
    gr.add_edge("paris", "milan")
    gr.add_edge("london", "milan")

    graph = Graph()
    graph.add_vertex("A")
    graph.add_vertex("B")
    graph.add_vertex("C")
    graph.add_vertex("D")
    graph.add_vertex("E")
    graph.add_vertex("F")

    graph.add_edge("A", "B")
    graph.add_edge("A", "C")
    graph.add_edge("B", "D")
    graph.add_edge("C", "E")
    graph.add_edge("D", "E")
    graph.add_edge("D", "F")
    graph.add_edge("E", "F")
    print(graph.dfs_rec("A"))
    print(graph.dfs_itter("A"))
    print(graph.bfs("A"))


    iife = lambda fn: fn()
    @iife
    def p():
        print("hellllooooo")
