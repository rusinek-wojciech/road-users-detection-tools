from PIL import Image
import argparse
import os
import glob


def resize_img_with_stretch(image_file, size):
    image = Image.open(image_file)
    new_image = image.resize(size)
    new_image.save(image_file)


def resize_img_with_aspect_ratio(image_file, size):
    image = Image.open(image_file)
    image.thumbnail(size)
    image.save(image_file)


def args_input():
    parser = argparse.ArgumentParser(description="Give scale and folder to format images")
    parser.add_argument("-f", "--folder", default="images", help="Specify folder from runnable")
    parser.add_argument("-wi", "--width", help="Specify width")
    parser.add_argument("-he", "--height", help="Specify height")
    parser.add_argument('--stretch', dest='stretch', action='store_true', help="Stretch images")
    parser.add_argument('--aspect-ratio', dest='stretch', action='store_false', help="Keep images aspect ratio")
    parser.set_defaults(stretch=False)
    return parser.parse_args()


def main():
    args = args_input()
    width = int(args.width)
    height = int(args.height)
    stretch = bool(args.stretch)

    path = os.path.join(os.getcwd(), args.folder)
    img_files = glob.glob(path + '/*.jpg')
    length = len(img_files)
    if length == 0:
        raise Exception("No files provided")

    print(f'Calling script with for {length} files: ')
    print('Stretching' if stretch else 'Keeping aspect ratio')
    print(f'width = {width}px')
    print(f'height = {height}px')
    print(f'path = {path}')

    if stretch:
        for img_file in img_files:
            print(img_file)
            resize_img_with_stretch(img_file, (width, height))
    else:
        for img_file in img_files:
            print(img_file)
            resize_img_with_aspect_ratio(img_file, (width, height))

    print(f'Successfully scaled images')


main()
