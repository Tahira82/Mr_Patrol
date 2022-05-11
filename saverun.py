from keras.models import load_model
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
start = time.time()
cnn=load_model('F:/FYP/emer res/models/modelf.h5')
cc=0

import cv2
import os

from skimage import io
import cv2
import os
from keras.preprocessing.image import ImageDataGenerator
test_gen= ImageDataGenerator(rescale=1./255)
count=0
c=0
u=input('enter url with */shot.jpg* at the end: ')
url = u
# loop over the image URLs
while url:
    # download the image using scikit-image

    image = io.imread(url)

    cv2.imwrite(os.path.join("F:/FYP/emer res/vidim/imagestotetOFFLINE", '%d.png') % count, image)
    count+=1
    cv2.waitKey(10)
    print('done')

    test_generator = test_gen.flow_from_directory('F:/FYP/emer res/vidim',
                                                  color_mode='rgb',
                                                  batch_size=32, shuffle=False, class_mode=None, seed=42)

    t_datagen = ImageDataGenerator(
        rotation_range=40,
        width_shift_range=0.2,
        height_shift_range=0.2,
        rescale=1. / 255,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True)
    t_generator = t_datagen.flow_from_directory(
        directory='F:/FYP/emer res/dataGen/label', color_mode='rgb',
        batch_size=32,
        class_mode='categorical', shuffle=True, seed=42)
    filelist = [f for f in os.listdir('F:/FYP/emer res/vidim/imagestotetOFFLINE')]
    test_generator.reset()
    predictions = cnn.predict_generator(test_generator, verbose=1, steps=1/ 32)
    count = 0
    for k in range(0, len(predictions)):
        predict = np.argmax(predictions[k])
        count = count + 1

        print("c=", count)

    l = (t_generator.class_indices)
    l = dict((v, k) for k, v in l.items())
    predict1 = np.argmax(predictions, axis=1)
    pred1 = [l[k] for k in predict1]
    filenames = test_generator.filenames

    res = pd.DataFrame({'file': filenames, 'predi': pred1})


    for i in range(0, len(pred1)):
        print(pred1[i])
        if pred1[i] != 'normal':

            f = open('F:/FYP/emer res/result/result.txt', "a", )
            f.write("emergency ")
            ccc=str(cc)
            f.write(ccc)
            ccc=int(cc)
            f.write(' :')
            f.write(pred1[i])
            cc = cc + 1

            f.write('      ')

            f.flush()

    end = time.time()
    print('Processing time:', (end - start))


    time.sleep(5)
    for f in filelist:
        os.remove(os.path.join('F:/FYP/emer res/vidim/imagestotetOFFLINE', f))
    print('ok')


