# -*- coding: utf-8 -*-
"""
Created on Thu Oct 18 12:28:06 2018

    MNIST Data package

    not working

@author: bejin
"""

#import input_data

#mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)

import tensorflow as tf
mnist = tf.keras.datasets.mnist
#import tensorflow.contrib.keras.python.keras.datasets



# x is a placeholder, not a special value
x = tf.placeholder("float", [None, 784])


W = tf.Variable(tf.zeros([784, 10]))
b = tf.Variable(tf.zeros([10]))

y = tf.nn.softmax(tf.matmul(x, W) + b)


y_ = tf.placeholder("float", [None, 10])

cross_entropy = -tf.reduce_sum(y_ * tf.log(y))

# GD, r = 0.01
train_step = tf.train.GradientDescentOptimizer(0.01).minimize(cross_entropy)

# init
init = tf.initialize_all_variables()


# session
sess = tf.Session()
sess.run(init)

for i in range(1000):
    batch_xs, batch_ys = mnist.train.next_batch(100)
    sess.run(train_step, feed_dict = {x: batch_xs, y_: batch_ys})
    
    

correct_prediction = tf.equal(tf.argmax(y,1), tf.argmax(y_,1))

accuracy = tf.reduct_mean(tf.cast(correct_prediction, "float"))

print (sess.run(accuracy, feed_dict={x: mnist.test.images, y_: mnist.test.labels}))
    



























