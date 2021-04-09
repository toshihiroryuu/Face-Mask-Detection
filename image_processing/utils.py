import cv2

# convert rgb image to grey-scale image.
def rgb_to_grey(rgb_img):
    grey_img = cv2.cvtColor(rgb_img, cv2.COLOR_BGR2GRAY)
    return grey_img

# convert grey-scale image to rgb image.
def grey_to_rgb(grey_img):
    return rgb_img
