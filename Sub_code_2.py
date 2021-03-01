# Step 2: Yaw

# Load image sentence (list type)
import os
import natsort
import shutil
         
path1 = '/home/user/PycharmProjects/lecture/imageset/original/O'
                    
for i in range(1,4):
    dirname = '%s%d' %('B_',i)
    dirname = path1 + '/' + dirname
    for l in range(1,9):
        roll_name = '%s%s%d' %(dirname,'_',l)
        roll_dir = os.listdir(roll_name)
        img_file_list_jpg = [file for file in roll_dir if file.endswith(".jpg")] # Load img_file name with os
        img_file_list_png = [file for file in roll_dir if file.endswith(".png")]
        img_file_list = img_file_list_jpg + img_file_list_png
        img_file_list = natsort.natsorted(img_file_list,reverse=False)
        
        for v in range(0,8):
            if v >= 8:
                break
            load_img = img_file_list[(v*45):((v+1)*45)]
            After_fold_name = '%s%s%d%s%d%s%d' %(path1,'/B_',i,'_',l,'_',v+1) 
            if not(os.path.isdir(os.path.join(After_fold_name))):
                os.makedirs(os.path.join(After_fold_name))
            for f in range(0,45):
                image_name = load_img[f]
                src = roll_name+'/'+image_name
                dir = After_fold_name+'/'+image_name
                shutil.copy(src, dir)
