import os
import cv2
import time
import argparse

from sys import platform
from patch_cropper import crop_patch
from table_creator import create_table
from crack_detector import detect_crack

start_time = time.clock()

parser = argparse.ArgumentParser()
parser.add_argument('--path', type=str, default=None, help = 'path to folder with images for training')
parser.add_argument('--patch', type=int, default=500, help = 'patch width and height and step in pixels')
arguments = parser.parse_args()

platform = platform.lower()

if platform == 'linux' or platform == 'linux2' or platform == 'darwin':
    slash = '/'
    print('1')
else:
    slash = '\''

input_path = 'input'
result_path = 'result_' + input_path + slash

rust_path = result_path + 'rust' + slash
crack_path = result_path + 'crack' + slash
nothing_path = result_path + 'nothing' + slash

patch_size = 5000

if not os.path.exists(result_path):
    os.mkdir(result_path)
    os.mkdir(rust_path)
    os.mkdir(crack_path)
    os.mkdir(nothing_path)

    create_table(result_path)

for file in os.listdir(input_path):
    image = cv2.imread(input_path + file)

    rust = False
    crack = False
    nothing = False

    for x, y, window in crop_patch(image, patch_size, (patch_size, patch_size)):
        if window.shape[0] != patch_size or window.shape[1] != patch_size:
            continue

        patch = image[y:y + patch_size, x:x + patch_size]
        if detect_crack(patch):
            print(detect_crack(patch))
            image[y:y + patch_size, x:x + patch_size] = [0,0,255]
            cv2.imwrite(crack_path + file, image)
