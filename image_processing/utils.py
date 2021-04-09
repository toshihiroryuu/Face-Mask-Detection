import cv2

# convert rgb images to grey-scale images.
def rgb_to_grey(rgb_img):
    grey_img = cv2.cvtColor(rgb_img, cv2.COLOR_BGR2GRAY)
    return grey_img

# convert grey-scale images to rgb images.
def grey_to_rgb(grey_img):
    return rgb_img