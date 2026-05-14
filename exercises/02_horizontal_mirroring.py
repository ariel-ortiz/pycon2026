from PIL import Image

INPUT_IMAGE = 'tree.png'
OUTPUT_IMAGE = 'mirror_tree.png'

with Image.open(INPUT_IMAGE) as in_img:
    in_img = in_img.convert('RGB')
    size = in_img.size
    in_grid = in_img.load()

width, height = size
out_img = Image.new('RGB', size)
out_grid = out_img.load()
for y in range(height):
    for x in range(width):
        out_grid[x, y] = in_grid[(width - 1) - x, y]
out_img.save(OUTPUT_IMAGE)

print('Done!')
