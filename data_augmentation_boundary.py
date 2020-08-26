#####################
# Data Augmentation #
#####################
from tqdm import tqdm
import numpy as np
import cv2
import matplotlib.pyplot as plt
import math
import sys
import os
import natsort


# from sklearn.model_selection import train_test_split
# from PIL import Image

###############################################################################

# Load Image from folder

def augmentation(image_name, image_path, save_path, Rotate30=None, Rotate60=None,
             Rotate90=None, HFlip0=None, HFlip1=None):

    
    img = cv2.imread(image_path)    
    
    if Rotate30 is True:
        rows, cols = img.shape[:2]
        M30 = cv2.getRotationMatrix2D((cols / 2, rows / 2), 30, 1)
        img_rotate30 = cv2.warpAffine(img, M30, (rows, cols))
        img_name1 = '%s%s' %('rotate_30_',image_name)
        cv2.imwrite(os.path.join(save_path, img_name1), img_rotate30)
            
    if Rotate60 is True:
        rows, cols = img.shape[:2]
        M60 = cv2.getRotationMatrix2D((cols / 2, rows / 2), 60, 1)
        img_rotate60 = cv2.warpAffine(img, M60, (rows, cols))
        img_name2 = '%s%s' %('rotate_60_',image_name)
        cv2.imwrite(os.path.join(save_path, img_name2), img_rotate60)
        
    if Rotate90 is True:
        rows, cols = img.shape[:2]
        M90 = cv2.getRotationMatrix2D((cols / 2, rows / 2), 90, 1)
        img_rotate90 = cv2.warpAffine(img, M90, (cols, rows))
        img_name3 = '%s%s' %('rotate_90_',image_name)
        cv2.imwrite(os.path.join(save_path, img_name3), img_rotate90)
    
    if HFlip0 is True:
        img_HFlip0 = cv2.flip(img, 0)
        img_name4 = '%s%s' %('HFlip0_',image_name)
        cv2.imwrite(os.path.join(save_path, img_name4), img_HFlip0)
    
    if HFlip1 is True:
        img_HFlip1 = cv2.flip(img, 1)
        img_name5 = '%s%s' %('HFlip1_',image_name)
        cv2.imwrite(os.path.join(save_path, img_name5), img_HFlip1)

###################################################################################
# Data_aug(categories,group_folder_path,Rotate30,Rotate60,Rotate90,HFlip0,HFlip1) #
###################################################################################
img_path = '/home/user/PycharmProjects/lecture/Boundary_Project/imageset/new_original_2/5000by3000/5000by3000_crop_con_76_dataaug/B3' #Image folder Path
path_dir = os.listdir(img_path)
img_file_list_jpg = [file for file in path_dir if file.endswith(".jpg")] # Load img_file name with os
img_file_list_png = [file for file in path_dir if file.endswith(".png")]
img_file_list = img_file_list_jpg + img_file_list_png
load_img = natsort.natsorted(img_file_list,reverse=False)
save_path = img_path

i = 0

while i <= len(load_img)-1:
    img_name = load_img[i]
    img_p = img_path + '/' + load_img[i]
    img = cv2.imread(img_p)
    start = augmentation(image_name = img_name,
                         image_path = img_p,
                         save_path=save_path,
                         Rotate30=True,
                         Rotate60=True,
                         Rotate90=True,
                         HFlip0=True,
                         HFlip1=True)
    i = i+1
    
    
    
# NPY = make_npy(categories = ['A', 'B', 'C', 'D'], group_folder_path = '/home/user/keras/npy_project/images/DATASET/')
