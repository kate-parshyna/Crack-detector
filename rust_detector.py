import cv2
import numpy


def detect_rust(patch):
    blur = cv2.GaussianBlur(patch, (5, 5), 5)
    hsv = cv2.cvtColor(blur, cv2.COLOR_BGR2HSV)
    lowermask = cv2.inRange(hsv, lower_color1, upper_color1)
    #uppermask = cv2.inRange(hsv, lower_color2, upper_color2)

    if 255 in lowermask.flatten():
        return True
    #elif 255 in uppermask.flatten():
    #    return True
    else:
        return False

lower_color1 = numpy.array([20, 20, 50])
upper_color1 = numpy.array([50, 50, 100])

lower_color2 = numpy.array([170, 0, 0])
upper_color2 = numpy.array([255, 255, 255])