# 0 = empty
# 1 = occipied
# 3 = queen



def four_dir(board, row, col):
    coordinates = []
    def not_inbound(r, c):
        rowInbound = r >= 0 and r < len(board)
        colInbound = c >= 0 and c < len(board[0])
        return not rowInbound or not colInbound

    def top(r, c):
        if not_inbound(r, c): return
        if board[r][c] == 1: return
        if board[r][c] != 2:
            board[r][c] = 1
            coordinates.append((r, c))
        top(r - 1, c)
    def bottom(r, c):
        if not_inbound(r, c): return
        if board[r][c] == 1: return
        if board[r][c] != 2:
            board[r][c] = 1
            coordinates.append((r, c))
        bottom(r + 1, c)
    def left(r, c):
        if not_inbound(r, c): return
        if board[r][c] == 1: return
        if board[r][c] != 2:
            board[r][c] = 1
            coordinates.append((r, c))
        left(r, c - 1)
    def right(r, c):
        if not_inbound(r, c): return
        if board[r][c] == 1: return
        if board[r][c] != 2:
            board[r][c] = 1
            coordinates.append((r, c))
        right(r, c + 1)

    top(row, col)
    bottom(row, col)
    left(row, col)
    right(row, col)
    return coordinates

def four_diag(board, row, col):
    coordinates = []
    def not_inbound(r, c):
        rowInbound = r >= 0 and r < len(board)
        colInbound = c >= 0 and c < len(board[0])
        return not rowInbound or not colInbound

    def top_left(r, c):
        if not_inbound(r, c): return
        if board[r][c] == 1: return
        if board[r][c] != 2:
            board[r][c] = 1
            coordinates.append((r, c))
        top_left(r - 1, c - 1)

    def top_right(r, c):
        if not_inbound(r, c): return
        if board[r][c] == 1: return
        if board[r][c] != 2:
            board[r][c] = 1
            coordinates.append((r, c))
        top_right(r - 1, c + 1)

    def bottom_left(r, c):
        if not_inbound(r, c): return
        if board[r][c] == 1: return
        if board[r][c] != 2:
            board[r][c] = 1
            coordinates.append((r, c))
        bottom_left(r + 1,  c - 1)

    def bottom_right(r, c):
        if not_inbound(r, c): return
        if board[r][c] == 1: return
        if board[r][c] != 2:
            board[r][c] = 1
            coordinates.append((r, c))
        bottom_right(r + 1, c + 1)

    top_left(row, col)
    bottom_left(row, col)
    top_right(row, col)
    bottom_right(row, col)
    return coordinates


def position_mark(board, row, col):
    board = [
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
    ]
    board[row][col] = 2
    coordinates = []
    four = four_dir(board, row, col)
    diag = four_diag(board, row, col)
    coordinates.extend(four)
    coordinates.extend(diag)
    for x in board:
        print(x)
    print(coordinates)
    state = set(coordinates)
    print(state)


if __name__ == "__main__":
    position_mark(board, 0, 0)
