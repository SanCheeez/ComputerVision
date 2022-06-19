from importlib.resources import path
import cv2
import numpy as np
import os
import tempfile


if not os.path.isdir("input_dir"):
    os.mkdir("input_dir")


def merge_channels(input_dir, output_dir):
    files = os.listdir(path=input_dir)
    for count in range(1, len(files) + 1):
        blu = cv2.imread(f'{input_dir}/00{count:03}_b.jpg', cv2.IMREAD_UNCHANGED)
        gre = cv2.imread(f'{input_dir}/00{count:03}_g.jpg', cv2.IMREAD_UNCHANGED)
        red = cv2.imread(f'{input_dir}/00{count:03}_r.jpg', cv2.IMREAD_UNCHANGED)

        # os.mkdir("output_dir ")
        if not os.path.isdir(f"{output_dir}"):
            os.mkdir(f"{output_dir}")

        img = cv2.merge((blu, gre, red))
        cv2.imwrite(f'{output_dir}/new_image_{count}.jpg', img)


merge_channels("input_dir", "output_dir")
