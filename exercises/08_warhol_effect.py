from PIL import Image

INPUT_FILE = 'woman.png'
OUTPUT_FILE = 'warhol_woman.png'

def place(out_grid, in_grid, size, position):
    width, height = size
    out_x, out_y = position
    for y in range(height):
        for x in range(width):
            out_grid[out_x + x, out_y + y] = in_grid[x, y]

def posterize(in_grid, size, dark_shadows, midtones, highlights):
    width, height = size
    out_img = Image.new('RGB', size)
    out_grid = out_img.load()
    for y in range(height):
        for x in range(width):
            red, green, blue = in_grid[x, y]
            avg = (red + green + blue) // 3
            if avg < 50:
                out_grid[x, y] = dark_shadows
            elif avg < 130:
                out_grid[x, y] = midtones
            else:
                out_grid[x, y] = highlights
    return out_grid

with Image.open(INPUT_FILE) as in_img:
    in_img = in_img.convert('RGB')
    size = in_img.size
    in_grid = in_img.load()

width, height = size

out_img = Image.new('RGB', (width * 2, height * 2))
out_grid = out_img.load()
place(
    out_grid,
    posterize(
        in_grid,
        size,
        (0x78, 0x29, 0x0f),
        (0xff, 0x7d, 0x00),
        (0xff, 0xec, 0xd1)),
    size,
    (0, 0))
place(
    out_grid,
    posterize(
        in_grid,
        size,
        (0x1d, 0x35, 0x57),
        (0xa6, 0x8a, 0x64),
        (0xf2, 0xe9, 0xe4)),
    size,
    (width, 0))
place(
    out_grid,
    posterize(
        in_grid,
        size,
        (0x1d, 0x35, 0x57),
        (0x00, 0xaf, 0xb9),
        (0xf1, 0xfa, 0xee)),
    size,
    (0, height))
place(
    out_grid,
    posterize(
        in_grid,
        size,
        (0x8e, 0x00, 0x80),
        (0xb8, 0x92, 0xff),
        (0xff, 0xeF, 0xff)),
    size,
    (width, height))
out_img.save(OUTPUT_FILE)

print('Done!')
