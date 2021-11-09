from PIL import Image
import argparse
import os
import glob


def resize_image(image_file, size):
    image = Image.open(image_file)
    print(image_file)
    new_image = image.resize(size)
    new_image.save(image_file)


def args_input():
    parser = argparse.ArgumentParser(description="Give sizes and folder to format image")
    parser.add_argument("-f", "--folder", default="images", help="Specify folder from runnable")
    parser.add_argument("-wi", "--width", help="Specify width")
    parser.add_argument("-he", "--height", help="Specify height")
    return parser.parse_args()


def main():
    args = args_input()
    width = int(args.width)
    height = int(args.height)

    image_path = os.path.join(os.getcwd(), args.folder)
    print('Calling script with: ')
    print(f'width = {width}px')
    print(f'height = {height}px')
    print(f'path = {image_path}')

    images = glob.glob(image_path + '/*.jpg')
    length = len(images)
    if length == 0:
        raise Exception("No files provided")

    for image_file in images:
        resize_image(image_file, (width, height))
    print(f'Successfully scaled {length} images')


main()
