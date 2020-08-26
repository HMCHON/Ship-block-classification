import random
import os
import glob
import shutil
import natsort

'''
# Load image sentence (list type)
folder_name = 'O'
img_path = os.path.join(os.getcwd()+'/Boundary_Project/imageset/original/' + folder_name) #Image folder Path
file_list = os.listdir(img_path) # Load file with os
img_file_list = [file for file in file_list if file.endswith(".png")] # Load img_file name with os
file_list = len(img_file_list)
path1 = os.path.isdir(os.path.join(os.getcwd()+'/imageset/original/' + folder_name) + '/' + After_fold_name)
path2 = os.path.join((os.getcwd()+'/imageset/original/' + folder_name) + '/' + After_fold_name)

## Step1 : Roll
for i in range(len(img_file_list)):

    image_name = img_file_list[i]
    
    if '1718' in image_name:
        image_name1 = int(image_name[-11:-8])
        num = 7
        for l in range(num):

            # degree 0~30
            if l*5-2 <=image_name1< (l+1)*5-2 :
                file_name = img_file_list[i]
                category = l+1
                category = str(category)
                After_fold_name = 'B_1_' + category
                
                if not(os.path.isdir(os.path.join(os.getcwd()+'/imageset/original/' + folder_name) + '/' + After_fold_name)):
                    os.makedirs(os.path.join((os.getcwd()+'/imageset/original/' + folder_name) + '/' + After_fold_name))
                
                src = img_path +'/'+file_name # Before
                dir = os.path.join(os.getcwd()+'/imageset/original/' + folder_name) + '/' + After_fold_name +'/'+ file_name # Before
                shutil.move(src, dir)
            
            
        for l in range(1,5):
                
            #degree 30~180
            if (l*30)+3 <= image_name1 < (l+1)*30+3 :
                category = l + num
                if l >= 4:
                    category = 9
                category = str(category)
                file_name = img_file_list[i]
                After_fold_name = 'B_1_' + category
                
                if not(os.path.isdir(os.path.join(os.getcwd()+'/imageset/original/' + folder_name) + '/' + After_fold_name)):
                    os.makedirs(os.path.join((os.getcwd()+'/imageset/original/' + folder_name) + '/' + After_fold_name))
                
                src = img_path +'/'+file_name # Before
                dir = os.path.join(os.getcwd()+'/imageset/original/' + folder_name) + '/' + After_fold_name +'/'+ file_name # Before
                shutil.move(src, dir)
    
            
    
    if '170A' in image_name:
        for l in range(1,9):
            number = '%s%d%s' %('(' , l , ')')
            
            if number in image_name:
                file_name = img_file_list[i]
                category = l
                category = str(category)
                After_fold_name = 'B_2_' + category
                
                if not(os.path.isdir(os.path.join(os.getcwd()+'/imageset/original/' + folder_name) + '/' + After_fold_name)):
                    os.makedirs(os.path.join((os.getcwd()+'/imageset/original/' + folder_name) + '/' + After_fold_name))
                
                src = img_path +'/'+file_name # Before
                dir = os.path.join(os.getcwd()+'/imageset/original/' + folder_name) + '/' + After_fold_name +'/'+ file_name # Before
                shutil.move(src, dir)
                
        for l in range(9,20):
            number = '%s%d%s' %('(' , l , ')')
            if number in image_name:
                if 9 <= l < 14:
                    file_name = img_file_list[i]
                    category = 8
                    category = str(category)
                    After_fold_name = 'B_2_' + category
                    
                    if not(os.path.isdir(os.path.join(os.getcwd()+'/imageset/original/' + folder_name) + '/' + After_fold_name)):
                        os.makedirs(os.path.join((os.getcwd()+'/imageset/original/' + folder_name) + '/' + After_fold_name))
                    
                    src = img_path +'/'+file_name # Before
                    dir = os.path.join(os.getcwd()+'/imageset/original/' + folder_name) + '/' + After_fold_name +'/'+ file_name # Before
                    shutil.move(src, dir)
                    
                else:
                    file_name = img_file_list[i]
                    category = 9
                    category = str(category)
                    After_fold_name = 'B_2_' + category
                    
                    if not(os.path.isdir(os.path.join(os.getcwd()+'/imageset/original/' + folder_name) + '/' + After_fold_name)):
                        os.makedirs(os.path.join((os.getcwd()+'/imageset/original/' + folder_name) + '/' + After_fold_name))
                    
                    src = img_path +'/'+file_name # Before
                    dir = os.path.join(os.getcwd()+'/imageset/original/' + folder_name) + '/' + After_fold_name +'/'+ file_name # Before
                    shutil.move(src, dir)
        
    if 'E811' in image_name:
        for l in range(1,9):
            number = '%s%d%s' %('(' , l , ')')
            
            if number in image_name:
                file_name = img_file_list[i]
                category = l
                category = str(category)
                After_fold_name = 'B_3_' + category
                
                if not(os.path.isdir(os.path.join(os.getcwd()+'/imageset/original/' + folder_name) + '/' + After_fold_name)):
                    os.makedirs(os.path.join((os.getcwd()+'/imageset/original/' + folder_name) + '/' + After_fold_name))
                
                src = img_path +'/'+file_name # Before
                dir = os.path.join(os.getcwd()+'/imageset/original/' + folder_name) + '/' + After_fold_name +'/'+ file_name # Before
                shutil.move(src, dir)
                
        for l in range(9,20):
            number = '%s%d%s' %('(' , l , ')')
            if number in image_name:
                if 9 <= l < 14:
                    file_name = img_file_list[i]
                    category = 8
                    category = str(category)
                    After_fold_name = 'B_3_' + category
                    
                    if not(os.path.isdir(os.path.join(os.getcwd()+'/imageset/original/' + folder_name) + '/' + After_fold_name)):
                        os.makedirs(os.path.join((os.getcwd()+'/imageset/original/' + folder_name) + '/' + After_fold_name))
                    
                    src = img_path +'/'+file_name # Before
                    dir = os.path.join(os.getcwd()+'//imageset/original/' + folder_name) + '/' + After_fold_name +'/'+ file_name # Before
                    shutil.move(src, dir)
                    
                else:
                    file_name = img_file_list[i]
                    category = 9
                    category = str(category)
                    After_fold_name = 'B_3_' + category
                    
                    if not(os.path.isdir(os.path.join(os.getcwd()+'/imageset/original/' + folder_name) + '/' + After_fold_name)):
                        os.makedirs(os.path.join((os.getcwd()+'/imageset/original/' + folder_name) + '/' + After_fold_name))
                    
                    src = img_path +'/'+file_name # Before
                    dir = os.path.join(os.getcwd()+'/imageset/original/' + folder_name) + '/' + After_fold_name +'/'+ file_name # Before
                    shutil.move(src, dir)


# Step 2: Yaw

path1 = '/home/user/PycharmProjects/lecture/imageset/original/O'
                    
for i in range(1,4):
    dirname = '%s%d' %('B_',i)
    dirname = path1 + '/' + dirname
    for l in range(1,10):
        roll_name = '%s%s%d' %(dirname,'_',l)
        roll_dir = os.listdir(roll_name)
        img_file_list_jpg = [file for file in roll_dir if file.endswith(".jpg")] # Load img_file name with os
        img_file_list_png = [file for file in roll_dir if file.endswith(".png")]
        img_file_list = img_file_list_jpg + img_file_list_png
        img_file_list = natsort.natsorted(img_file_list,reverse=False)
        
        if (1<=l<8):
            for v in range(0,8):
                load_img = img_file_list[(v*45):((v+1)*45)]
                After_fold_name = '%s%s%d%s%d%s%d' %(path1,'/B_',i,'_',l,'_',v+1) 
                if not(os.path.isdir(os.path.join(After_fold_name))):
                    os.makedirs(os.path.join(After_fold_name))
                for f in range(0,45):
                    image_name = load_img[f]
                    src = roll_name+'/'+image_name
                    dir = After_fold_name+'/'+image_name
                    shutil.copy(src, dir)
        if l >= 8:
            for v in range(0,8):
                load_img = img_file_list[(v*270):((v+1)*270)]
                After_fold_name = '%s%s%d%s%d%s%d' %(path1,'/B_',i,'_',l,'_',v+1) 
                if not(os.path.isdir(os.path.join(After_fold_name))):
                    os.makedirs(os.path.join(After_fold_name))
                for f in range(0,270):
                    image_name = load_img[f]
                    src = roll_name+'/'+image_name
                    dir = After_fold_name+'/'+image_name
                    shutil.copy(src, dir)
                print('ddd')

'''

