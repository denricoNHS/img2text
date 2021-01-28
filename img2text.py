import argparse
import numpy as np
from PIL import Image

# python3 img2txt.py img/surprised_pikachu.jpg 10 120 img/surprised_pikachu.txt

char_aspect = .6

# parsing command line inputs
parser = argparse.ArgumentParser(description='Process some integers.')
ncolors = int(colors)	parser.add_argument('integers', metavar='N', type=int, nargs='+',
output_width = int(output_width)	                    help='an integer for the accumulator')
parser.add_argument('--sum', dest='accumulate', action='store_const',
                    const=sum, default=max,
                    help='sum the integers (default: find the max)')

args = parser.parse_args()
print(args.accumulate(args.integers))

original_img = Image.open(input_file)
original_width, original_height = original_img.size

img_bw_quantized = original_img.convert("L").quantize(args.color)

scaling_factor = args.output_width / original_width
processed_img = img_bw_quantized.resize((args.output_width, int(scaling_factor * original_height * char_aspect)))

img_array = np.array(processed_img)

gradient = " .:-=+*#%@"
usable_gradient = [int(round(i)) for i in np.linspace(0, len(gradient) - 1, args.color)]

with open(args.output_file, "w") as f:
    for row in img_array:
        output = ""
        for value in row:
            output += gradient[usable_gradient[value]]
        f.write(output + "\n")
