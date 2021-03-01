from sklearn.metrics import confusion_matrix
from keras.optimizers import RMSprop
from keras.models import load_model
from pandas import DataFrame
import natsort
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import pandas as pd
import numpy as np
import os
from keras import backend as K
import cv2

plt.rcParams["figure.figsize"] = (20,3)
path = '/home/user/PycharmProjects/batang.ttc'
fontprop = fm.FontProperties(fname=path, size=18)

def plot_image(predictions_array, true_label, plot_image, class_name):
    plt.grid(False)
    plt.xticks([])
    plt.yticks([])
    
    plt.imshow(plot_image, cmap = 'gray')
    
    predicted_label = np.argmax(predictions_array)
    if predicted_label == true_label:
        color = 'blue'
    else:
        color = 'red'
    
    plt.xlabel("{} {:2.0f}% ({})".format(class_name[predicted_label],
               100*np.max(predictions_array),
               class_name[true_label]),
               color=color,
               fontproperties=fontprop)
    
def plot_value_array(predictions_array, true_label, class_name):
    plt.grid(False)
    plt.xticks(range(len(class_name)), class_name,  fontproperties=fontprop)
    plt.yticks([])
    thisplot = plt.bar(range(len(class_name)), predictions_array, color='#777777')
    plt.ylim([0,1])
    predicted_label=np.argmax(predictions_array)
    
    thisplot[predicted_label].set_color('red')
    thisplot[true_label].set_color('blue')

def draw_plot(result, class_name,csv_name):
    data = {'class':class_name,
    'TP':result[0],
    'TN':result[1],
    'FP':result[2],
    'FN':result[3],
    'Precision':result[4],
    'Recall':result[5],
    'Accuracy':result[6],
    'Avg_F1-Score':result[7]}
    frame = DataFrame(data)
    #print('-'*80)
    #print(frame)
    
    df = pd.DataFrame(data)
    df.to_csv(csv_name)
    
def draw_matrix(confusion_matrix, matrix_name):
    confusion_matrix = np.array(confusion_matrix)
    np.save(matrix_name, confusion_matrix)
    '''
    data2 = {'class':class_name,
            'B1':confusion_matrix[0][],
            'B2': ,
            'B3': }
    frame = DataFrame(data2)
    #print('-'*80)
    #print(frame)
    
    df = pd.DataFrame(data2)
    df.to_csv(matrix_name)
    '''
def save_measure_performance(confusion_matrix, class_name, csv_name, matrix_name):
    confusion_matrix = confusion_matrix # [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    
    # Calcultate Accurcy ------------------------------------------------------
    diag = np.diag(confusion_matrix,k=0) # [[1, 2, 3], [4, 5, 6], [7, 8, 9]] -> [1, 5, 8](array)
    sum_all = confusion_matrix.sum() #  [[1, 2, 3], [4, 5, 6], [7, 8, 9]] -> 45(int64)
    sum_diag = diag.sum() # [1, 5, 8] -> 14(int64)
    Accuracy = sum_diag/sum_all
    
    # TP, TN, FP, FN ----------------------------------------------------------
    class_len = len(class_name) # 3(int)
    
    ## TP(True_Positive)
    i = 0
    xx_TP = []
    while i <= class_len - 1:
        x_TP = confusion_matrix[i,i]
        xx_TP.append(x_TP)
        i = i+1
    TP = xx_TP
    
    ## TN(True_Nagetive)
    i = 0
    j = 0
    ji = []
    ij = []
    xx_TN = []
    while i <= class_len -1:
        j = 0
        ji = []
        while j <= class_len -1:
            x_ji = confusion_matrix[j, i]
            ji.append(x_ji)
            j = j+1
        
        j = 0
        ij = []
        while j <= class_len - 1:
            x_ij = confusion_matrix[i, j]
            ij.append(x_ij)
            j = j+1
            
        x_TN = sum_all - sum(ji) - sum(ij) + confusion_matrix[i,i]
        xx_TN.append(x_TN)
        i = i+1
    TN = xx_TN
    
    ## FP(False_Positive)
    i = 0
    xx_FP = []
    while i <= class_len - 1:
        
        j = 0
        ji = []
        while j <= class_len - 1:
            x_ji = confusion_matrix[j, i]
            ji.append(x_ji)
            j = j+1

        x_FP = sum(ji) - confusion_matrix[i,i]
        xx_FP.append(x_FP)
        i = i+1
    FP = xx_FP
    
    ##FN(False_Nagative)
    i = 0
    xx_FN = []
    while i <= class_len -1:
        
        j = 0
        ij = []
        while j <= class_len - 1:
            x_ij = confusion_matrix[i, j]
            ij.append(x_ij)
            j = j+1

        x_FN = sum(ij) - confusion_matrix[i,i]
        xx_FN.append(x_FN)
        i = i+1
    FN = xx_FN
    
    
    ##Precision----------------------------------------------------------------
    i = 0
    precision = []
    while i <= class_len -1:
        x_precision = TP[i]/(TP[i]+FP[i])
        precision.append(x_precision)
        i = i+1
    
    i = 0
    recall = []
    while i <= class_len -1:
        x_recall = TP[i]/(TP[i]+FN[i])
        recall.append(x_recall)
        i = i+1
    
    Avg_F1_score = 2*(((sum(precision)/class_len)*(sum(recall)/class_len)) / ((sum(precision)/class_len)+(sum(recall)/class_len)))
    
    result = [TP,TN,FP,FN,precision,recall,round(Accuracy,4),round(Avg_F1_score,4)]
    
    draw_plot(result=result,class_name=class_name,csv_name=csv_name)
    draw_matrix(confusion_matrix=confusion_matrix, matrix_name=matrix_name)
    
    return result


