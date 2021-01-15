import sys
import numpy as np
from PIL import Image

# python img/surprised_pikachu.jpg 10 120 img/surprised_pikachu.txt

char_aspect = .6

# parsing command line inputs
input_file, colors, output_width, output_file = sys.argv[1:]
try:
  ncolors = int(colors)
  if ncolors not in range(2, 10):
    raise ValueError
  output_width = int(output_width)
  if ncolors not in range(2, 10) or output_width not in range(80,121):
    raise ValueError

  original_img = Image.open(input_file)
  original_width, original_height = original_img.size

  img_bw_quantized = original_img.convert("L").quantize(colors=ncolors)

  scaling_factor = output_width / original_width
  processed_img = img_bw_quantized.resize((output_width, int(scaling_factor * original_height * char_aspect)))

  img_array = np.array(processed_img)

  gradient = " .:-=+*#%@"
  usable_gradient = [int(round(i)) for i in np.linspace(0, len(gradient) - 1, ncolors)]

  with open(output_file, "w") as f:
    for row in img_array:
        output = ""
        for value in row:
            output += gradient[usable_gradient[value]]
        f.write(output + "\n")
except:
  print("Invalid input for colors:acceptable is number range from 2-9 or invalid input for output_width: acceptable is number range from 80-120")


