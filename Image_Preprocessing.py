import os
import cv2
import glob
import numpy as np
import natsort
###############################################################################    
def Contours(image_name, load_img_path, show=False, save = False):
    #################################################################
    ## 2020.01.21 HAEMYUNG                                         ##
    ## This code is about Contour Extract from input image         ##
    ## [parameter]                                                 ##
    ##   load_img : loaded image                                   ##
    ## [return]                                                    ##
    ##   contours : contour array from cv2.findContours function   ##
    #################################################################
    
    img2 = cv2.imread(load_img_path)
    imgray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
    ret, thr = cv2.threshold(imgray, 78, 255, cv2.THRESH_BINARY)  # White Bakckground, Black Object #Prediction = 100, Training = 76
    contours, _ = cv2.findContours(thr, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(img2, contours, -1, (0, 255, 0), 1)

    # Define show & save argument
    if show == True:
        cv2.imshow('thr', thr)
        cv2.imshow('contours', img2)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    if save == True:
        
        save_path_con = '%s%s' %(img_path,'/con')
        if not(os.path.isdir(os.path.join(save_path_con))):
            os.makedirs(os.path.join(save_path_con))
            
        contours_img_name_1 = '%s%s%s' % (save_path_con,'/con_',image_name)
        contours_img_name_2 = '%s%s%s' % (save_path_con,'/thr_',image_name)
        cv2.imwrite(contours_img_name_1, thr)
        cv2.imwrite(contours_img_name_2, img2)
    elif save == False:
        pass

    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return contours
###############################################################################
def Seek_maxmin(Contour, i):
    #################################################################
    ## 2020.01.21 HAEMYUNG                                         ##
    ## This code is about find maximum,minimum x and y cordinate   ##
    ## [parameter]                                                 ##
    ##   Contour : Contour array from 'def_Contours'               ##
    ##   i : Performance number                                    ##
    ## [return]                                                    ##
    ##   Array : x and y cordinate (max_x, max_y, min_x, min_y)    ##
    #################################################################

    # Definite parameter
    width = img.shape[0]
    height = img.shape[1]
    Max_x = []
    Max_y = []
    Min_x = []
    Min_y = []
    s = 0
    ls = len(Contour)
    max_x, max_y, min_x, min_y = 0, 0, 100000, 100000

    # About find maximum and minimum x,y cordinate
    while s <= ls-1:
        d, f, g = 0, 0, 0
        ld = Contour[s].shape[0]
        while d <= ld-1:
            lg = Contour[s][d][0].shape[0]
            while g <= lg-1:
                if g == 0:
                    x = Contour[s][d][0][g]
                    g = g+1
                    if x <= 10 or x >= height-10:
                        pass
                    else:
                        if max_x <= x:
                            max_x = x
                        elif x <= min_x:
                            min_x = x
                        else:
                            pass
                elif g == 1:
                    y = Contour[s][d][0][g]
                    g = g+1
                    if y<= 10 or y >= width-10:
                        pass
                    else:
                        if max_y <= y:
                            max_y = y
                        elif y <= min_y:
                            min_y = y
                        else:
                            pass
            g = 0
            d = d+1
        s = s+1

    # About append arrray sentence
    Max_x.append(max_x)
    Max_y.append(max_y)
    Min_x.append(min_x)
    Min_y.append(min_y)

    # About Change append array to numpy array
    Max_array_x = np.array(Max_x)
    Max_array_y = np.array(Max_y)
    Min_array_x = np.array(Min_x)
    Min_array_y = np.array(Min_y)
    Array = np.array((Max_array_x,Max_array_y,Min_array_x,Min_array_y))

    return Array
###############################################################################
def Countor_Extraction(Array, i, img, show=True):
    #################################################################
    ## 2020.01.21 HAEMYUNG                                         ##
    ## This code is about extract object region                    ##
    ## [parameter]                                                 ##
    ##   Array : Contour array from 'def_Seek_maxmin'              ##
    ##   i : Performance number                                    ##
    ##   img : Input image                                         ##
    ##   save : Show and save Image Contains object region area    ##
    ## [return]                                                    ##
    ##   rect_array : square cordinate array , offset = 10         ##
    ##                (min_x, min_y, max_x, max_y)                 ##
    #################################################################

    # Definite parameter from Contour Array
    max_x = Array[0][0]
    min_x = Array[2][0]
    max_y = Array[1][0]
    min_y = Array[3][0]

    # Calculate circle radius
    x = max_x - min_x
    y = max_y - min_y
    r = round(((x**2 + y**2)**0.5)/2)
    r = int(r)
    x = round(max_x+min_x)/2
    x = int(x)
    y = round(max_y+min_y)/2
    y = int(y)

    # Calculate Square that tangent to a circle
    X1,Y1,X2,Y2 = x-r,y-r,x+r,y+r
    X1 = int(X1) 
    Y1 = int(Y1) 
    X2 = int(X2) 
    Y2 = int(Y2) 
    rect_array = np.array((X1,Y1, X2, Y2))
    
    # Define show argument
    if show == True:
        img1 = cv2.rectangle(img, (min_x, min_y), (max_x, max_y), (0, 0, 255), 2)
        img2 = cv2.circle(img, (x, y), r, (0, 0, 255), 2)
        img3 = cv2.rectangle(img2, (X1, Y1), (X2, Y2), (0, 0, 255), 2)
        conext_img_name = '%s%d%s' % ('Img_conext', i, '.png')
        cv2.imwrite(conext_img_name, img3)
        #cv2.imshow('img3', img3)
        #cv2.waitKey(0)
        #cv2.destroyAllWindows()
    elif show == False:
        pass

    return rect_array
###############################################################################
def Crop_img(i, img, crop_region, image_name, save_path=None):
    #################################################################
    ## 2020.01.22 HAEMYUNG                                          #
    ## This code is about image Crop considering boundary condition #
    ## [parameter]                                                  #
    ##   i : Performance number                                     #
    ##   img : Input Image                                          #
    ##   crop_region : (min_x, min_y, max_x, max_y) numpy array     #
    ## [return]                                                     #
    ##   crop_img_shape : cropped image shape array                 #
    #################################################################


    # Parameter definite
    w = img.shape[1]
    h = img.shape[0]


    # About min_x condition sentence
    if crop_region[0] <= 0:
        crop_region[0] = 0
    elif crop_region[0] >= w:
        crop_region[0] = w

    # About min_y condition sentence
    if crop_region[1] <= 0:
        crop_region[1] = 0
    elif crop_region[1] >= h:
        crop_region[1] = h

    # About max_x condition sentence
    if crop_region[2] <= 0:
        crop_region[2] = 0
    elif crop_region[2] >= w:
        crop_region[2] = w

    # About max_y condition sentence
    if crop_region[3] <= 0:
        crop_region[3] = 0
    elif crop_region [3] >= h:
        crop_region[3] = h

    # Image Crop and Save sentence
    
    if crop_region[2]-crop_region[0] >= crop_region[3]-crop_region[1]:
        hhh = (crop_region[3]-crop_region[1])/2
        center = (crop_region[2]-crop_region[0])/2 + crop_region[0]
        crop_region[0] = center-hhh
        crop_region[2] = center+hhh
       
    img4 = img[crop_region[1]:crop_region[3],crop_region[0]:crop_region[2]]
    img_name = '%s%s' % ('crop_',image_name)
    if save_path == None:
        cv2.imwrite(img_name, img4)
    if not save_path == None:
        cv2.imwrite(os.path.join(save_path + '/' , img_name), img4)
    
    crop_img_shape = img4.shape

    return crop_img_shape
###############################################################################
def Error_image_seek(i, img, image_file_list, Error, number, crop_img_shape, percent=0.1):
    ##################################################################
    ## 2020.01.30 HAEMYUNG                                           #
    ## This code is about Seek wrong cropped image                   #
    ## [parameter]                                                   #
    ##   i : Performance number                                      #
    ##   crop_img : Cropped image shape                              #
    ##   percent : On the basis of Original image,                   #
    ##             smaller than percent% less is wrong cropped image #
    ##             (0<=percent<=1)                                   #
    ## [return]                                                      #
    ##   Error : Wrong cropped image name Array                      #
    ##################################################################

    # Parameter definite
    W = crop_img_shape[1]
    wrong_W_size = img.shape[1]*percent

    # About Seek wrong cropped image sentence and append Error array
    if W <= wrong_W_size:
        Error_img = img
        Error.append(Error_img)
    else:
        pass

    Error = np.array(Error)
    if i == len(image_file_list)-1:
        print('Error_array', Error)

    return Error
###############################################################################
i = 0
f = 0
Error = []
number = []
#/home/user/PycharmProjects/lecture/Boundary_Project/test
#/home/user/PycharmProjects/lecture/Boundary_Project/imageset/new_original/B1
img_path = '/home/user/PycharmProjects/lecture/Boundary_Project/Untitled Folder' #Image folder Path
path_dir = os.listdir(img_path)
img_file_list_jpg = [file for file in path_dir if file.endswith(".jpg")] # Load img_file name with os
img_file_list_png = [file for file in path_dir if file.endswith(".png")]
img_file_list = img_file_list_jpg + img_file_list_png
load_img = natsort.natsorted(img_file_list,reverse=False)

while i <= len(load_img)-1:
    #imgaaa = cv2.resize(img, (224,224))
    
    #cv2.imshow('img', imgaaa)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()
    
    img_p = img_path + '/' + load_img[i]
    img_name = load_img[i]
    img = cv2.imread(img_p)
    
    save_path = '%s%s' %(img_path,'/crop')
    if not(os.path.isdir(os.path.join(save_path))):
        os.makedirs(os.path .join(save_path))
                
    Contour = Contours(img_name, img_p, save=True, show=False)
    Array = Seek_maxmin(Contour,i)
    rect_array = Countor_Extraction(Array, i, img, show=False)
    crop_img = Crop_img(i, img, rect_array, img_name, save_path=save_path)
    # Error_image_seek(f, img, load_img , Error, number, crop_img_shape=crop_img, percent=0.1)
    # print('i=',i)
    i = i+1

'''
for i in range(1,4):
    dirname2 = '%s%d' %('B_',i)
    dirname1 = img_path + '/' + dirname2
    for l in range(1,10):
        rotate_name2 = '%s%s%d' %(dirname2,'_',l)
        rotate_name1 = '%s%s%d' %(dirname1,'_',l)
        for v in range(1,9):
            path_name1 = '%s%s%d' %(rotate_name1,'_',v)
            path_name2 = '%s%s%s%s%d' %(img_path[:-1],'crop/',rotate_name2,'_',v)
            
            if not(os.path.isdir(os.path.join(path_name2))):
                os.makedirs(os.path.join(path_name2))

            path_dir = os.listdir(path_name1)
            img_file_list_jpg = [file for file in path_dir if file.endswith(".jpg")] # Load img_file name with os
            img_file_list_png = [file for file in path_dir if file.endswith(".png")]
            img_file_list = img_file_list_jpg + img_file_list_png
            img_file_list = natsort.natsorted(img_file_list,reverse=False)
            
            for f in range(len(img_file_list)):
                img_name = img_file_list[f]
                img_p = path_name1 + '/' + img_file_list[f]
                img = cv2.imread(img_p)
                imgaaa = cv2.resize(img, (224,224))
                    
                # cv2.imshow('img', imgaaa)
                # cv2.waitKey(0)
                # cv2.destroyAllWindows()
                
                Contour = Contours(img_name, img_p, save=False, show=False)
                Array = Seek_maxmin(Contour,f)
                rect_array = Countor_Extraction(Array, f, img, show=False)
                crop_img = Crop_img(f, img, rect_array, img_name, save_path=path_name2)
                #Error_image_seek(f, img, img_file_list, Error, number, crop_img_shape=crop_img, percent=0.1)
'''