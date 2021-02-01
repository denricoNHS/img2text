import sys
import argparse
import numpy as np
from PIL import Image

# python img/surprised_pikachu.jpg 10 120 img/surprised_pikachu.txt
# python3 img2text.py img/surprised_pikachu.jpg 10 120 img/surprised_pikachu.txt

char_aspect = .6

# parsing command line inputs
input_file, colors, output_width, output_file = sys.argv[1:]
ncolors = int(colors)
output_width = int(output_width)
parser = argparse.ArgumentParser(description='Change Images into ASCII Photos.')
parser.add_argument('input_file', help='location of the input image file')
parser.add_argument('colors', type=int, choices=range(1, 11), metavar='colors[1-10]', help='number of colors in gradient for picture (min:1, max:10)')
parser.add_argument('output_width', type=int, choices=range(80, 241), metavar='output_width[80-240]', help='number of pixels/characters the final photo width will have (min:80, max:240)')
parser.add_argument('output_file', help='location of the file that will store the final image')

original_img = Image.open(input_file)
args = parser.parse_args()

original_img = Image.open(args.input_file)
original_width, original_height = original_img.size

img_bw_quantized = original_img.convert("L").quantize(colors=ncolors)
img_bw_quantized = original_img.convert("L").quantize(args.colors)

scaling_factor = output_width / original_width
processed_img = img_bw_quantized.resize((output_width, int(scaling_factor * original_height * char_aspect)))
scaling_factor = args.output_width / original_width
processed_img = img_bw_quantized.resize((args.output_width, int(scaling_factor * original_height * char_aspect)))

img_array = np.array(processed_img)

gradient = " .:-=+*#%@"
usable_gradient = [int(round(i)) for i in np.linspace(0, len(gradient) - 1, ncolors)]
usable_gradient = [int(round(i)) for i in np.linspace(0, len(gradient) - 1, args.colors)]

with open(output_file, "w") as f:
with open(args.output_file, "w") as f:
    for row in img_array:
        output = ""
        for value in row:
            output += gradient[usable_gradient[value]]
        f.write(output + "\n")
