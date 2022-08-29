import cv2
import numpy as np

camera = cv2.VideoCapture(0)

while True:

    ret, frame = camera.read()
    image = cv2.imshow("image", frame)
    cv2.waitKey(1)
