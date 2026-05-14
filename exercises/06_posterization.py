from PIL import Image

INPUT_FILE = 'snake.png'
OUTPUT_FILE = 'posterized_snake.png'

DARK_SHADOWS = (120, 41, 15) # Brandy
MIDTONES = (255, 125, 0) # Harvest Orange
HIGHLIGHTS = (255, 236, 209) # Papaya Whip

with Image.open(INPUT_FILE) as in_img:
    in_img = in_img.convert('RGB')
    size = in_img.size
    in_stream = in_img.get_flattened_data()

out_stream = []
for (red, green, blue) in in_stream:
    average = int(0.299 * red +0.587 * green +0.114 * blue)
    if average < 50:
        out_stream.append(DARK_SHADOWS)
    elif average < 130:
        out_stream.append(MIDTONES)
    else:
        out_stream.append(HIGHLIGHTS)

out_img = Image.new('RGB', size)
out_img.putdata(out_stream)
out_img.save(OUTPUT_FILE)

print('Done!')
