
from keras.models import load_model
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import glob
import os

os.environ["CUDA_VISIBLE_DEVICES"]='0,2'
########################################################################################
    ##################################################################################
    ## This definite is about loading model and loading image npy file              ##
    ## from current directory                                                       ##
    ## [parameter]                                                                  ##
    ##  i :                                                                         ##
    ##  predictions_array :                                                         ##
    ##  true_label :                                                                ##
    ##  plot_image :                                                                ##
    ##  class_name :                                                                ##
    ##                                                                              ##
    ## [return]                                                                     ##
    ##   None                                                                       ##
    ##################################################################################

def plot_image(i, predictions_array, true_label, plot_image, class_name):
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
    color=color)
    
########################################################################################
    ##################################################################################
    ## This definite is about loading model and loading image npy file              ##
    ## from current directory                                                       ##
    ## [parameter]                                                                  ##
    ##  i :                                                                         ##
    ##  predictions_array :                                                         ##
    ##  true_label :                                                                ##
    ##  class_name :                                                                ##
    ##                                                                              ##
    ## [return]                                                                     ##
    ##   None                                                                       ##
    ##################################################################################
    
def plot_value_array(i, predictions_array, true_label, class_name):
    plt.grid(False)
    plt.xticks(range(len(class_name)), class_name)
    plt.yticks([])
    thisplot = plt.bar(range(len(class_name)), predictions_array, color='#777777')
    plt.ylim([0,1])
    predicted_label=np.argmax(predictions_array)
    
    thisplot[predicted_label].set_color('red')
    thisplot[true_label].set_color('blue')
########################################################################################
    ##################################################################################
    ## This definite is about loading model and loading image npy file              ##
    ## from current directory                                                       ##
    ## [parameter]                                                                  ##
    ##  i :                                                                         ##
    ##  predictions_array :                                                         ##
    ##  true_label :                                                                ##
    ##  class_name :                                                                ##
    ##                                                                              ##
    ## [return]                                                                     ##
    ##   None                                                                       ##
    ##################################################################################

from pandas import Series, DataFrame

def draw_plot(result, class_name, model_name):
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
    print('-'*80)
    print(frame)
    
    df = pd.DataFrame(data)
    df.to_csv('%s.csv' % model_name[0:-5])
    
def draw_matrix(confusion_matrix, matrix_name):
    confusion_matrix = np.array(confusion_matrix)
    np.save(matrix_name, confusion_matrix)

########################################################################################
    ##################################################################################
    ## This definite is about loading model and loading image npy file              ##
    ## from current directory                                                       ##
    ## [parameter]                                                                  ##
    ##  i :                                                                         ##
    ##  predictions_array :                                                         ##
    ##  true_label :                                                                ##
    ##  class_name :                                                                ##
    ##                                                                              ##
    ## [return]                                                                     ##
    ##   multi_class_matrix                                                         ##
    ##################################################################################
    
def save_measure_performance(confusion_matrix, class_name, model_name):
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
    
    draw_plot(result = result, class_name = class_name, model_name = model_name)
    
    return result
########################################################################################
    ##################################################################################
    ## This definite is about loading model and loading image npy file              ##
    ## from current directory                                                       ##
    ## [parameter]                                                                  ##
    ##  imave_size :                                                                ##
    ##  class_name : class_name = ['class1', 'class2', ... , 'classn']              ##
    ##                                                                              ##
    ## [return]                                                                     ##
    ##   None                                                                       ##
    ##################################################################################
import keras
from keras.applications.vgg19 import VGG19
from keras.applications.resnet_v2 import ResNet152V2
from keras.applications.densenet import DenseNet201
import keras.backend as K

import tensorflow as tf
from tensorflow.python.framework import ops

import cv2

def deprocess_image(x):
    x = np.squeeze(x)
    x -= x.mean()
    x /= (x.std() + 1e-5)
    x *= 0.1
    
    x += 0.5
    x = np.clip(x, 0, 1)
    
    x *= 255
    x = np.clip(x, 0, 255).astype('uint8')
    return x
def register_gradient():
    if "GuidedBackProp" not in ops._gradient_registry._registry:
        @ops.RegisterGradient("GuidedBackProp")
        def _GuidedBackProp(op, grad):
            dtype = op.inputs[0].dtype
            return grad * tf.cast(grad > 0., dtype) * tf.cast(op.inputs[0] > 0., dtype)

