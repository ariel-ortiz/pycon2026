from PIL import Image

INPUT_FILE1 = 'woman.png'
INPUT_FILE2 = 'sunset.png'
OUTPUT_FILE = 'woman_sunset.png'
ALPHA = 0.5

with Image.open(INPUT_FILE1) as in_img1:
    in_img1 = in_img1.convert('RGB')
    in_stream1 = in_img1.get_flattened_data()
    size = in_img1.size

with Image.open(INPUT_FILE2) as in_img2:
    in_img2 = in_img2.convert('RGB')
    in_stream2 = in_img2.get_flattened_data()

out_stream = []
for (r1, g1, b1), (r2, g2, b2) in zip(in_stream1, in_stream2):
    color = (int((r1 * ALPHA) + (r2 * (1 - ALPHA))),
             int((g1 * ALPHA) + (g2 * (1 - ALPHA))),
             int((b1 * ALPHA) + (b2 * (1 - ALPHA))))
    out_stream.append(color)
out_img = Image.new('RGB', size)
out_img.putdata(out_stream)
out_img.save(OUTPUT_FILE)

print('Done!')
