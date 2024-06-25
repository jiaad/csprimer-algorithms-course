from PIL import Image
import sys

def floodFill(image_path, sr, sc, color):
    image = Image.open(image_path)
    old_color = image.getpixel((sr, sc))
    sys.setrecursionlimit(image.height * image.width)
    dfs(image, sr, sc, old_color, color)
    image.show()

def dfs(image, sr, sc, old_color, new_color):
    row_inbound = 0 <= sr < image.height
    col_inbound = 0 <= sc < image.width
    if not row_inbound or not col_inbound:
        return
    if image.getpixel((sr, sc)) != old_color:
        return
    if image.getpixel((sr, sc)) == new_color:
        return

    image.putpixel((sr, sc), new_color)
    dfs(image, sr - 1, sc, old_color, new_color)
    dfs(image, sr + 1, sc, old_color, new_color)
    dfs(image, sr, sc - 1, old_color, new_color)
    dfs(image, sr, sc + 1, old_color, new_color)
    return  image


# Example usage:
floodFill("./flood.png", 1, 1, (255, 99, 71, 255))
# print(floodFill([[1,1,1],[1,1,0],[1,0,1]], 1, 1, 10))