# 8:2
img_path = '/home/user/PycharmProjects/lecture/imageset/original/crop' #Image folder Path

for i in range(1,4):
    dirname2 = '%s%d' %('B_',i)
    dirname1 = img_path + '/' + dirname2
    for l in range(1,10):
        rotate_name2 = '%s%s%d' %(dirname2,'_',l)
        rotate_name1 = '%s%s%d' %(dirname1,'_',l)
        for v in range(1,9):
            image_path = '%s%s%d' %(rotate_name1,'_',v)
            path_name_train = '%s%s%s%s%d' %(img_path,'/train/',rotate_name2,'_',v)
            path_name_test = '%s%s%s%s%d' %(img_path,'/test/',rotate_name2,'_',v)
            
            if not(os.path.isdir(os.path.join(path_name_train))):
                os.makedirs(os.path.join(path_name_train))
                
            if not(os.path.isdir(os.path.join(path_name_test))):
                os.makedirs(os.path.join(path_name_test))

            path_dir = os.listdir(image_path)
            img_file_list_jpg = [file for file in path_dir if file.endswith(".jpg")] # Load img_file name with os
            img_file_list_png = [file for file in path_dir if file.endswith(".png")]
            img_file_list = img_file_list_jpg + img_file_list_png
            img_file_list = natsort.natsorted(img_file_list,reverse=False)
            
            train_number = round(len(img_file_list) * 0.8)
            test_number = len(img_file_list) - train_number
            test_filename = random.sample(img_file_list,test_number)
            testll = len(test_filename)
            ii = 0
            while ii <= testll-1:
                file_name = test_filename[ii]
                dir = os.path.join(path_name_test +'/'+ file_name) # After
                src = os.path.join(image_path +'/'+ file_name) # Before
                shutil.move(src, dir)
                ii = ii+1








