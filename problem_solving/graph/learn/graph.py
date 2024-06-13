class Graph:
    def __init__(self):
        self.adjacency = {}
 
    # a node is a vertex
    def add_vertex(self, vrtx_name):
        if not self.adjacency.get(vrtx_name):
            self.adjacency[vrtx_name] = []

    def add_edge(self, key1, key2):
        if key1 in self.adjacency:
            self.adjacency[key1].append(key2)
        if key2 in self.adjacency:
            self.adjacency[key2].append(key1)
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


if __name__ == "__main__":
    gr = Graph()
    gr.add_vertex("paris")
    gr.add_vertex("london")
    gr.add_vertex("milan")
    gr.add_vertex("tokyo")
    gr.add_vertex("kyoto")
    gr.add_edge("paris", "milan")
    gr.add_edge("london", "milan")

    graph_dfs = Graph()
    graph_dfs.add_vertex("A")
    graph_dfs.add_vertex("B")
    graph_dfs.add_vertex("C")
    graph_dfs.add_vertex("D")
    graph_dfs.add_vertex("E")
    graph_dfs.add_vertex("F")

    graph_dfs.add_edge("A", "B")
    graph_dfs.add_edge("A", "C")
    graph_dfs.add_edge("B", "D")
    graph_dfs.add_edge("C", "E")
    graph_dfs.add_edge("D", "E")
    graph_dfs.add_edge("D", "F")
    graph_dfs.add_edge("E", "F")
    print(graph_dfs.adjacency)

    def travers_graph_dfs(graph):
        visited = set()
         
        keys = graph.adjacency
        def dfs(vrtx):
            if not len(vrtx): return
            print(vrtx, end="->")
            visited.add(vrtx)
            for vrtx in keys[vrtx]:
                if not vrtx in visited:
                    dfs(vrtx)

        dfs("A")
    travers_graph_dfs(graph_dfs)

