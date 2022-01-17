import os
from glob import glob
import shutil
from sklearn.model_selection import train_test_split
# do test train splitting
train_ratio = 0.70
test_ratio=0.15
val_ratio = 0.15
# find image names
image_files = glob("images/*.jpg")
# remove file extension
image_names = [name.replace(".jpg","").lstrip("images/") for name in image_files]
# Use scikit learn function for convenience
train_names_temp, test_names = train_test_split(image_names, test_size=test_ratio)
train_names, val_names = train_test_split(train_names_temp, test_size=val_ratio/(1-test_ratio))
def batch_move_files(file_list, source_path, destination_path):
    for file in file_list:
         image = file+'.jpg'
         xml = file+'.xml'
         shutil.move(os.path.join(source_path, image), os.path.join(destination_path, image))
         shutil.move(os.path.join(source_path, xml), os.path.join(destination_path, xml))
    return

source_dir = "images/"
test_dir = "images/test/"
train_dir = "images/train/"
val_dir = "images/val/"


test_val=len(set(test_names))
train_val = len(set(train_names))
val_val = len(set(val_names))
print(f'{test_val=}')
print(f'{train_val=}')
print(f'{val_val=}')
batch_move_files(test_names, source_dir, test_dir)
batch_move_files(train_names, source_dir, train_dir)
batch_move_files(val_names, source_dir, val_dir)