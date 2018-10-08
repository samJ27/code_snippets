import os

# Rename a large series of files

path = '.../data/concrete/train/positive'
files = os.listdir(path)
i = 20001

for file in files:
    os.rename(os.path.join(path, file), os.path.join(path, str(i)+'.jpg'))
    i = i+1
