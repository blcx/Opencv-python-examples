#Read image rescale function and show

import cv2

img = cv2.imread("Resources/lena.png")


def rescaleFrame(image, scale=2):
    width = int(image.shape[1] * scale)
    height = int(image.shape[0] * scale)
    dimensions = (width, height)
    return  cv2.resize(image,dimensions,interpolation=cv2.INTER_AREA)


resized = rescaleFrame(img)
cv2.imshow("OutputWindow", resized)

cv2.waitKey(0)
