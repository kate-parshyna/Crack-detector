import numpy as np
from skimage import io, color, img_as_ubyte
from skimage.feature import greycomatrix, greycoprops
from sklearn.metrics.cluster import entropy

rgbImg = io.imread('3.jpg')
grayImg = img_as_ubyte(color.rgb2gray(rgbImg))
print(entropy(grayImg))