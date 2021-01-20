import sys
import numpy as np
from PIL import Image

# python img/surprised_pikachu.jpg 10 120 img/surprised_pikachu.txt

char_aspect = .6

# parsing command line inputs
try : 
input_file, colors, output_width, output_file = sys.argv[1:]
if  output_width <0: 
ncolors = int(colors)
output_width = int(output_width)
else:
raise ValueError("You input a width less than zero.") 
except ValueError:
print ("Enter integers only!")
original_img = Image.open(input_file)
original_width, original_height = original_img.size

img_bw_quantized = original_img.convert("L").quantize(colors=ncolors)

scaling_factor = output_width / original_width
processed_img = img_bw_quantized.resize((output_width, int(scaling_factor * original_height * char_aspect)))

img_array = np.array(processed_img)

gradient = " .:-=+*#%@"
gradient_scale= (len(gradient) - 1)/(ncolors-1)
scaled_array=np.rint(img_array * gradient_scale).astype(int)
with open(output_file, "w") as f:
    for row in scaled_array:
        output = ""
        for value in row:
            output += gradient[value]
        f.write(output + "\n")



