from PIL import Image

INPUT_IMAGE = 'tree.png'
OUTPUT_IMAGE = 'shrank_tree.png'

with Image.open(INPUT_IMAGE) as in_img:
    in_img = in_img.convert('RGB')
    in_grid = in_img.load()
    width, height = in_img.size

new_width = width // 10
new_height = height // 10

out_img = Image.new('RGB', (new_width, new_height))
out_grid = out_img.load()
for y in range(new_height):
    for x in range(new_width):
        out_grid[x, y] = in_grid[x * 10, y * 10]
out_img.save(OUTPUT_IMAGE)

print('Done!')
