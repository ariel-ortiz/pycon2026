from PIL import Image

INPUT_FILE = 'puppy.png'
OUTPUT_FILE = 'negative_puppy.png'

with Image.open(INPUT_FILE) as in_img:
    in_img = in_img.convert('RGB')
    in_stream = in_img.get_flattened_data()
    size = in_img.size

out_stream = []
for (red, green, blue) in in_stream:
    out_stream.append((255 - red, 255 - green, 255 - blue))

out_img = Image.new('RGB', size)
out_img.putdata(out_stream)
out_img.save(OUTPUT_FILE)

print('Done!')
