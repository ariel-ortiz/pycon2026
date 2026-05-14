from PIL import Image

INPUT_FILE = 'woman.png'
OUTPUT_FILE = 'binarized_woman.png'

with Image.open(INPUT_FILE) as in_img:
    in_img = in_img.convert('RGB')
    in_stream = in_img.get_flattened_data()
    size = in_img.size

out_stream = []
for (_, green, _) in in_stream:
    out_stream.append(0 if green < 130 else 1)

out_img = Image.new('1', size)
out_img.putdata(out_stream)
out_img.save(OUTPUT_FILE)

print('Done!')