#####Problem here###########
def modify_backprop(model, name):
    g = tf.get_default_graph()
    with g.gradient_override_map({'Relu': name}):

        # get layers that have an activation
        layer_dict = [layer for layer in model.layers[1:]
                      if hasattr(layer, 'activation')]

        # replace relu activation
        for layer in layer_dict:
            if layer.activation == keras.activations.relu:
                layer.activation = tf.nn.relu

        # re-instanciate a new model
        new_model = ResNet152V2(weights='imagenet')
    return new_model


def guided_backpropagation(img_tensor, model, activation_layer):
    model_input = model.input
    layer_output = model.get_layer(activation_layer).output

    # one_output = layer_output[:, :, :, 256]
    max_output = K.max(layer_output, axis=3)

    get_output = K.function([model_input], [K.gradients(max_output, model_input)[0]])
    # get_output = K.function([model_input], [K.gradients(one_output, model_input)[0]])
    saliency = get_output([img_tensor])

    return saliency[0]

def keras_guided_Grad_CAM(image, guided_model, model_name, layer):
    img = image
    img = np.expand_dims(img,axis=0)
    gradient_image = guided_backpropagation(img, guided_model, layer)
    return gradient_image
        
        
        
        
########################################################################################
    ##################################################################################
    ## This definite is about loading model and loading image npy file              ##
    ## from current directory                                                       ##
    ## [parameter]                                                                  ##
    ##  imave_size :                                                                ##
    ##  class_name : class_name = ['class1', 'class2', ... , 'classn']              ##
    ##                                                                              ##
    ## [return]                                                                     ##
    ##   None                                                                       ##
    ##################################################################################
from keras import backend as K
import cv2

