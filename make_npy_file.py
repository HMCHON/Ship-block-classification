###############################
# Make .npz file
###############################

import os
import sys
import cv2
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from PIL import Image

#np.set_printoptions(threshold=sys.maxsize)

groups_folder_path = '/home/user/PycharmProjects/lecture/Boundary_Project/images/prediction/con_Zoom_out'
#print(groups_folder_path)
# categories = ['B1718', 'E170A', 'E811']
categories = ['B1', 'B2', 'B3']
num_classes = len(categories)

#x_train = 6000,28,28
#y_train = 6000
#x_test = 1000,28,28
#y_test = 1000

image_w = 224
image_h = 224

X = []
Y = []

for idex, categorie in enumerate(categories):
    label = [idex]
    image_dir = groups_folder_path + '/'  + categorie + '/'
    
    for top, dir, f in os.walk(image_dir):
        for filename in f:
            image_name = image_dir + '/' + filename
            print(image_name)
            img = cv2.imread(image_name, cv2.IMREAD_COLOR)
            img = cv2.resize(img, None,fx = image_w/img.shape[1], fy = image_h/img.shape[0])
            
            # cv2.imshow('img', img)
            # cv2.waitKey(0)
            # cv2.destroyAllWindows()


            X.append(img/255)
            Y.append(label)

X1 = np.array(X)
Y1 = np.array(Y)


#X_train, X_test, Y_train, Y_test = train_test_split(X1,Y1,test_size=0.5)
#xy = X_train, Y_train, X_test, Y_test
#print(xy)
    
np.save('./con_224_X.npy', X1)
np.save('./con_224_y.npy', Y1)

print('Successfully converted image to npy.')
