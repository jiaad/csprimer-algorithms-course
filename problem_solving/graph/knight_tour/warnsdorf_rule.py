
def knight_tour(start_r, start_c):
    directions = [
        #up
        (-2, -1), (-2, 1),
        (-1, -2), (-1, +2),

        #down
        (1, -2), (1, 2),
        (2, -1), (2, 1)
    ]
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
    def itter(chess, row, col, visited, directions, path, step):
        # mean already done
        if chess[row][col] == 1: return "ONE_DONE"

        if chess[row][col] == 0:
            chess[row][col] = 1
            steps[row][col] = step

        if len(path) >= 64:
            print("*"* 50)
            print("\n\n\n\n")
            print_chess(chess)
            print("\n")
            print_chess(steps)
            print(path, len(path), step)
            print("\n\n\n\n")
            print("*"* 50)
            return True

        for (r, c) in directions:
            r, c = row + r, col + c
            if (r, c) in visited: continue
            rowInbound = r >= 0 and r < len(chess)
            colInbound = c >= 0 and c < len(chess[0])
            if not rowInbound or not colInbound:
                continue
            visited.add((r,c))
            res = itter(chess, r, c, visited, directions, path + [(r, c)], step + 1)
            if res == True:
                print("==============", res)
                print_chess(chess)
                return chess, path, steps

        if len(path) != 64:
            chess[row][col] = 0
            visited.discard((row, col))
            steps[row][col] = 0

        return False
    return itter(chess, start_r, start_c, visited, directions, [(0, 0)], 1)

def print_chess(chess):
    for x in chess: print(x)



if __name__ == "__main__":
    chess, path, steps = knight_tour(0, 0)

    print_chess(chess)
    print(path, len(path))
    print_chess(steps)
