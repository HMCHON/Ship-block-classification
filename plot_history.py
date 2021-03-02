from keras.models import load_model
import matplotlib.pyplot as plt
import pandas as pd
import csv
import numpy as np
import glob
import os
###############################################################################
# Load history_history.npy
df = pd.read_csv('history.csv')
df
print('Loaded history from diretory')
###############################################################################
loss_df = df[['loss']]
val_loss_df = df[['val_loss']]
acc_df = df[['acc']]
val_acc_df = df[['val_acc']]

    
def plot_training(history):
    acc = acc_df
    val_acc = val_acc_df
    loss = loss_df
    val_loss = val_loss_df
    epochs = range(len(acc))
    
    plt.plot(epochs, acc, 'b')
    plt.plot(epochs, val_acc, 'r')
    plt.title('Training and Validation accuracy')
    fig1 = plt.gcf()
    plt.show()
    fig1.savefig('VGG19_Training and Validation accuracy.png')
    plt.close(fig1)
    
    plt.plot(epochs, loss, 'b')
    plt.plot(epochs, val_loss, 'r')
    plt.title('Training and validation loss')
    fig2 = plt.gcf()
    plt.show()
    fig2.savefig('VGG19_Training and validation loss.png')

plot_training(history)

