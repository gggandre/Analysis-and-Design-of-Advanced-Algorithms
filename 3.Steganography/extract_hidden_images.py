# ----------------------------------------------------------
# Lab #1: Steganography
# Image processing through bit manipulation.
#
# Date: 26-Aug-2022
# Authors:
#           A01745336 Diego Alejandro Balderas Tlahuitzo
#           A01753176 Gilberto André García Gaytán
# ----------------------------------------------------------
import sys
from PIL import Image


def process_image(file_name: str) -> None:
    if ".png" in file_name:
        image = Image.open(file_name)
        if image.mode == "RGB":
            # extract_hidden_images(image)
            pixin = image.load()  # type: ignore
            width, height = image.size
            output_image = Image.new('1', (width, height))
            pixout = output_image.load()  # type: ignore
            for y in range(height):
                for x in range(width):
                    r, _, _ = pixin[x, y]
                    pixout[x, y] = r & 1  # black
            output_image.save("scarlett_chanel_1_red.png")
            for y in range(height):
                for x in range(width):
                    _, g, _ = pixin[x, y]
                    pixout[x, y] = g & 1  # black
            output_image.save("scarlett_chanel_2_green.png")
            for y in range(height):
                for x in range(width):
                    _, _, b = pixin[x, y]
                    pixout[x, y] = b & 1
            output_image.save("scarlett_chanel_3_blue.png")
        else:
            print("The mode of the file is not RGB.")
            sys.exit()
    else:
        print("The provided file name doesn’t have a .png extension.")
        sys.exit()


try:
    if __name__ == '__main__':
        INPUT_FILE_NAME = sys.argv[1]
        process_image(INPUT_FILE_NAME)
except:
    print("The name of the file was not provided as a command line argument.")
