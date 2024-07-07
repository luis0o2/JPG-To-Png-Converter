from PIL import Image
import sys
import os

dir = "New"
parent_dir = 'C:\\Users\\ochoa\\PycharmProjects\\images\\.venv\\Pokedex'
path = os.path.join(parent_dir,dir)
if not os.path.exists(path):
    os.makedirs(path)
    dir_list = os.listdir(path)
    print(f'Files and directories{path}')
    print(dir_list)
else:
    print('path already exists')

files = os.listdir(parent_dir)

for x in files:
    if x.endswith('.jpg'):
        img = Image.open(os.path.join(parent_dir, x))
        img.save(os.path.join(path, os.path.splitext(x)[0] + '.png'), 'png')
        print('done')