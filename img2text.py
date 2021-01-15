import sys
import numpy as np
from PIL Import Image

# python img/surpised_pikachu.jpg 10 120 img/surpised_pikachu.txt

char aspect = 6
gradient =" .:=+*#%@" 

#parsing commad line imputs
input_file, colors, out_width, output_file = sys.argv[1:]
ncolors = int(colors)
output_width = int(output_eidth)

orginal_img = Image.open(input_file)
orginal_width, orginal_height = orginal_img.size 

img_bw_quantized = orginal_img.convert("L").quantize(colors=ncolors)

scaling_factor = output_width / orginal_width
processed_img = img_bw_quantized.resize((output_width, int(scaling_factor * orginal_height * c
____________________________________________________________________________________________________
img.array = np.array(processed_img)
gradient_scale = (len(gradient) - 1) / (ncolrs-1)
scaled_array = np.rint(img_array * gradient_scale).astype(int)
                                               
with open(output_file, "w") as f:
    for row in scaled_array:
        output = ""
        for value in row:
            output += gradient[value]
        f.write(output + "\n")