def Grad__CAM(guided_Grad_CAM, guided_model, pred_Y, true_Y, image_list, model, class_name, model_name, first_layer, second_layer, third_layer):
    
    
    #VGG :
    #Inception : 'conv2d_92' 'conv2d_93' 'conv2d_94'
    #Dense :
    #Res : conv5_block3_1_conv conv5_block3_2_conv conv5_block3_3_conv 
    #NAS :
    
    iii = 0
    l = 9
         # for true_Y predictions
    ii = [193,152,198,332,263,387,557,576,525]
    #ii = [18,156,178,207,246,285,400,413,415]
    #ii = [26,27,113,114,491,499,541,542]
    while iii <= l-1:
        i = ii[iii]
        rimage_list = np.expand_dims(image_list[i],axis=0) # (1, 224, 224, 3)
        model_input = model.input
        y_c = model.outputs[0].op.inputs[0][0, pred_Y[i]]
        
        A_k = model.get_layer(first_layer).output
        get_output = K.function([model_input], [A_k, K.gradients(y_c, A_k)[0]])
        [conv_output, grad_val] = get_output(rimage_list)        
        conv_output = conv_output[0]
        grad_val = grad_val[0]
        weights = np.mean(grad_val, axis=(0, 1))
        grad_cam = np.zeros(dtype=np.float32, shape=conv_output.shape[0:2])
        for k, w in enumerate(weights):
            grad_cam += w * conv_output[:, :, k]
        grad_cam1 = np.maximum(grad_cam, 0)
        
        '''
        A_k = model.get_layer(second_layer).output
        get_output = K.function([model_input], [A_k, K.gradients(y_c, A_k)[0]])
        [conv_output, grad_val] = get_output(rimage_list)        
        conv_output = conv_output[0]
        grad_val = grad_val[0]
        weights = np.mean(grad_val, axis=(0, 1))
        grad_cam = np.zeros(dtype=np.float32, shape=conv_output.shape[0:2])
        for k, w in enumerate(weights):
            grad_cam += w * conv_output[:, :, k]
        grad_cam2 = np.maximum(grad_cam, 0)
        
        A_k = model.get_layer(third_layer).output
        get_output = K.function([model_input], [A_k, K.gradients(y_c, A_k)[0]])
        [conv_output, grad_val] = get_output(rimage_list)        
        conv_output = conv_output[0]
        grad_val = grad_val[0]
        weights = np.mean(grad_val, axis=(0, 1))
        grad_cam = np.zeros(dtype=np.float32, shape=conv_output.shape[0:2])
        for k, w in enumerate(weights):
            grad_cam += w * conv_output[:, :, k]
        grad_cam3 = np.maximum(grad_cam, 0)
        '''
        
       
        iimg = image_list[i]
        # cam1 = cv2.resize(grad_cam1, (iimg.shape[1], iimg.shape[0]))
        grad_cam1 = cv2.resize(grad_cam1, (iimg.shape[1], iimg.shape[0]))
        #grad_cam2 = cv2.resize(grad_cam2, (iimg.shape[1], iimg.shape[0]))
        #grad_cam3 = cv2.resize(grad_cam3, (iimg.shape[1], iimg.shape[0]))
        
        if guided_Grad_CAM == True:
            iimg = image_list[i]
            gradient1 = keras_guided_Grad_CAM(iimg, guided_model, model_name, first_layer)
            #gradient2 = keras_guided_Grad_CAM(iimg, guided_model, model_name, second_layer)
            #gradient3 = keras_guided_Grad_CAM(iimg, guided_model, model_name, third_layer)
            guided_gradcam1 = gradient1 * grad_cam1[..., np.newaxis]
            #guided_gradcam2 = gradient2 * grad_cam2[..., np.newaxis]
            #guided_gradcam3 = gradient3 * grad_cam3[..., np.newaxis]
            '''
            plt.figure(figsize=(15, 9))
            plt.xticks([])
            plt.yticks([])
        
            plt.subplot(3,4,1)
            plt.imshow(iimg)
            plt.title('Input Image')
            plt.axis('off')    
            
            plt.subplot(3,4,2)
            plt.imshow(grad_cam1)
            plt.title(first_layer + ' heatmap')
            plt.axis('off')    
            plt.subplot(3,4,6)
            plt.imshow(iimg)
            plt.imshow(grad_cam1, cmap = 'jet', alpha = 0.5)
            plt.title(first_layer + '   Grad_CAM')
            plt.axis('off')    
            plt.subplot(3,4,10)
            plt.imshow(deprocess_image(guided_gradcam1))
            plt.title(first_layer + '   guided_Grad_CAM')
            plt.axis('off')    
            
            
            plt.subplot(3,4,3)
            plt.imshow(grad_cam2)
            plt.title(second_layer + ' heatmap')
            plt.axis('off')    
            plt.subplot(3,4,7)
            plt.imshow(iimg)
            plt.imshow(grad_cam2, cmap = 'jet',  alpha = 0.5)
            plt.title(second_layer)
            plt.axis('off')    
            plt.subplot(3,4,11)
            plt.imshow(deprocess_image(guided_gradcam2))
            plt.title(second_layer + '   guided_Grad_CAM')
            plt.axis('off')    
            
            plt.subplot(3,4,4)
            plt.imshow(grad_cam3)
            plt.title(third_layer + ' heatmap')
            plt.axis('off')    
            plt.subplot(3,4,8)
            plt.imshow(iimg)
            plt.imshow(grad_cam3, cmap = 'jet',  alpha = 0.5)
            plt.title(third_layer)    
            plt.axis('off')    
            plt.subplot(3,4,12)
            plt.imshow(deprocess_image(guided_gradcam3))
            plt.title(third_layer + '   guided_Grad_CAM')
            plt.axis('off')    
            
            plt.suptitle('Pred_Class : ' + '{}'.format(class_name[pred_Y[i]]) + '     True_Class : ' + '{}'.format(class_name[true_Y[i]]))
            '''
            plt.figure(figsize=(6, 3))
            plt.xticks([])
            plt.yticks([])
            plt.axis('off')
            plt.imshow(iimg)
            plt.imshow(deprocess_image(guided_gradcam1))
            fig_name = '%s%s%d%s' % (model_name, 'IMG_', i, 'GRAD_CAM.png')
            plt.savefig(fig_name)
            # plt.show()
            plt.close('all')
            plt.clf()
            
        else:
            cam1 = cv2.resize(grad_cam1, (iimg.shape[1], iimg.shape[0]))
            #grad_cam2 = cv2.resize(grad_cam2, (iimg.shape[1], iimg.shape[0]))
            #grad_cam3 = cv2.resize(grad_cam3, (iimg.shape[1], iimg.shape[0]))
            plt.figure(0)
            plt.imshow(iimg)
            plt.imshow(cam1, cmap = 'jet', alpha=0.4)
            plt.axis('off')    
            
            fig_name = '%s%d%s' % ('IMG_', i, '_Grad_CAM.png')
            plt.savefig(fig_name)
            # plt.show()
            plt.close('all')
            plt.clf()
        
        iii = iii+1
       
