from PIL import Image

INPUT_FILE = 'snake.png'
OUTPUT_FILE1 = 'grayscale_average_snake.png'
OUTPUT_FILE2 = 'grayscale_luma_snake.png'

with Image.open(INPUT_FILE) as in_img:
    in_img = in_img.convert('RGB')
    size = in_img.size
    in_stream = in_img.get_flattened_data()

out_stream1 = []
out_stream2 = []
for (red, green, blue) in in_stream:
    average = (red + green + blue) // 3
    out_stream1.append(average)
    luma = int(0.299 * red +0.587 * green +0.114 * blue)
    out_stream2.append(luma)

out_img1 = Image.new('L', size)
out_img1.putdata(out_stream1)
out_img1.save(OUTPUT_FILE1)

out_img2 = Image.new('L', size)
out_img2.putdata(out_stream2)
out_img2.save(OUTPUT_FILE2)

print('Done!')
