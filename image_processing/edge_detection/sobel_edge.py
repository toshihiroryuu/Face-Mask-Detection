import cv2
import numpy as np

# perform edge detection using sobels filter on grey-scale image.

def sobels_filter(grey_img):
    
    # 3 x 3 filter
    filter_h, filter_w = 3, 3

    filter_coeffx = [[-1, 0, 1], 
                    [-2, 0, 2], 
                    [-1, 0, 1]]

    filter_coeffy = [[-1, -2, -1], 
                    [0, 0, 0], 
                    [1, 2, 1]]

    #padding on sides.
    pad_h, pad_w = int((filter_h-1)/2), int((filter_w-1)/2)

    data_h = int(grey_img.shape[0]+ (2 * pad_h))
    data_w = int(grey_img.shape[1] + (2 * pad_w))

    data = np.zeros([data_h , data_w])

    data[pad_h:int(data_h - pad_h), pad_w:int(data_w - pad_w)] = grey_img

    out_lst = []
    out_lstx = []
    out_lsty = []
    for i in range(grey_img.shape[0]):
        for j in range(grey_img.shape[1]):
            # convolution in x-direction.
            out_lstx.append(np.sum((data[i:i + filter_h, j:j + filter_w])*filter_coeffx)/(filter_h*filter_w))
            # convolution in y-direction.
            out_lsty.append(np.sum((data[i:i + filter_h, j:j + filter_w])*filter_coeffy)/(filter_h*filter_w))

    out_lst = [ abs(i) + abs(j) for i,j in zip(out_lstx, out_lsty) ]

    #reshape list to image size.
    sb_fil_img = np.reshape(out_lst, (grey_img.shape[0], grey_img.shape[1]))
    sb_fil_img = np.array(array, dtype = np.uint8)
    
    return sb_fil_img
