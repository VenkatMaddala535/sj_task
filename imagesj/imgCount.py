#!/usr/bin/env python
import os

images = os.listdir('/dd/home/balajid/sj_task/data')
exr_images = []

for image in images:
    if image.endswith(".exr"):
        exr_images.append(image)

wg = len(exr_images)

print(f"on total images we have {wg}  exr")
