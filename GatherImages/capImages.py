import cv2
import numpy as np
import os
import time

camera = cv2.VideoCapture(0)
camera.set(cv2.CAP_PROP_FRAME_WIDTH, 416)
camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 416)
if not camera.isOpened():
    print("no camera detected...")
    exit()

print("Capturing Images...")

num_images = 0
count = 0

while count < 10:
    status, img = camera.read()
    cv2.imshow("feed", img)

    if status:
        cv2.imwrite("Images/test_image_%d.jpg" % num_images, img)
        num_images += 1
        print("Saved %d image..." % num_images)
        time.sleep(2)
    else:
        print("No Frame being capture, exiting...")
        exit()

    cv2.waitKey(1)
    count += 1
