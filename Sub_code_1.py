import random
import os
import glob
import shutil

# Load image sentence (list type)
folder_name = 'Original E811 (copy)'
img_path = os.path.join(os.getcwd()+'/Boundary_Project/imageset/original/' + folder_name) #Image folder Path
file_list = os.listdir(img_path) # Load file with os
img_file_list = [file for file in file_list if file.endswith(".jpg")] # Load img_file name with os
file_list = len(img_file_list)

for i in range(len(img_file_list)):

    image_name = img_file_list[i]
    
    if '1718' in image_name:
        image_name = int(image_name[-11:-8])
        num = 7
        for l in range(num):

            # degree 0~30
            if l*5-2 <=image_name< (l+1)*5-2 :
                file_name = img_file_list[i]
                category = l+1
                category = str(category)
                After_fold_name = 'B_1_' + category
                
                if not(os.path.isdir(os.path.join(os.getcwd()+'/Boundary_Project/imageset/original/' + folder_name) + '/' + After_fold_name)):
                    os.makedirs(os.path.join((os.getcwd()+'/Boundary_Project/imageset/original/' + folder_name) + '/' + After_fold_name))
                
                src = img_path +'/'+file_name # Before
                dir = os.path.join(os.getcwd()+'/Boundary_Project/imageset/original/' + folder_name) + '/' + After_fold_name +'/'+ file_name # Before
                shutil.move(src, dir)
                print(i)
            
            
        for l in range(1,5):
                
            #degree 30~180
            if (l*30)+3 <= image_name < (l+1)*30+3 :
                category = l + num
                if l == 4:
                    category = 9
                category = str(category)
                file_name = img_file_list[i]
                After_fold_name = 'B_1_' + category
                
                if not(os.path.isdir(os.path.join(os.getcwd()+'/Boundary_Project/imageset/original/' + folder_name) + '/' + After_fold_name)):
                    os.makedirs(os.path.join((os.getcwd()+'/Boundary_Project/imageset/original/' + folder_name) + '/' + After_fold_name))
                
                src = img_path +'/'+file_name # Before
                dir = os.path.join(os.getcwd()+'/Boundary_Project/imageset/original/' + folder_name) + '/' + After_fold_name +'/'+ file_name # Before
                shutil.move(src, dir)
                print(i)
    
            
    
    if '170A' in image_name:
        for l in range(8):
            number = '%s%d%s' %('(' , l , ')')
            
            if number in image_name:
                file_name = img_file_list[i]
                category = l+1
                category = str(category)
                After_fold_name = 'B_2_' + category
                
                if not(os.path.isdir(os.path.join(os.getcwd()+'/Boundary_Project/imageset/original/' + folder_name) + '/' + After_fold_name)):
                    os.makedirs(os.path.join((os.getcwd()+'/Boundary_Project/imageset/original/' + folder_name) + '/' + After_fold_name))
                
                src = img_path +'/'+file_name # Before
                dir = os.path.join(os.getcwd()+'/Boundary_Project/imageset/original/' + folder_name) + '/' + After_fold_name +'/'+ file_name # Before
                shutil.move(src, dir)
                
        for l in range(8,20):
            number = '%s%d%s' %('(' , l , ')')
            if number in image_name:
                if 8 <= l < 14:
                    file_name = img_file_list[i]
                    category = 8
                    category = str(category)
                    After_fold_name = 'B_2_' + category
                    
                    if not(os.path.isdir(os.path.join(os.getcwd()+'/Boundary_Project/imageset/original/' + folder_name) + '/' + After_fold_name)):
                        os.makedirs(os.path.join((os.getcwd()+'/Boundary_Project/imageset/original/' + folder_name) + '/' + After_fold_name))
                    
                    src = img_path +'/'+file_name # Before
                    dir = os.path.join(os.getcwd()+'/Boundary_Project/imageset/original/' + folder_name) + '/' + After_fold_name +'/'+ file_name # Before
                    print('hi', file_name)
                    shutil.move(src, dir)
                    
                else:
                    file_name = img_file_list[i]
                    category = 9
                    category = str(category)
                    After_fold_name = 'B_2_' + category
                    
                    if not(os.path.isdir(os.path.join(os.getcwd()+'/Boundary_Project/imageset/original/' + folder_name) + '/' + After_fold_name)):
                        os.makedirs(os.path.join((os.getcwd()+'/Boundary_Project/imageset/original/' + folder_name) + '/' + After_fold_name))
                    
                    src = img_path +'/'+file_name # Before
                    dir = os.path.join(os.getcwd()+'/Boundary_Project/imageset/original/' + folder_name) + '/' + After_fold_name +'/'+ file_name # Before
                    shutil.move(src, dir)
                    print('hi', file_name)
        
    if 'E811' in image_name:
        for l in range(8):
            number = '%s%d%s' %('(' , l , ')')
            
            if number in image_name:
                file_name = img_file_list[i]
                category = l+1
                category = str(category)
                After_fold_name = 'B_3_' + category
                
                if not(os.path.isdir(os.path.join(os.getcwd()+'/Boundary_Project/imageset/original/' + folder_name) + '/' + After_fold_name)):
                    os.makedirs(os.path.join((os.getcwd()+'/Boundary_Project/imageset/original/' + folder_name) + '/' + After_fold_name))
                
                src = img_path +'/'+file_name # Before
                dir = os.path.join(os.getcwd()+'/Boundary_Project/imageset/original/' + folder_name) + '/' + After_fold_name +'/'+ file_name # Before
                shutil.move(src, dir)
                
        for l in range(8,20):
            number = '%s%d%s' %('(' , l , ')')
            if number in image_name:
                if 8 <= l < 14:
                    file_name = img_file_list[i]
                    category = 8
                    category = str(category)
                    After_fold_name = 'B_3_' + category
                    
                    if not(os.path.isdir(os.path.join(os.getcwd()+'/Boundary_Project/imageset/original/' + folder_name) + '/' + After_fold_name)):
                        os.makedirs(os.path.join((os.getcwd()+'/Boundary_Project/imageset/original/' + folder_name) + '/' + After_fold_name))
                    
                    src = img_path +'/'+file_name # Before
                    dir = os.path.join(os.getcwd()+'/Boundary_Project/imageset/original/' + folder_name) + '/' + After_fold_name +'/'+ file_name # Before
                    print('hi', file_name)
                    shutil.move(src, dir)
                    
                else:
                    file_name = img_file_list[i]
                    category = 9
                    category = str(category)
                    After_fold_name = 'B_3_' + category
                    
                    if not(os.path.isdir(os.path.join(os.getcwd()+'/Boundary_Project/imageset/original/' + folder_name) + '/' + After_fold_name)):
                        os.makedirs(os.path.join((os.getcwd()+'/Boundary_Project/imageset/original/' + folder_name) + '/' + After_fold_name))
                    
                    src = img_path +'/'+file_name # Before
                    dir = os.path.join(os.getcwd()+'/Boundary_Project/imageset/original/' + folder_name) + '/' + After_fold_name +'/'+ file_name # Before
                    shutil.move(src, dir)
                    print('hi', file_name)
