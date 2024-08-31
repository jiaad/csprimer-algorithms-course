
def is_valid_state(board, state):
  if len(state) == 64:
      return True

def get_candidates():
    directions = [
        #up
        (-2, -1), (-2, 1),
        (-1, -2), (-1, +2),

        #down
        (1, -2), (1, 2),
        (2, -1), (2, 1)
    ]
    return directions

def search(row, col, state, solutions, board):
    if board[row][col] == 1: return
    board[row][col] = 1

    if is_valid_state(board, state):
        solutions.append(state.copy())
        print("valid")
        return True


    for (r, c) in get_candidates():
        r,c = row + r, col + c
        rowBound = r >= 0 and r < len(board)
        colBound = c >= 0 and c < len(board[0])
        if rowBound and colBound:
            state.append((r, c))
            res = search(r, c, state, solutions, board)
            if res == True:
              print("found")
              for x in board:
                print(x)
              return board, solutions

            #state.remove((r, c))
    if len(state) != 64:
        board[row][col] = 0
        state.remove((row, col))

def solve():
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
    solutions = []
    state = [(0, 0)]
    search(0, 0, state, solutions, board)
    return solutions

if __name__ == "__main__":
  print("== start ==")
  print(solve())
