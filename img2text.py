import sys
import numpy as np
from PIL import Image

# python img/surprised_pikachu.jpg 10 120 img/surprised_pikachu.txt

char_aspect = .6

# parsing command line inputs
input_file, colors, output_width, output_file = sys.argv[1:]

gradient = " .:-=+*#%@"

try:
     ncolors = int(colors)
     if (ncolors <= 0) or (ncolors > len(gradient)):
         print("Invalid input. The number of colors has to be between 0 and 10.")
         sys.exit()
except ValueError:
     print("The number of colors has to be a number!")
     sys.exit()

try:
     output_width = int(output_width)
     if (output_width < 80) or (output_width > 240):
         print("Invalid input. The width has to be between 80 and 240.")
         sys.exit()
except ValueError:
     print("The width has to be a number!")
     sys.exit()

original_img = Image.open(input_file)
original_width, original_height = original_img.size

img_bw_quantized = original_img.convert("L").quantize(colors=ncolors)

scaling_factor = output_width / original_width
processed_img = img_bw_quantized.resize((output_width, int(scaling_factor * original_height * char_aspect)))

img_array = np.array(processed_img)

usable_gradient = [int(round(i)) for i in np.linspace(0, len(gradient) - 1, ncolors)]

with open(output_file, "w") as f:
    for row in img_array:
        output = ""
        for value in row:
            output += gradient[usable_gradient[value]]
        f.write(output + "\n")



