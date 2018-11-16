def crop_patch(image, step, window):
    for y in range(0, image.shape[0], step):
        for x in range(0, image.shape[1], step):
            yield x, y, image[y:y + window[1], x:x + window[0]]