def Grad__CAM(pred_Y, true_Y, grad_image, model, class_name, fig_save_path, tlayer, l):
    
    
    rimage_list = np.expand_dims(grad_image,axis=0) # (1, 224, 224, 3)
    model_input = model.input
    y_c = model.outputs[0].op.inputs[0][0, pred_Y]
    
    
    A_k = model.get_layer(tlayer).output
    get_output = K.function([model_input], [A_k, K.gradients(y_c, A_k)[0]])
    [conv_output, grad_val] = get_output(rimage_list)        
    conv_output = conv_output[0]
    grad_val = grad_val[0]
    weights = np.mean(grad_val, axis=(0, 1))
    grad_cam = np.zeros(dtype=np.float32, shape=conv_output.shape[0:2])
    for k, w in enumerate(weights):
        grad_cam += w * conv_output[:, :, k]
    grad_cam = np.maximum(grad_cam, 0)
            
    iimg = grad_image
    cam1 = cv2.resize(grad_cam, (iimg.shape[1], iimg.shape[0]))
    plt.figure(0)
    plt.imshow(iimg)
    plt.imshow(cam1, cmap = 'jet', alpha=0.4)
    plt.axis('off')    
    
    fig_name = '%s%d%s' % ('IMG_', l, '_Grad_CAM.png')
    save_path = '%s%s%s' % (fig_save_path,'/',fig_name)
    plt.savefig(save_path)
    plt.close('all')
    plt.clf()

