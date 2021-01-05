# img2text
A command line script to convert images to text 

## Usage:

1. Run `cd img` to change directory

2. Import your image into this directory

3. Run `cd ..` to go back to the main directory

4. Run the file `img2text.py` using `python3` with the needed arguments
   *The format of the line should look like this:*
   `python3 img2text.py original_image colors output_width final_text_file`

Your result will be a text file with the finished version of the ASCII Photo

## Options:

`python3` is what we are using to run the file. **DON'T CHANGE THIS OPTION!**

`img2text.py` is the file that has all of the code that we will need. **DON'T CHANGE THIS OPTION!**

`original_image` is the location of the image that you want to convert.

`colors` is the number of colors you want your final image to have. *Has to be an integer.*

`output_width` is the number of pixels/characters that your final image width will have. *Has to be an integer.*

`final_text_file` is the location of the text file in which your ASCII Photo will be saved. If the file can't be located, a new one will be made.
