import argparse
import numpy as np
from PIL import Image

# python3 img2text.py img/surprised_pikachu.jpg 10 120 img/surprised_pikachu.txt

char_aspect = .6

# parsing command line inputs
parser = argparse.ArgumentParser(description='converting pictures to text')
parser.add_argument("input_file", help="path to the original image")
parser.add_argument("color", help="an integer number of shades of gray for the output image (min: 2, max: 10)", type=int)
parser.add_argument("output_width", help="an integer number of pixels for the output image", type=int)
parser.add_argument("output_file", help="the file where the output will be written")
parser.add_argument("-w", "--web", action="store_true", help="use link instead of file")

args = parser.parse_args()

if args.web == True:
 	original_img = Image.open(requests.get(args.input_file, stream=True).raw)
else:
 	original_img = Image.open(args.input_file)

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

