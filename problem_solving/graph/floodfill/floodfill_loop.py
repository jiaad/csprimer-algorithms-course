from PIL import Image

def floodfill(image_path, row, col, color):
    image = Image.open(image_path)
    q = [[row, col]]
    visited = set()
    old_color = image.getpixel((row, col))
    print(old_color)
    # up
    # right
    #down
    # left
    while len(q):
        row, col = q.pop(0)
        rowInboud = row >= 0 and row < image.height
        colInboud = col >= 0 and col < image.width
        if not rowInboud or not colInboud: continue
        curr_coordinates = str(row) + "," + str(col)
        if curr_coordinates in visited: continue
        if old_color != image.getpixel((row, col)): continue
        visited.add(curr_coordinates)
        image.putpixel((row, col), color)
        q.append([row - 1, col])
        q.append([row + 1, col])
        q.append([row, col - 1])
        q.append([row, col + 1])
    image.show()
    return image


# print(floodfill([[1,1,1],[1,1,0],[1,0,1]], 1, 1, 2))
print(floodfill("./flood-big.jpg", 40, 40, 11))
