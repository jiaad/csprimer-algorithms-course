from collections import defaultdict
from graph import Graph
import time


def make_graph():
    key_variations = defaultdict(list)
    graph = Graph()
    visited = set()
    with open("./words.txt") as f:
        while data := f.readline().strip().lower():
            if data in visited: continue
            visited.add(data)
            for j in range(len(data)):
                res = "".join("?" if k == j else x for k, x in enumerate(data))
                key_variations[res].append("".join(data))
                graph.add_vertex(data)

    for x in key_variations:
        i = 0
        keys = key_variations[x]
        while i < len(keys):
            j = i + 1
            while j < len(keys):
                graph.add_edge(keys[i], keys[j])
                j += 1
            i += 1
    return graph

def ladder_bfs(start, end, graph):
    q = [(start, [start], 0)]
    visited = set()
    while len(q):
        vrtx, path, depth = q.pop(0)
        if vrtx == end:
            return path, depth
        for x in graph.neighbors(vrtx):
            if x not in visited:
                visited.add(x)
                q.append((x, path + [x], depth + 1))
    return None

        
if __name__ == "__main__":
    ladder_graph = make_graph()
    print(ladder_bfs("hey", "sty", ladder_graph))
    print(ladder_bfs("aloof", "coins", ladder_graph))
    print(ladder_bfs("ring", "nice", ladder_graph))
    print(ladder_bfs("pig", "pit", ladder_graph))
    print(ladder_bfs("aloof", "piggy", ladder_graph))
    print(ladder_bfs("hey", "say", ladder_graph))

