
board = [
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
]
directions = [
    #up
    (-2, -1), (-2, 1),
    (-1, -2), (-1, +2),

    #down
    (1, -2), (1, 2),
    (2, -1), (2, 1)
]

def find_next(chess, row, col, visited):
    global directions
    res = []
    for (y, x) in directions:
        y, x = row + y, col + x
        rowInbound = y >= 0 and y < len(chess)
        colInbound = x >= 0 and x < len(chess[0])
        if not rowInbound or not colInbound: continue
        if (y,x) in visited: continue
        res.append((y, x))
    return res

def get_optimal_move(chess, row, col, visited):
    moves = find_next(chess, row, col, visited)
    moves.sort(key=lambda c: len(find_next(chess, c[0], c[1], visited)))
    return moves

print(get_optimal_move(board, 0, 6, set()))




def knight_tour(start_r, start_c):
    steps = [
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
    ]
    chess = [
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
    ]
    visited = set()
    visited.add((0,0))
    def itter(chess, row, col, visited, path, step):
        if chess[row][col] == 1: return False

        if chess[row][col] == 0:
            chess[row][col] = 1
            steps[row][col] = step

        if len(path) == 64:
            print("*"* 50)
            print("\n\n\n\n")
            print_chess(chess)
            print("\n")
            print_chess(steps)
            print(path, len(path), step)
            print("\n\n\n\n")
            print("*"* 50)
            return path

        for (r, c) in get_optimal_move(chess, row, col, visited):
            visited.add((r,c))
            res = itter(chess, r, c, visited, path + [(r, c)], step + 1)
            if res:
                print("==============", res)
                print("==============", len(path), path)
                print_chess(chess)
                return res
            # visited.discard((r, c))  # Unmark the square when backtracking
            # chess[r][c] = 0
            # steps[r][c] = 0

        # if len(path) != 64:
        #     chess[row][col] = 0
        #     visited.discard((row, col))
        #     steps[row][col] = 0

        return False

    return itter(chess, start_r, start_c, visited, [(0, 0)], 1)

def print_chess(chess):
    for x in chess: print(x)



if __name__ == "__main__":
    res = knight_tour(0, 0)
    print("res:::", res)
    # if res != False and res != True:
    #     chess, path, steps =  res
    #
    #     print_chess(chess)
    #     print(path, len(path))
    #     print_chess(steps)
