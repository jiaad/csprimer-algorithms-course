
def is_valid_state(state, n):
    return len(state) == n

def not_inbound(r, c, h, w):
    rowInbound = r >= 0 and r < h
    colInbound = c >= 0 and c <  w
    return not rowInbound or not colInbound

def can_be_placed(board, row, col):
    # if board[row][col] == 1: return False
    rcol, lcol = col, col
    while row >= 0:
        if board[row][col] == 1: return False
        if rcol < len(board[0]):
            if board[row][rcol] == 1:
                # print("this is [row, rcol, value]:", row, rcol, board[row][rcol])
                return False
            rcol += 1
        if lcol >= 0:
            if board[row][lcol] == 1:
                # print("this i1 :", row, lcol, board[row][lcol])
                return False
            lcol -= 1
        row -= 1
    return True

def get_candidates():
    directions = [
        # four directions
        (0, 1), (0, -1),
        (-1, 0), (1, 0),
        # diagonal
        (1, 1), (-1, 1),
        (1, -1), (-1, -1)
    ]
    rax = []
    # for r, c in directions:
    #     r, c = row - r, col - c
    #     if not_inbound(r, c):
    #         continue
    #     rax.append((r, c))
    return [0,1,2,3,4,5,6,7, 8]
    #return [(-1, 0), (1, 0), (0, -1), (0, 1)]

def found(arr, elem):
    row, col = elem
    for (r, c) in arr:
        if r == row: return True
        if c == col: return True
    return False

def search(state, solutions, n, board, r, c):
    if is_valid_state(state, n):
        solutions.append(state.copy())
        return True

    if r >= n:
        return

    if board[r][c] == 1:
        print("id one")
        return

    for col in get_candidates():
        if not_inbound(r, col, n, n): continue
        if can_be_placed(board, r, col):
            state.append((r, col))
            board[r][col] = 1
            res = search(state, solutions, n, board, r + 1, col)
            if res:
                print("res", res, state)
            board[r][col] = 0
            if (r,col) in state:
                state.remove((r, col))



def solve(n):
    solutions = []
    state = []
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
    return search(state, solutions, n, board, 0, 0)
    #return solutions

directions = [
    # four directions
    (0, 1), (0, -1),
    (-1, 0), (1, 0),
    # diagonal
    (1, 1), (-1, 1),
    (1, -1), (-1, -1)
]


if __name__ == "__main__":
    sol = solve(8)
    print("\n\n\n")
    # print(sol)
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
    # for x in sol:
    #     r, c = x
    #     board[r][c] = 1
    # for x in board:
    #     print(x)
    #
    #
    # print("\n\n\n")
    #
# [(0, 3), (1, 5), (2, 7), (3, 2), (4, 0), (5, 6), (6, 4),(7, 1)]

# [(0, 0), (1, 5), (2, 3), (3, 1), (4, 7), (5, 4), (6, 2)]

    board2 = [
[1, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 1, 0, 0],
[0, 0, 0, 1, 0, 0, 0, 0],
[0, 1, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 1],
[0, 0, 0, 0, 1, 0, 0, 0],
[0, 0, 1, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0],
    ]
    #

    print(can_be_placed(board2, 7, 6))
