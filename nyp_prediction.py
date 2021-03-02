########################
# CNN Image Prediction #
########################

from keras.models import load_model
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import glob
import os
###############################################################################
# Load Model
model_dir = os.path.join(os.getcwd())
model_name = glob.glob(model_dir+'/*.hdf5')
print('Loaded model from diretory',model_name[0])
model = load_model(model_name[0])
model.compile(loss='binary_crossentropy',optimizer='rmsprop',metrics=['accuracy'])

image_file = 'Predict_Zoom_in_X.npy'
label_file = 'Predict_Zoom_in_y.npy'

image_file = os.path.join(os.getcwd()+'/Predict_Zoom_in_X_331.npy')
label_file = os.path.join(os.getcwd()+'/Predict_Zoom_in_y_331.npy')
images = np.load(image_file,allow_pickle=True)
labels = np.load(label_file,allow_pickle=True)
###############################################################################
# Append Image Data
i=0
l=images.shape[0]
rimages=[]
img=[]

while i<=l-1:
    #plt.imshow(images[i], cmap = 'gray')
    #plt.show()
    imagek=images[i]
    imagezz=np.expand_dims(imagek,axis=0)
    rimages.append(imagezz)
    #plt.imshow(rimages[i], cmap = 'gray')
    #plt.show()
    #print(i)
    i=i+1
img = np.array(rimages)
print('append image data is finish')
###############################################################################
# Plot
def plot_image(i, predictions_array, true_label, plot_image):
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
###############################################################################
def plot_value_array(i, predictions_array, true_label):
    plt.grid(False)
    plt.xticks(range(4), class_name)
    plt.yticks([])
    thisplot = plt.bar(range(4), predictions_array, color='#777777')
    plt.ylim([0,1])
    predicted_label=np.argmax(predictions_array)
    
    thisplot[predicted_label].set_color('red')
    thisplot[true_label].set_color('blue')
###############################################################################
i = 0
tr = 0  # true count
fl = 0  # false count
#class_name = ['A', 'B', 'C', 'D']
class_name = ['A', 'B','C','D']
labels = np.squeeze(labels)

A_A = 0
A_B = 0
A_C = 0
A_D = 0

B_A = 0
B_B = 0
B_C = 0
B_D = 0

C_A = 0
C_B = 0
C_C = 0
C_D = 0

D_A = 0
D_B = 0
D_C = 0
D_D = 0

while i <= l - 1:
    predict = model.predict(img[i])
    predictions_array = np.squeeze(predict)

    # count correct answer
    maxpredict = np.argmax(predict)
    answer = class_name[maxpredict]
    label_answer = class_name[labels[i]]
    if answer == label_answer:
        tr = tr + 1
    else:
        fl = fl + 1

    if label_answer == 'A':
        if answer == 'A':
            A_A = A_A + 1
        if answer == 'B':
            A_B = A_B + 1
        if answer == 'C':
            A_C = A_C + 1
        if answer == 'D':
            A_D = A_D + 1
    if label_answer == 'B':
        if answer == 'A':
            B_A = B_A + 1
        if answer == 'B':
            B_B = B_B + 1
        if answer == 'C':
            B_C = B_C + 1
        if answer == 'D':
            B_D = B_D + 1
    if label_answer == 'C':
        if answer == 'A':
            C_A = C_A + 1
        if answer == 'B':
            C_B = C_B + 1
        if answer == 'C':
            C_C = C_C + 1
        if answer == 'D':
            C_D = C_D + 1
    if label_answer == 'D':
        if answer == 'A':
            D_A = D_A + 1
        if answer == 'B':
            D_B = D_B + 1
        if answer == 'C':
            D_C = D_C + 1
        if answer == 'D':
            D_D = D_D + 1

    plt.figure(figsize=(6, 3))
    plt.subplot(1, 2, 1)
    # def plot_image(i, predictions_array, true_label, plot_image):
    plot_image(i, predictions_array, labels[i], images[i])
    plt.subplot(1, 2, 2)
    # plot_value_array(i, predictions_array, true_label)
    plot_value_array(i, predictions_array, labels[i])
    fig_name = '%s%d%s' % ('IMG_', i, '.png')
    plt.savefig(fig_name)
    plt.show()
    plt.close('all')
    i = i + 1
