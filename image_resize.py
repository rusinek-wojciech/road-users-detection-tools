from PIL import Image
import argparse
import os
import glob


def scale_image(image_file, scale: float):
    image = Image.open(image_file)
    print(image_file)
    x, y = image.size
    new_size = (int(x * scale), int(y * scale))
    new_image = image.resize(new_size)
    new_image.save(image_file)


def args_input():
    parser = argparse.ArgumentParser(description="Give scale and folder to format image")
    parser.add_argument("-sc", "--scale", default=1.0, help="Specify used scale")
    parser.add_argument("-f", "--folder", default="images", help="Specify folder from runnable")
    return parser.parse_args()


def main():
    args = args_input()
    image_path = os.path.join(os.getcwd(), args.folder)
    print('Calling script with: ')
    print(f'scale = {args.scale}')
    print(f'path = {image_path}')
    for image_file in glob.glob(image_path + '/*.jpg'):
        scale_image(image_file, float(args.scale))
    print('Successfully scaled all images')


main()

