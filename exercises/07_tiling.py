from PIL import Image

INPUT_FILE1 = 'puppy.png'
INPUT_FILE2 = 'snake.png'
INPUT_FILE3 = 'tree.png'
INPUT_FILE4 = 'woman.png'
OUTPUT_FILE = 'tile2x2.png'

def place(out_grid, file_name, position):
    with Image.open(file_name) as in_img:
        in_img = in_img.convert('RGB')
        width, height = in_img.size
        in_grid = in_img.load()
    out_x, out_y = position
    for y in range(height):
        for x in range(width):
            out_grid[out_x + x, out_y + y] = in_grid[x, y]

with Image.open(INPUT_FILE1) as in_img:
    width, height = in_img.size

out_img = Image.new('RGB', (width * 2, height * 2))
out_grid = out_img.load()
place(out_grid, INPUT_FILE1, (0, 0))
place(out_grid, INPUT_FILE2, (width, 0))
place(out_grid, INPUT_FILE3, (0, height))
place(out_grid, INPUT_FILE4, (width, height))
out_img.save(OUTPUT_FILE)

print('Done!')
