import cv2

from sklearn.metrics.cluster import entropy


def detect_roughness(patch):
    blur = cv2.GaussianBlur(patch, (5, 5), 5)
    patch = cv2.cvtColor(blur, cv2.COLOR_BGR2GRAY)

    if entropy(patch) > 4:
        return True
    else:
        return False