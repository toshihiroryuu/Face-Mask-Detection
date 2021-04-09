import os
import cv2
import numpy as np
from PIL import Image

image_names = os.listdir("image_processing\\test-results\\sobels_filter\\input")

for image in image_names[0]:

    image = cv2.imread(image)
    dt_in = rgb_to_grey(image)

    array = sobels_filter(dt_in)
    dt_sb = Image.fromarray(array,'L')
    cv2.imwrite("test", dt_sb)
    # dt_sb.show()