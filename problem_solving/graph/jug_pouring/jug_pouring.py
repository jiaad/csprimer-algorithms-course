from collections import deque

def jug_pour(left, right, ans):
    #q = [(0,0, ["start"])]
    q = deque()
    q.append((0,0, ["start"]))

    visited = set()
    while q:
        state = q.popleft()
        left_size, right_size, ops = state

        if left_size < 0 or left_size > left: continue
        if right_size < 0 or right_size > right: continue
        if right_size == ans or left_size == ans: 
            print("won: ", left_size, right_size)
            print(*ops, sep="\n")
            break

        steps = [
            # fill right
            (left_size, right, "fill right"),
            # fill left
            (left, right_size, "fill left"),
            # empty right
            (left_size, 0, "empty right"),
            # empty left
            (0, right_size, "empty left"),
            # transfer left to right
            (max(0, left_size + right_size - 5), min(right, left_size + right_size), "left to right"),
            # transfer right to left
            (min(left, left_size + right_size ), max(0, right_size + left_size - left), "right to left")
        ]
        for l,r,path in steps:
            if not (l,r) in visited:
                visited.add((l,r))
                q.append((l, r, ops + [path]))
    return None


if __name__ == "__main__":
    jug_pour(3, 5, 4)
