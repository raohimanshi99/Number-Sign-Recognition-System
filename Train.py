# -*- coding: utf-8 -*-
"""
Created on Fri Aug 16 09:24:20 2019

@author: Sumit
"""

from keras.models import Sequential
from keras.layers import Dense, Convolution2D,MaxPooling2D,Flatten


model = Sequential()

model.add(Convolution2D(32,(3,3),input_shape = (64,64,1),activation = 'relu'))
model.add(MaxPooling2D(pool_size = (2,2)))
model.add(Convolution2D(32,(3,3),activation = 'relu'))
model.add(MaxPooling2D(pool_size = (2,2)))

model.add(Flatten())
model.add(Dense(units = 128,activation = 'relu'))
model.add(Dense(units = 10,activation = 'softmax'))

model.compile(optimizer = 'adam',loss = 'categorical_crossentropy',metrics = ['accuracy'])


from keras.preprocessing.image import ImageDataGenerator
train_gen = ImageDataGenerator(rescale = 1./255,horizontal_flip= True,shear_range=0.2,zoom_range=0.2)

test_gen = ImageDataGenerator(rescale = 1./255)
 
train_data = train_gen.flow_from_directory('data/train',
                                           target_size=(64,64),
                                           batch_size=5,
                                           color_mode='grayscale',
                                           class_mode='categorical'
                                           )

test_data = test_gen.flow_from_directory('data/test',
                                         target_size=(64,64),
                                         batch_size=5,
                                         color_mode='grayscale',
                                         class_mode='categorical')

model.fit_generator(train_data,
          validation_data = test_data,
          epochs = 10,
          steps_per_epoch = 2599,
          validation_steps = 1002
          )

json_model = model.to_json()
with open("model-bw.json", "w") as json_file:
    json_file.write(json_model)
model.save_weights('model-bw.h5')










