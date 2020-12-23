# img2text
A command line script to convert images to text 

## Usage:
**Homework:** Write a description for how to use the program here
In order to use this program, you will need the image that will be converted.  Then, run the file by using
python3 on the command line, and include the parameters needed in order for this function to work.  This
program will then take your picture, convert it to the size you requested, and also change the color to black
and white.  Then, based on the number of colors you have picked, the picture will be transformed to have
only the specified amount of colors.  Finally, using our gradient of characters, each of the pixels will be
replaced with the character mapped to that colored pixel.  The finished ASCII Photo will then be saved in
the text file of your choice.
So this is how you would run the file:
$ python3 img2text.py original_image colors output_width final_text_file

## Options:
**Homework:** Write your description of each of the options here
In order for this program to work, there are a few arguments that you will have to include in order for the
program to function.  After you use python3 to run the file, you will first need to write the location of
the original picture that you want to convert.  The next argument would be the number of colors you want the
image to have.  Your image can have up to a 10-color gradience, so you can pick a number from 1 - 10.  Then,
the next input would be the integer width of your picture.  You would state how many pixels/characters wide
you want your picture to be, and your photo will be resized to be proportional to the new width.  Finally, the
last input is the name/location of the text file you want to use in order to save your new ASCII Photo.
If the text file is not found, a new one will be made with the name given, in the location that is said.
