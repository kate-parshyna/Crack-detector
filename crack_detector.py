import os
import cv2
import numpy as np

from matplotlib import pyplot as plt
i = 0 

def detect_crack(patch):
    global i
    
    # patch = cv2.GaussianBlur(patch,(1,1),0)
    
    lap = cv2.Laplacian(cv2.cvtColor(patch, cv2.COLOR_BGR2GRAY), cv2.CV_64F)
    plt.imsave(str(i) + 'laptemp.jpg', lap, cmap='gray')

    patch_mask_lap = cv2.imread(str(i) + 'laptemp.jpg')

    edges_lap = cv2.Canny(patch_mask_lap, 100, 200, apertureSize=3)
    plt.imsave(str(i) + 'edgeslaptemp.jpg', edges_lap, cmap='gray')
    minLineLength = 0
    maxLineGap = 500

    lines_lap = cv2.HoughLinesP(edges_lap,1,np.pi/180,90,minLineLength,maxLineGap)
    i = i + 1
    # os.remove('laptemp.jpg')

    try:
        for x in range(0, len(lines_lap)):
            for x1, y1, x2, y2 in lines_lap[x]:
                cv2.line(patch, (x1, y1), (x2, y2), (0, 0, 255), 3)
                cv2.imwrite('result_input/filename.jpg', patch)
                return [x1, y1, x2, y2],
    except Exception:
        return False
