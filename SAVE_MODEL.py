from keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array, load_img
from tensorflow import keras
import numpy as np
import os
from random import shuffle
from tqdm import tqdm
import tensorflow as tf
import cv2
import matplotlib as plt
from keras.models import Sequential
from keras.layers.convolutional import Convolution2D
from keras.layers.core import Flatten, Dense, Activation
from keras.utils import np_utils
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D
from keras.layers import Activation, Flatten, Dense, Dropout
from keras.preprocessing.image import ImageDataGenerator
import time
import pandas as pd


train_data_fire ='F:/FYP/emer res/BUILDING FIRE'
train_data_collapse='F:/FYP/emer res/BUILDING COLLAPSE'
train_data_turnover='F:/FYP/emer res/CAR TURNED OVER ACCIDENTS/yes'
train_data_no_fc='F:/FYP/emer res/normal buildings'
train_data_no_turnover='F:/FYP/emer res/CAR TURNED OVER ACCIDENTS/no'


train_data='F:/FYP/emer res/TRAIN'
labels='F:/FYP/emer res/dataGen/labels'

for i in tqdm(os.listdir(train_data_fire)):
    path = os.path.join(train_data_fire, i)
    img = cv2.imread(path, -1)
    x = img_to_array(img)
    x = x.reshape((1,) + x.shape)

    train_datagen = ImageDataGenerator(
        rotation_range=40,
        width_shift_range=0.2,
        height_shift_range=0.2,
        rescale=1. / 255,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True)
    j = 1
    gt=3
    for batch in train_datagen.flow(x, batch_size=1, save_to_dir='F:/FYP/emer res/dataGen/train/fire', save_format='png',
                             save_prefix='all'):
        j += 1
        if j & gt:
            break


for i in tqdm(os.listdir(train_data_collapse)):
        path = os.path.join(train_data_collapse, i)
        img = cv2.imread(path, -1)
        x = img_to_array(img)
        x = x.reshape((1,) + x.shape)

        train_datagen = ImageDataGenerator(
            rotation_range=40,
            width_shift_range=0.2,
            height_shift_range=0.2,
            rescale=1. / 255,
            shear_range=0.2,
            zoom_range=0.2,
            horizontal_flip=True)
        j = 1
        gt = 3
        for batch in train_datagen.flow(x, batch_size=1, save_to_dir='F:/FYP/emer res/dataGen/train/collapse',
                                        save_format='png',
                                        save_prefix='all'):
            j += 1
            if j & gt:
                break

for i in tqdm(os.listdir(train_data_turnover)):
    path = os.path.join(train_data_turnover, i)
    img = cv2.imread(path, -1)
    x = img_to_array(img)
    x = x.reshape((1,) + x.shape)

    train_datagen = ImageDataGenerator(
        rotation_range=40,
        width_shift_range=0.2,
        height_shift_range=0.2,
        rescale=1. / 255,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True)
    j = 1
    gt=3
    for batch in train_datagen.flow(x, batch_size=1, save_to_dir='F:/FYP/emer res/dataGen/train/turnover', save_format='png',
                             save_prefix='all'):
        j += 1
        if j & gt:
            break

for i in tqdm(os.listdir(train_data_no_fc)):
        path = os.path.join(train_data_no_fc, i)
        img = cv2.imread(path, -1)
        x = img_to_array(img)
        x = x.reshape((1,) + x.shape)

        train_datagen = ImageDataGenerator(
            rotation_range=40,
            width_shift_range=0.2,
            height_shift_range=0.2,
            rescale=1. / 255,
            shear_range=0.2,
            zoom_range=0.2,
            horizontal_flip=True)
        j = 1
        gt = 3
        for batch in train_datagen.flow(x, batch_size=1, save_to_dir='F:/FYP/emer res/dataGen/train/normal',
                                        save_format='png',
                                        save_prefix='all'):
            j += 1
            if j & gt:
                break


for i in tqdm(os.listdir(train_data_no_turnover)):
        path = os.path.join(train_data_no_turnover, i)
        img = cv2.imread(path, -1)
        x = img_to_array(img)
        x = x.reshape((1,) + x.shape)

        train_datagen = ImageDataGenerator(
            rotation_range=40,
            width_shift_range=0.2,
            height_shift_range=0.2,
            rescale=1. / 255,
            shear_range=0.2,
            zoom_range=0.2,
            horizontal_flip=True)
        j = 1
        gt = 3
        for batch in train_datagen.flow(x, batch_size=1, save_to_dir='F:/FYP/emer res/dataGen/train/normal',
                                        save_format='png',
                                        save_prefix='all'):
            j += 1
            if j & gt:
                break
validation_datagen = ImageDataGenerator(rescale=1. / 255)
test_gen= ImageDataGenerator(rescale=1./255)
train_generator = train_datagen.flow_from_directory(
       directory= 'F:/FYP/emer res/dataGen/train',color_mode='rgb',
        batch_size=32,
        class_mode='categorical',shuffle=True,seed=42)
validation_generator = validation_datagen.flow_from_directory(
        directory='F:/FYP/emer res/validation',color_mode='rgb',
        batch_size=32,
        class_mode='categorical',shuffle=True,seed=42)

ndim=3
input_shape = (256, 256, 3)
IMG_SIZE =  256
NB_CHANNELS =  3
BATCH_SIZE =  32
NB_TRAIN_IMG =  40000
NB_VALID_IMG =  12171
cnn = Sequential()
cnn.add(Conv2D(filters=32,
                   kernel_size=(3,3),
                   strides=(1, 1),
                   padding='same',
                   input_shape=(IMG_SIZE, IMG_SIZE, NB_CHANNELS),
                   data_format='channels_last'))
cnn.add(Activation('relu'))
cnn.add(MaxPooling2D(pool_size=(2, 2),
                         strides=2))
cnn.add(Conv2D(filters=64,
                   kernel_size=(3,3),
                   strides=(1, 1),
                   padding='valid'),)
cnn.add(Activation('relu'))
cnn.add(MaxPooling2D(pool_size=(2, 2),
                         strides=2))
cnn.add(Flatten())
cnn.add(Dense(128))
cnn.add(Activation('relu'))
cnn.add(Dropout(0.5))

cnn.add(Dense(4))
cnn.add(Activation('softmax'))
cnn.compile(loss='categorical_crossentropy', optimizer='rmsprop', metrics=['accuracy'])

start = time.time()
cnn.fit_generator(
        train_generator,
        steps_per_epoch=NB_TRAIN_IMG // BATCH_SIZE,
        epochs=10,verbose=2,
        validation_data=validation_generator,
        validation_steps=NB_VALID_IMG // BATCH_SIZE)
cnn.evaluate_generator(validation_generator,steps=12171/32)


cnn.save('F:/FYP/emer res/models/model3.h5')

