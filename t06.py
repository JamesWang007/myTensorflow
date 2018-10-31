# -*- coding: utf-8 -*-
"""
Created on Fri Oct 19 14:55:45 2018

    Predict house prices: regression 
    https://www.tensorflow.org/tutorials/keras/basic_regression
    
    not working
    
@author: bejin
"""

from __future__ import absolute_import, division, print_function

import tensorflow as tf
from tensorflow import keras

import numpy as np
print(tf.__version__)


# dataset
boston_housing = keras.datasets.boston_housing
(train_data, train_labels), (test_data, test_labels) = boston_housing.load_data()

# Shuffle the training set
order = np.argsort(np.random.random(train_labels.shape))
train_data = train_data[order]
train_labels = train_labels[order]


# Examples and features
print("Training set: {}".format(train_data.shape))  # 404 examples, 13 features
print("Testing set:  {}".format(test_data.shape))   # 102 examples, 13 features

print(train_data[0])


import pandas as pd

column_names = ['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS', 
                'RAD', 'TAX', 'PTRATIO', 'B', 'STAT']

df = pd.DataFrame(train_data, columns = column_names)
df.head()


# Labels
print(train_labels[0:10])   # Display first 10 entries


# Normals features
# Test data is not uses when calculating the mean and std

mean        = train_data.mean(axis=0)
std         = train_data.std(axis=0)
train_data  = (train_data - mean) / std
test_data   = (test_data - mean) / std

print(train_data[0])    # First training sample, normalized


# Create the model
def build_model():
    model = keras.Sequential([
                keras.layers.Dense(64, activation = tf.nn.relu,
                                   input_shape = (train_data.shape[1],)),
            ])

    optimizer = tf.train.RMSPropOptimizer(0.001)
    
    model.compile(loss = 'mse',
                  optimizer = optimizer,
                  metrics=['mae'])
    return model

model = build_model()
model.summary()



# Train the model
# Display training progress by printing a single dot for each completed epoch
class PrintDot(keras.callbacks.Callback):
    def on_epoch_end(self, epoch, logs):
        if epoch % 100 == 0: print('')
        print('.', end='')
        
EPOCHS = 500

# Store training stats
history = model.fit(train_data, train_labels, epochs=EPOCHS,
                    validation_split=0.2, verbose=0,
                    callbacks=[PrintDot()])


import matplotlib.pyplot as plt

def plot_history(history):
    plt.figure()
    plt.xlabel('Epoch')
    plt.ylabel('Mean Abs Error [1000$]')
    plt.plot(history.epoch, np.ary(history.history['mean_absolute_error']), 
                                   label ='Train Loss')
    
    plt.legend()
    plt.ylim([0, 5])
    
plot_history(history)



# more about callback
model = build_model()

# The patience parameter is the amount of epochs to check for improvement
early_stop = keras.callbacks.EarlyStopping(monitor='val_loss', patience=20)

history = model.fit(train_data, train_labels, epochs=EPOCHS,
                    validation_split=0.2, verbose=0,
                    callbacks=[early_stop, PrintDot()])

plot_history(history)

    
[loss, mae] = model.evaluate(test_data, test_labels, verbose=0)

print("Testing set Mean Abs Error: ${:7.2f}".format(mae * 1000))




# predict
test_predictions = model.predict(test_data).flatten()

plt.scatter(test_labels, test_predictions)
plt.xlabel('True Values [1000$]')
plt.ylabel('Predictions [1000$]')
plt.axis('equal')
plt.xlim(plt.xlim())
plt.ylim(plt.ylim())
_ = plt.plot([-100, 100], [-100, 100])



error = test_predictions - test_labels
plt.hist(error, bins = 50)
plt.xlabel("Prediction Error [1000$]")
_ = plt.ylabel("Count")


