def Prediction(model, class_name, Grad_CAM = False):
    npy_file_path = './'
    npy_file_path_list = os.listdir(npy_file_path)
    npy_X_file_list = [file for file in npy_file_path_list if file.endswith("X.npy")]
    npy_X_file_list = natsort.natsorted(npy_X_file_list, reverse=False) #EX. ['thr_76_size_224_X.npy',...,'~X.npy']
    npy_y_file_list = [file for file in npy_file_path_list if file.endswith("y.npy")]
    npy_y_file_list = natsort.natsorted(npy_y_file_list, reverse=False) #EX. ['thr_76_size_224_y.npy',...,'~y.npy']
    
    model_name = model
    
    model_folders_path ='%s%s' % ('./',model) #EX. ./model
    model_folders_list = os.listdir(model_folders_path)
    model_folders_list = natsort.natsorted(model_folders_list, reverse = False) #EX.['thr_75_densenet-201',...,'thr_80_densenet-201']
    hdf5_name_list = [file for file in model_folders_list if file.endswith(".hdf5")]
    hdf5_name_list = natsort.natsorted(hdf5_name_list) #EX. ['01_thr_75.hdf5','02_thr_75.hdf5',...,'05_thr_75.hdf5']
    for f in range(len(hdf5_name_list)):
        target_hdf5 = '%s%s%s' % ('model','/',hdf5_name_list[f]) #EX. ./densenet-201/thr_75_densenet-201/01_thr_75.hdf5
        model = load_model(target_hdf5)
        model.compile(loss='categorical_crossentropy',optimizer=RMSprop(lr = 2e-5), metrics=['acc'])
        for g in range(len(npy_X_file_list)):
            X_npy_path = '%s%s' % ('./',npy_X_file_list[g]) #EX. ./prediction/npy/~X.npy
            y_npy_path = '%s%s' % ('./',npy_y_file_list[g]) #EX. ./prediction/npy/~y.npy
            images = np.load(X_npy_path,allow_pickle=True) # shape : (120, 224, 224, 3)
            labels = np.load(y_npy_path,allow_pickle=True) # shape : (240,1)
            
            rimages = []
            image_list = []
            img = []
            for l in range(images.shape[0]):
                imagek=images[l] # (224, 224, 3)
                image_list.append(imagek)
                imagek=np.expand_dims(imagek,axis=0) # (1, 224, 224, 3)
                rimages.append(imagek) # list (240)
            img = np.array(rimages) # (240, 1, 224, 224, 3)
            
            pred_Y = []
            for l in range(images.shape[0]):
                predict = model.predict(img[l])
                predictions_array = np.squeeze(predict) # [percent'1' percent'2' ... percent'n']
                maxpredict = np.argmax(predict)
                pred_Y.append(maxpredict)
                
                plt.figure(figsize=(6, 3))
                plt.subplot(1, 2, 1)
                # def plot_image(i, predictions_array, true_label, plot_image):
                plot_image(predictions_array, labels[l], images[l], class_name = class_name)
                plt.subplot(1, 2, 2)
                # def plot_value_array(i, predictions_array, true_label):
                plot_value_array(predictions_array, labels[l], class_name = class_name)
                
                npy_name = ((npy_X_file_list[g])[:-6])
                hdf5_name = ((hdf5_name_list[f])[:-5])
                fig_name = '%s%s%s%s%s%d%s' % ('pred_',npy_name,'_epoch_',hdf5_name,'_',l,'.png') #EX. pred_thr_76_size_224_epoch_01_thr_75_0.png
                fig_save_path = '%s%s%d%s%s' % (model_folder_dir,'/epoch_',f+1,'/',npy_name) #EX. ./densenet-201/thr_75_densenet-201/epoch_1/thr_76_size_224
                if not(os.path.isdir(os.path.join(fig_save_path))):
                    os.makedirs(os.path.join(fig_save_path))
                fig_save_dir = '%s%s%s' % (fig_save_path,'/',fig_name) #EX. ./densenet-201/thr_75_densenet-201/epoch_1/thr_76_size_224/pred_thr_76_size_224_epoch_01_thr_75_0.png
                plt.savefig(fig_save_dir)
                plt.close('all')
                                
                if Grad_CAM == True:
                    if model_name == 'vgg-19':
                        tlayer = 'block5_pool'
                    if model_name == 'resnet-152v2':
                        tlayer = 'conv5_block3_3_conv'
                    if model_name == 'densenet-201':
                        tlayer = 'relu'
                        
                    Grad__CAM(true_Y = labels[l], 
                                pred_Y = maxpredict, 
                                grad_image = image_list[l], 
                                model = model, 
                                class_name = class_name,
                                fig_save_path = fig_save_path,
                                tlayer = tlayer,
                                l=l)
            
            pred_Y = np.array(pred_Y)
            true_Y = np.array(labels) # true_Y = [0 0 0 ... 3 3 3]
            Confusion_matrix = confusion_matrix(true_Y, pred_Y)
            csv_name = '%s%s%s%s%s' % ('pred_',npy_name,'_epoch_',hdf5_name,'.csv') #EX. pred_thr_76_size_224_epoch_01_thr_75.csv
            matrix_name = '%s%s%s%s%s' % ('pred_', npy_name, '_epoch_', hdf5_name, '_confusion_matrix.npy')
            csv_name_path = '%s%s%d%s%s%s%s' % (model_folder_dir,'/epoch_',f+1,'/',npy_name,'/',csv_name) #EX. ./densenet-201/thr_75_densenet-201/epoch_1/thr_76_size_224/pred_thr_76_size_224_epoch_01_thr_75.csv
            matrix_name_path = '%s%s%d%s%s%s%s' % (model_folder_dir,'/epoch_',f+1,'/',npy_name,'/',matrix_name)
            save_measure_performance(Confusion_matrix, class_name=class_name, csv_name = csv_name_path, matrix_name = matrix_name_path)

class_name = ['B1','B2','B3']
Prediction(model='model',class_name=class_name)