##############################################################################
# make confusion matrix
CM1 = [A_A, A_B, A_C, A_D]
CM2 = [B_A, B_B, B_C, B_D]
CM3 = [C_A, C_B, C_C, C_D]
CM4 = [D_A, D_B, D_C, D_D]

A_TP = A_A
A_FP = B_A + C_A + D_A
A_TN = B_B + B_C + B_D + C_B + C_C + C_D + D_B + D_C + D_D
A_FN = A_B + A_C + A_D

B_TP = B_B
B_FP = A_B + C_B + D_B
B_TN = A_A + A_C + A_D + C_A + C_C + C_D + D_A + D_C + D_D
B_FN = B_A + B_C + B_D

C_TP = C_C
C_FP = A_C + B_C + D_C
C_TN = A_A + A_B + A_D + B_A + B_B + B_D + D_A + D_B + D_D
C_FN = C_A + C_B + C_D

D_TP = D_D
D_FP = A_D + B_D + C_D
D_TN = A_A + A_B + A_C + B_A + B_B + B_C + C_A + C_B + C_C
D_FN = D_A + D_B + D_C

# Precision & Recall
if A_TP is 0:
    A_Precision = 0
    A_Recall = 0
else:
    A_Precision = A_TP/(A_TP + A_FP)
    A_Recall = A_TP/(A_TP + A_FN)
    
if B_TP is 0:
    B_Precision = 0
    B_Recall = 0
else:
    B_Precision = B_TP/(B_TP + B_FP)
    B_Recall = B_TP/(B_TP + B_FN)

if C_TP is 0:
    C_Precision = 0
    C_Recall = 0
else:
    C_Precision = C_TP/(C_TP + C_FP)
    C_Recall = C_TP/(C_TP + C_FN)

if D_TP is 0:
    D_Precision = 0
    D_Recall = 0
else:
    D_Precision = D_TP/(D_TP + D_FP)
    D_Recall = D_TP/(D_TP + D_FN)

       
# Average
Avg_Precision = (A_Precision + B_Precision + C_Precision + D_Precision) / 4
Avg_Recall = (A_Recall + B_Recall + C_Recall + D_Recall) / 4

# F1 Score & Accuracy
F1_Score = 2*((Avg_Precision*Avg_Recall)/(Avg_Precision+Avg_Recall))
Accuracy = (A_A + B_B + C_C + D_D)/(A_A + A_B + A_C + A_D + B_A + B_B + B_C + B_D + C_A + C_B + C_C + C_D + D_A + D_B + D_C + D_D)

confusion_matrix = [[A_A, A_B, A_C, A_D],
                    [B_A, B_B, B_C, B_D],
                    [C_A, C_B, C_C, C_D],
                    [D_A, D_B, D_C, D_D]]

print('confusion_matrix :',confusion_matrix)
print('Avg_Precision :',Avg_Precision)
print('Avg_Recall :', Avg_Recall)
print('F1-score :', F1_Score)
print('Accuracy :', Accuracy)
print('tr :', tr)
print('fl :', fl)
###############################################################################
model_name = model_name[0]

csv1 = [['model', model_name[0:-5]],
        ['tr', tr],
        ['fl', fl],
        ['confusion metrix', confusion_matrix],
        ['A_Precision', A_Precision],
        ['B_Precision', B_Precision],
        ['C_Precision', C_Precision],
        ['D_Precision', D_Precision],
        ['A_Recall', A_Recall],
        ['B_Recall', B_Recall],
        ['C_Recall', C_Recall],
        ['D_Recall', D_Recall],
        ['Average Precision', Avg_Precision],
        ['Average Recall', Avg_Recall],
        ['F1-Score', F1_Score],
        ['Accuracy', Accuracy]]

df = pd.DataFrame(csv1)
df.to_csv('%s.csv' % model_name[0:-5])
