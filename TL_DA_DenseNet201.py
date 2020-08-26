from keras.applications.densenet import DenseNet201
from keras.preprocessing.image import ImageDataGenerator
from keras.optimizers import RMSprop
from keras.models import Model
from keras.layers import Dropout, Flatten, Dense, GlobalAveragePooling2D
from keras.callbacks import ModelCheckpoint, LearningRateScheduler, TensorBoard, EarlyStopping
from keraspp import sfile
from keraspp import skeras



from PIL import Image
import matplotlib.pyplot as plt
import pandas as pd
import os
os.environ["CUDA_VISIBLE_DEVICES"]='2'
#######################################################################
HEIGHT = 224
WIDTH = 224

base_model = DenseNet201(include_top = False, weights='imagenet', input_shape=(HEIGHT, WIDTH, 3))

#######################################################################
train_data_dir = "/home/user/PycharmProjects/lecture/Boundary_Project/imageset/new_original_2/5000by3000/5000by3000_crop_con_76_train_test/train"
test_data_dir = "/home/user/PycharmProjects/lecture/Boundary_Project/imageset/new_original_2/5000by3000/5000by3000_crop_con_76_train_test/test"
BATCH_SIZE = 16

train_datagen = ImageDataGenerator(rescale=1./255)

train_generator = train_datagen.flow_from_directory(
    train_data_dir,
    target_size = (HEIGHT, WIDTH),
    batch_size = BATCH_SIZE,
    class_mode = "categorical")

validation_datagen = ImageDataGenerator(rescale=1./255)

validation_generator = validation_datagen.flow_from_directory(
    test_data_dir,
    target_size = (HEIGHT, WIDTH),
    batch_size = BATCH_SIZE,
    class_mode = "categorical")

#######################################################################
def build_finetune_model(base_model,nb_classes):
    for layer in base_model.layers[:5]:
        layer.trainable = False

    x = base_model.output
    x = GlobalAveragePooling2D()(x)
    x = Dropout(0.4)(x)
    predictions = Dense(nb_classes, activation='softmax')(x)

    finetune_model = Model(input=base_model.input, output=predictions)
    finetune_model.summary()
    return finetune_model

class_list = ['B1','B2','B3']
finetune_model = build_finetune_model(base_model, nb_classes = len(class_list))
#######################################################################
NUM_EPOCH = 5
num_train_images = 6912
num_test_images = 1728
#######################################################################
# from keras.utils import multi_gpu_model
# finetune_model = multi_gpu_model(finetune_model, gpus=4)
'''
import tensorflow as tf
from keras.utils import multi_gpu_model
import keras.backend.tensorflow_backend as K

config = tf.ConfigProto(allow_soft_placement=True)
config.gpu_options.per_process_gpu_memory_fraction = 0.8
config.gpu_options.allow_growth = False
sess = tf.Session(config=config)
K.set_session(sess)

finetune_model = multi_gpu_model(finetune_model, gpus=3)
'''
#######################################################################
finetune_model.compile(loss='categorical_crossentropy',optimizer=RMSprop(lr = 2e-5), metrics=['acc'])

suffix = sfile.unique_filename('datatime')
foldname = 'output_' + suffix
os.makedirs(foldname)


filepath = "./" + foldname + "/{epoch:02d}-{val_loss:.4f}.hdf5"

checkpoint = ModelCheckpoint(filepath, monitor = ['val_acc'], verbose = 1, mode = 'max')
callbacks_list = [checkpoint]

history = finetune_model.fit_generator(train_generator,
                                       epochs = NUM_EPOCH,
                                       workers = 4,
                                       steps_per_epoch=num_train_images // BATCH_SIZE,
                                       shuffle = True,
                                       callbacks = callbacks_list,
                                       validation_data = validation_generator,
                                       nb_val_samples = num_test_images)

skeras.save_history_history('TL_DA_DenseNet-201', history.history, fold = foldname)

score = finetune_model.evaluate(validation_generator, verbose = 0)
finetune_model.save(os.path.join(foldname, 'TL_DA_DenseNet-201.hdf5'))
print('Output results are saved in', foldname)

hist_df = pd.DataFrame(history.history)

hist_json_file = 'TL_DA_DenseNet-201.json' 
with open(hist_json_file, mode='w') as f:
    hist_df.to_json(f)

# or save to csv: 
hist_csv_file = 'TL_DA_DenseNet-201.csv'
with open(hist_csv_file, mode='w') as f:
    hist_df.to_csv(f)

# Plot the training and validation loss + accuracy
def plot_training(history):
    acc = history.history['acc']
    val_acc = history.history['val_acc']
    loss = history.history['loss']
    val_loss = history.history['val_loss']
    epochs = range(len(acc))
    
    plt.plot(epochs, acc, 'b')
    plt.plot(epochs, val_acc, 'r')
    plt.title('Training and Validation accuracy')
    fig1 = plt.gcf()
    plt.show()
    fig1.savefig('TL_DA_DenseNet-201_Training and Validation accuracy.png')
    plt.close(fig1)
    
    plt.plot(epochs, loss, 'b')
    plt.plot(epochs, val_loss, 'r')
    plt.title('Training and validation loss')
    fig2 = plt.gcf()
    plt.show()
    fig2.savefig('TL_DA_DenseNet-201_Training and validation loss.png')

plot_training(history)

