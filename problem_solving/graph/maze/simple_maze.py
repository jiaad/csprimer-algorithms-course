maze = [
    [0,0,0,1,1,1,0],
    [0,0,1,1,0,0,0],
    [0,0,1,0,0,0,0],
    [0,0,1,1,0,0,0],
    [0,0,0,1,0,0,0],
    [0,0,0,1,1,0,0],
    [0,0,0,0,1,0,0],
    [0,0,0,0,1,1,0],
    [0,0,0,0,0,1,0],
    [0,0,0,0,0,1,0],
]


# nor finished
def bfs(mz, row, col):
    q, res, visited = [(row, col, [(row, col)])], [], set()
    visited.add(str(row) + "," + str(col))
    while len(q):
        y, x, path = q.pop(0)
        res.append((y, x))
        print(path)
        for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            dy, dx = dy + y, dx + x
            rowInbound = dy >= 0 and dy < len(mz)
            colInbound = dx >= 0 and dx < len(mz[0])
            if not rowInbound or not colInbound: continue
            if mz[dy][dx] != 1: continue
            key = str(dy) + "," + str(dx)
            if key in visited: continue
            visited.add(key)
            print("--")
            q.append((dy, dx, path + [dx, dy]))
    return res

print(bfs(maze, 0, 4))