########################################################################################
    ##################################################################################
    ## This definite is about loading model and loading image npy file              ##
    ## from current directory                                                       ##
    ## [parameter]                                                                  ##
    ##  imave_size :                                                                ##
    ##  class_name : class_name = ['class1', 'class2', ... , 'classn']              ##
    ##                                                                              ##
    ## [return]                                                                     ##
    ##   None                                                                       ##
    ##################################################################################
from keras.models import Model
from keras.layers import UpSampling2D, Conv2D

def keras_CAM(pred_Y, true_Y, class_name, image_list, last_conv_layer, pred_layer, model):
    
    #VGG :
    #Inception : 'conv2d_92' 'conv2d_93' 'conv2d_94'
    #Dense :
    #Res : conv5_block3_1_conv conv5_block3_2_conv conv5_block3_3_conv 
    #NAS :
    
    i = 0
    l = len(true_Y)
    N_CLASSES = len(class_name)
         # for true_Y predictions
         
    while i <= l-1:
        
       
        rimage_list = np.expand_dims(image_list[i],axis=0) # (1, 224, 224, 3)
        
        '''
        #cmodel = model(input_shape=(len(image_list[0]), len(image_list[1]), 3))
        cmodel = model
        
        final_params = cmodel.get_layer(pred_layer).get_weights()
        final_params = (final_params[0].reshape(1, 1, -1, N_CLASSES), final_params[1])
        
        last_conv_output = cmodel.get_layer(last_conv_layer).output
        x = UpSampling2D(size=(32, 32), interpolation='bilinear')(last_conv_output)
        x = Conv2D(filters=N_CLASSES, kernel_size=(1, 1), name='predictions_2')(x)        
        
        cam_model = Model(inputs=cmodel.input, outputs=[cmodel.output, x])
        cam_model.get_layer('predictions_2').set_weights(final_params)
        
        preds, cams = cmodel.predict(rimage_list)
        
        top_k = 1
        
        idxes = np.argsort(preds[0])[-top_k:]
        cam1 = np.zeros_like(cams[0, :, :, 0])
        
        for i in idxes:
            cam1 += cams[0, :, :, i]
        '''


        
        
        model_input = model.input
        A_k = model.get_layer(last_conv_layer).output
        get_output = K.function([model_input], [A_k])
        [conv_output] = get_output(rimage_list)
        conv_output = conv_output[0]
        weights = model.layers[-1].get_weights()[0][:, pred_Y[i]]
        cam1 = np.zeros(dtype=np.float32, shape=conv_output.shape[0:2])
        for k, w in enumerate(weights):
            cam1 += w * conv_output[:, :, k]        
        
        
        
        iimg = image_list[i]
        cam1 = cv2.resize(cam1, (iimg.shape[1], iimg.shape[0]))
        '''
        plt.figure(figsize=(9, 6))
        plt.xticks([])
        plt.yticks([])
    
        plt.subplot(131)
        plt.imshow(image_list[i])
        plt.title('Input Image')
        
        plt.subplot(132)
        plt.imshow(cam1)
        plt.title(last_conv_layer + ' heatmap')
        
        plt.subplot(133)
        plt.imshow(image_list[i])
        plt.imshow(cam1, cmap = 'jet',  alpha = 0.5)
        plt.title(last_conv_layer + ' CAM')
        
        plt.suptitle('Pred_Class : ' + '{}'.format(class_name[pred_Y[i]]) + '     True_Class : ' + '{}'.format(class_name[true_Y[i]]))
        '''
        plt.figure(0)
        plt.imshow(iimg)
        plt.imshow(cam1, cmap = 'jet', alpha=0.4)
        plt.axis('off')    
        
        fig_name = '%s%d%s' % ('IMG_', i, '_CAM.png')
        plt.savefig(fig_name)
        # plt.show()
        plt.close('all')
        plt.clf()
        
        i = i+1
        
        
