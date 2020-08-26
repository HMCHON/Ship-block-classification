import os
import cv2
import glob
import numpy as np
import natsort

i = 0
f = 0
Error = []
number = []
#/home/user/PycharmProjects/lecture/Boundary_Project/test
#/home/user/PycharmProjects/lecture/Boundary_Project/imageset/new_original/B1
img_path = '/home/user/PycharmProjects/lecture/Boundary_Project/test' #Image folder Path
path_dir = os.listdir(img_path)
img_file_list_jpg = [file for file in path_dir if file.endswith(".jpg")] # Load img_file name with os
img_file_list_png = [file for file in path_dir if file.endswith(".png")]
img_file_list = img_file_list_jpg + img_file_list_png
load_img = natsort.natsorted(img_file_list,reverse=False)


while i <= len(load_img)-1:
    load_imga = img_path + '/' + load_img[i]
    #load_imgb = img_path + '/' + load_img[i*2]
    img = cv2.imread(load_imga)
    #img2 = cv2.imread(load_imgb)
    imgaaa = cv2.resize(img, (224,224))
    #imgbbb = cv2.resize(img2, (224,224))
    cv2.imshow(load_img[i], imgaaa)
    #cv2.imshow(load_img[i+1], imgbbb)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    i = i+1