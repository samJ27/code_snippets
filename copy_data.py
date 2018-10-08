import os
import shutil
import random

# short snippet to move random files to create a validation set

root_dir = '.../data/concrete/train/positive'
output_dir = '.../data/concrete/test'

files = [file for file in os.listdir(root_dir)]
list_files = random.sample(files, 6166)

for x in list_files:
    shutil.move(os.path.join(root_dir, x), output_dir)