########################################################################################
    ##################################################################################
    ## This definite is about loading model and loading image npy file              ##
    ## from current directory                                                       ##
    ## [parameter]                                                                  ##
    ##  imave_size :                                                                ##
    ##  class_name : class_name = ['class1', 'class2', ... , 'classn']              ##
    ##                                                                              ##
    ## [return]                                                                     ##
    ##   None                                                                       ##
    ##################################################################################
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from keras.optimizers import RMSprop

def Prediction(image_size, class_name, prediction_name, X_npy_file_name, y_npy_file_name, Grad_CAM = False, CAM = False, Guided_Grad_CAM = False):
  
    image_file = os.path.join(os.getcwd()+ '/' + X_npy_file_name)
    label_file = os.path.join(os.getcwd()+ '/' + y_npy_file_name)
    images = np.load(image_file,allow_pickle=True) # (120, 224, 224, 3)
    labels = np.load(label_file,allow_pickle=True) # (240,1)
    
    model_dir = os.path.join(os.getcwd())
    model_name = glob.glob(model_dir+'/*.hdf5')
    
    model_name_dir = os.listdir(model_dir)
    model_name_list = [file for file in model_name_dir if file.endswith(".hdf5")] # Load img_file name with os



    i=0
    l=images.shape[0]
    rimages=[]
    img=[]
    image_list = []
    
    # Append image ( )
    while i<=l-1:
        imagek=images[i] # (224, 224, 3)
        image_list.append(imagek)
        imagezz=np.expand_dims(imagek,axis=0) # (1, 224, 224, 3)
        rimages.append(imagezz) # list (240)
        i=i+1
    img = np.array(rimages) # (240, 1, 224, 224, 3)
    print('Image data is loaded')
    
    labels = np.squeeze(labels) # [0 0 0 ... 3 3 3]
 
    
    

    for loop in range(len(model_name)):
        
        print('model load:',model_name[loop])
        model = load_model(model_name[loop])
        
        for i, layer in enumerate(model.layers[:]):
            print(i, layer.name)
        
        model.compile(loss='categorical_crossentropy',optimizer=RMSprop(lr = 2e-5), metrics=['acc'])
        
        i = 0
        tr = 0  # true count
        fl = 0  # false count
        l = 600
        pred_Y = []
        while i <= l - 1:
            
            
            predict = model.predict(img[i])
            predictions_array = np.squeeze(predict) # [percent'1' percent'2' ... percent'n']
            
            
            '''
            predictions_array1 = predictions_array[0:72]
            predictions_array1 = predictions_array1.sum()
            predictions_array2 = predictions_array[72:144]
            predictions_array2 = predictions_array2.sum()
            predictions_array3 = predictions_array[144:216]
            predictions_array3 = predictions_array3.sum()
            predictions_array = [predictions_array1, predictions_array2, predictions_array3]
            '''
            
            
            # count correct answer
            maxpredict = np.argmax(predict)
            answer = class_name[maxpredict]
            
            
            '''
            #print(answer[0:3])
            if answer[0:3] == 'B_1':
                answer = 'B_1'
                pred_Y.append(0)
            if answer[0:3] == 'B_2':
                answer = 'B_2'
                pred_Y.append(1)
            if answer[0:3] == 'B_3':
                answer = 'B_3'
                pred_Y.append(2)
            '''
            
            
            pred_Y.append(maxpredict) # if not categorical prediction
            
            
            label_answer = prediction_name[labels[i]]
            
            if answer == label_answer:
                tr = tr + 1
            else:
                fl = fl + 1
            
            plt.figure(figsize=(6, 3))
            plt.subplot(1, 2, 1)
            
            # def plot_image(i, predictions_array, true_label, plot_image):
            plot_image(i, predictions_array, labels[i], images[i], class_name = prediction_name)
            plt.subplot(1, 2, 2)
            
            # plot_value_array(i, predictions_array, true_label)
            plot_value_array(i, predictions_array, labels[i], class_name = prediction_name)
            fig_name = '%s%s%d%s' % (model_name_list[loop],'IMG_', i, '.png')
            #plt.savefig(fig_name)
            # plt.show()
            plt.close('all')
            plt.cla()
            
            
            i = i + 1
            
        pred_Y = np.array(pred_Y)
        pred_Y = np.squeeze(pred_Y) # pred_Y = [0 0 0 ... 3 3 3]
        true_Y = np.array(labels) # true_Y = [0 0 0 ... 3 3 3]
        ###Confusion_matrix = confusion_matrix(true_Y, pred_Y)
        ###save_measure_performance(Confusion_matrix, class_name=prediction_name, model_name=model_name[loop])
 
       # print(result)
        # print(Confusion_matrix)
        print('-'*80)
        ###print(classification_report(true_Y, pred_Y, target_names=prediction_name))
        print('-'*80)
        
        if Grad_CAM == True:
            if Guided_Grad_CAM == True:
                  guided_model = modify_backprop(model, 'GuidedBackProp')
                  Grad__CAM(guided_Grad_CAM = True,
                            guided_model = guided_model,
                            true_Y = true_Y, 
                            pred_Y = pred_Y, 
                            image_list = image_list, 
                            model = model, 
                            class_name = class_name,
                            model_name = model_name[loop],
                            first_layer = 'post_relu',
                            second_layer = 'relu',
                            third_layer = 'relu')
            if Guided_Grad_CAM == False:
                  Grad__CAM(guided_Grad_CAM = False,
                            guided_model = None,
                            true_Y = true_Y, 
                            pred_Y = pred_Y, 
                            image_list = image_list, 
                            model = model, 
                            class_name = class_name,
                            model_name = model_name[loop],
                            first_layer = 'post_relu',
                            second_layer = 'conv5_block3_3_conv',
                            third_layer = 'conv5_block3_3_conv')                  
            # Densenet-201 : 
            # Resnet-152v2 : 
            # NASNetLarge : 
            # VGG-19 : 'block1_conv1','block3_conv1', 'block5_conv1'
            # Inception-v3 :       
                  
              
        if CAM == True:
            keras_CAM(true_Y = true_Y,
                      pred_Y = pred_Y,
                      image_list = image_list,
                      model = model,
                      class_name = class_name,
                      model_name = model_name[loop],
                      last_conv_layer = 'conv5_block3_3_conv',
                      pred_layer = 'post_relu')
            
            # Densenet-201 : 'relu' 
            # Resnet-152v2 : 'conv5_block3_3_conv' 
            # NASNetLarge : 'normal_concat_18' 
            # VGG-19 : 'block5_pool'
            # Inception-v3 : 'mixed10'
            '''
        if guided_Grad_CAM == True:
            guided_model = modify_backprop(model, 'GuidedBackProp')
            keras_guided_Grad_CAM(true_Y = true_Y, 
                                  pred_Y = pred_Y, 
                                  image_list = img, 
                                  guided_model = guided_model, 
                                  class_name = class_name,
                                  model_name = model_name[loop],
                                  first_layer = 'block1_pool',
                                  second_layer = 'block3_pool',
                                  third_layer = 'block5_pool')
            '''
            
