#################################################################
## 2020.01.21 HAEMYUNG                                         ##
## This code is about Moving image randomly                    ##
## [parameter]                                                 ##
#################################################################

import random
import os
import glob
import shutil
# Load image sentence (list type)
folder_name = 'B3'
img_path = os.path.join('/home/user/PycharmProjects/lecture/Boundary_Project/imageset/new_original_2/5000by3000/5000by3000_crop_con_76_train_test/train/'+folder_name) #Image folder Path
file_list = os.listdir(img_path) # Load file with os
img_file_list1 = [file for file in file_list if file.endswith(".jpg")] # Load img_file name with os
img_file_list2 = [file for file in file_list if file.endswith(".png")] # Load img_file name with os
img_file_list = img_file_list1 + img_file_list2

# train:test = 8:2
file_list = img_file_list
train_number = round(len(file_list) * 0.8)
test_number = len(file_list) - train_number

# Extract at random from file_list
test_filename = random.sample(file_list,test_number)

# File Move
testll = len(test_filename)

i = 0
while i <= testll-1:
    file_name = test_filename[i]
    dir = os.path.join('/home/user/PycharmProjects/lecture/Boundary_Project/imageset/new_original_2/5000by3000/5000by3000_crop_con_76_train_test/test/'+folder_name+'/'+file_name) # After
    src = os.path.join(img_path+'/'+file_name) # Before
    shutil.move(src, dir)
    # print(i)
    i = i+1
