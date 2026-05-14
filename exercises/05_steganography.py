from PIL import Image

INPUT_IMAGE = 'snake.png'
OUTPUT_IMAGE = 'secret.png'

with Image.open(INPUT_IMAGE) as in_img:
    in_img = in_img.convert('RGB')
    size = in_img.size
    in_stream = in_img.get_flattened_data()

out_stream = []
for (_, green, _) in in_stream:
    out_stream.append(green % 2)

out_img = Image.new('1', size)
out_img.putdata(out_stream)
out_img.save(OUTPUT_IMAGE)

print('Done!')