####################################################################################
####################################################################################
##       #################################################################        ##
##       ## 2020.03.02 HAEMYUNG                                         ##        ##
##       ## This code is about Grad_CAM                                 ##        ##
##       ## [function]                                                  ##        ##
##       ##   i : Performance number                                    ##        ##
##       ##   class_name :                                              ##        ##
##       ##   X_npy_file_name :                                         ##        ##
##       ##   y_npy_file_name :                                         ##        ##
##       ## [return]                                                    ##        ##
##       ##   None                                                      ##        ##
##       #################################################################        ##
####################################################################################
####################################################################################
register_gradient()
Prediction(image_size = '224', 
           class_name = ['B1','B2','B3'],           
           prediction_name = ['B1','B2','B3'],           
           X_npy_file_name = 'thr_50_size_224_X.npy', 
           y_npy_file_name = 'thr_50_size_224_y.npy',
           Grad_CAM = True,
           Guided_Grad_CAM = True)
'''  
 class_name = ['B_1_1_1','B_1_1_2','B_1_1_3','B_1_1_4','B_1_1_5','B_1_1_6','B_1_1_7','B_1_1_8',
'B_1_2_1','B_1_2_2','B_1_2_3','B_1_2_4','B_1_2_5','B_1_2_6','B_1_2_7','B_1_2_8',
'B_1_3_1','B_1_3_2','B_1_3_3','B_1_3_4','B_1_3_5','B_1_3_6','B_1_3_7','B_1_3_8',
'B_1_4_1','B_1_4_2','B_1_4_3','B_1_4_4','B_1_4_5','B_1_4_6','B_1_4_7','B_1_4_8',
'B_1_5_1','B_1_5_2','B_1_5_3','B_1_5_4','B_1_5_5','B_1_5_6','B_1_5_7','B_1_5_8',
'B_1_6_1','B_1_6_2','B_1_6_3','B_1_6_4','B_1_6_5','B_1_6_6','B_1_6_7','B_1_6_8',
'B_1_7_1','B_1_7_2','B_1_7_3','B_1_7_4','B_1_7_5','B_1_7_6','B_1_7_7','B_1_7_8',
'B_1_8_1','B_1_8_2','B_1_8_3','B_1_8_4','B_1_8_5','B_1_8_6','B_1_8_7','B_1_8_8',
'B_1_9_1','B_1_9_2','B_1_9_3','B_1_9_4','B_1_9_5','B_1_9_6','B_1_9_7','B_1_9_8',
'B_2_1_1','B_2_1_2','B_2_1_3','B_2_1_4','B_2_1_5','B_2_1_6','B_2_1_7','B_2_1_8',
'B_2_2_1','B_2_2_2','B_2_2_3','B_2_2_4','B_2_2_5','B_2_2_6','B_2_2_7','B_2_2_8',
'B_2_3_1','B_2_3_2','B_2_3_3','B_2_3_4','B_2_3_5','B_2_3_6','B_2_3_7','B_2_3_8',
'B_2_4_1','B_2_4_2','B_2_4_3','B_2_4_4','B_2_4_5','B_2_4_6','B_2_4_7','B_2_4_8',
'B_2_5_1','B_2_5_2','B_2_5_3','B_2_5_4','B_2_5_5','B_2_5_6','B_2_5_7','B_2_5_8',
'B_2_6_1','B_2_6_2','B_2_6_3','B_2_6_4','B_2_6_5','B_2_6_6','B_2_6_7','B_2_6_8',
'B_2_7_1','B_2_7_2','B_2_7_3','B_2_7_4','B_2_7_5','B_2_7_6','B_2_7_7','B_2_7_8',
'B_2_8_1','B_2_8_2','B_2_8_3','B_2_8_4','B_2_8_5','B_2_8_6','B_2_8_7','B_2_8_8',
'B_2_9_1','B_2_9_2','B_2_9_3','B_2_9_4','B_2_9_5','B_2_9_6','B_2_9_7','B_2_9_8',
'B_3_1_1','B_3_1_2','B_3_1_3','B_3_1_4','B_3_1_5','B_3_1_6','B_3_1_7','B_3_1_8',
'B_3_2_1','B_3_2_2','B_3_2_3','B_3_2_4','B_3_2_5','B_3_2_6','B_3_2_7','B_3_2_8',
'B_3_3_1','B_3_3_2','B_3_3_3','B_3_3_4','B_3_3_5','B_3_3_6','B_3_3_7','B_3_3_8',
'B_3_4_1','B_3_4_2','B_3_4_3','B_3_4_4','B_3_4_5','B_3_4_6','B_3_4_7','B_3_4_8',
'B_3_5_1','B_3_5_2','B_3_5_3','B_3_5_4','B_3_5_5','B_3_5_6','B_3_5_7','B_3_5_8',
'B_3_6_1','B_3_6_2','B_3_6_3','B_3_6_4','B_3_6_5','B_3_6_6','B_3_6_7','B_3_6_8',
'B_3_7_1','B_3_7_2','B_3_7_3','B_3_7_4','B_3_7_5','B_3_7_6','B_3_7_7','B_3_7_8',
'B_3_8_1','B_3_8_2','B_3_8_3','B_3_8_4','B_3_8_5','B_3_8_6','B_3_8_7','B_3_8_8',
'B_3_9_1','B_3_9_2','B_3_9_3','B_3_9_4','B_3_9_5','B_3_9_6','B_3_9_7','B_3_9_8']
'''