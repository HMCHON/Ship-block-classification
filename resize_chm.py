import os
import cv2
import natsort

'''
i = 0

img_path = '/home/user/PycharmProjects/lecture/Boundary_Project/imageset/new_original_crop/B1_crop' #Image folder Path
path_dir = os.listdir(img_path)
img_file_list_jpg = [file for file in path_dir if file.endswith(".jpg")] # Load img_file name with os
img_file_list_png = [file for file in path_dir if file.endswith(".png")]
img_file_list = img_file_list_jpg + img_file_list_png
load_img = natsort.natsorted(img_file_list,reverse=False)

while i <= len(load_img)-1:
    img_p = img_path + '/' + load_img[i]
    img_name = load_img[i]
    img = cv2.imread(img_p)
    
    img224 = cv2.resize(img, (224,224))
    img299 = cv2.resize(img, (299,299))
    img331 = cv2.resize(img, (331,331))
    
    save_path_224 = '%s%s' %(img_path,'/224')
    if not(os.path.isdir(os.path.join(save_path_224))):
        os.makedirs(os.path.join(save_path_224))
        
    save_path_299 = '%s%s' %(img_path,'/299')
    if not(os.path.isdir(os.path.join(save_path_299))):
        os.makedirs(os.path.join(save_path_299))

    save_path_331 = '%s%s' %(img_path,'/331')
    if not(os.path.isdir(os.path.join(save_path_331))):
        os.makedirs(os.path.join(save_path_331))
    
    img_name_224 = '%s%s' % ('224_',img_name)
    img_name_299 = '%s%s' % ('299_',img_name)
    img_name_331 = '%s%s' % ('331_',img_name)
    
    cv2.imwrite(os.path.join(save_path_224 + '/' , img_name_224), img224)
    cv2.imwrite(os.path.join(save_path_299 + '/' , img_name_299), img299)
    cv2.imwrite(os.path.join(save_path_331 + '/' , img_name_331), img331)
    
    #cv2.imshow('img', imgaaa)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()
    i = i+1
'''
'''
i = 0

img_path = '/home/user/PycharmProjects/lecture/Boundary_Project/imageset/new_original_crop/B2_crop' #Image folder Path
path_dir = os.listdir(img_path)
img_file_list_jpg = [file for file in path_dir if file.endswith(".jpg")] # Load img_file name with os
img_file_list_png = [file for file in path_dir if file.endswith(".png")]
img_file_list = img_file_list_jpg + img_file_list_png
load_img = natsort.natsorted(img_file_list,reverse=False)

while i <= len(load_img)-1:
    img_p = img_path + '/' + load_img[i]
    img_name = load_img[i]
    img = cv2.imread(img_p)
    
    img224 = cv2.resize(img, (224,224))
    img299 = cv2.resize(img, (299,299))
    img331 = cv2.resize(img, (331,331))
    
    save_path_224 = '%s%s' %(img_path,'/224')
    if not(os.path.isdir(os.path.join(save_path_224))):
        os.makedirs(os.path.join(save_path_224))
        
    save_path_299 = '%s%s' %(img_path,'/299')
    if not(os.path.isdir(os.path.join(save_path_299))):
        os.makedirs(os.path.join(save_path_299))

    save_path_331 = '%s%s' %(img_path,'/331')
    if not(os.path.isdir(os.path.join(save_path_331))):
        os.makedirs(os.path.join(save_path_331))
    
    img_name_224 = '%s%s' % ('224_',img_name)
    img_name_299 = '%s%s' % ('299_',img_name)
    img_name_331 = '%s%s' % ('331_',img_name)
    
    cv2.imwrite(os.path.join(save_path_224 + '/' , img_name_224), img224)
    cv2.imwrite(os.path.join(save_path_299 + '/' , img_name_299), img299)
    cv2.imwrite(os.path.join(save_path_331 + '/' , img_name_331), img331)
    
    #cv2.imshow('img', imgaaa)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()
    i = i+1
'''
i = 0

img_path = '/home/user/PycharmProjects/lecture/Boundary_Project/imageset/new_original_2/500by300/500by300_8_2/test/B1' #Image folder Path
path_dir = os.listdir(img_path)
img_file_list_jpg = [file for file in path_dir if file.endswith(".jpg")] # Load img_file name with os
img_file_list_png = [file for file in path_dir if file.endswith(".png")]
img_file_list = img_file_list_jpg + img_file_list_png
load_img = natsort.natsorted(img_file_list,reverse=False)

while i <= len(load_img)-1:
    img_p = img_path + '/' + load_img[i]
    img_name = load_img[i]
    img = cv2.imread(img_p)
    '''
    img224 = cv2.resize(img, (224,224))
    img299 = cv2.resize(img, (299,299))
    img331 = cv2.resize(img, (331,331))
    
    save_path_224 = '%s%s' %(img_path,'/224')
    if not(os.path.isdir(os.path.join(save_path_224))):
        os.makedirs(os.path.join(save_path_224))
        
    save_path_299 = '%s%s' %(img_path,'/299')
    if not(os.path.isdir(os.path.join(save_path_299))):
        os.makedirs(os.path.join(save_path_299))
    '''
    img224 = cv2.resize(img, (224,224))
    
    save_path_224 = '%s%s' %(img_path,'/224')
    if not(os.path.isdir(os.path.join(save_path_224))):
        os.makedirs(os.path.join(save_path_224))
    
    # img_name_224 = '%s%s' % ('224_',img_name)
    # img_name_299 = '%s%s' % ('299_',img_name)
    img_name_224 = '%s%s' % ('224_',img_name)
    
    # cv2.imwrite(os.path.join(save_path_224 + '/' , img_name_224), img224)
    # cv2.imwrite(os.path.join(save_path_299 + '/' , img_name_299), img299)
    cv2.imwrite(os.path.join(save_path_224 + '/' , img_name_224), img224)
    
    #cv2.imshow('img', imgaaa)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()
    i = i+1
