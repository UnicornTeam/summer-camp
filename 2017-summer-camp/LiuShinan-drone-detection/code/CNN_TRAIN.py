from __future__ import print_function
import tensorflow as tf
import numpy as np
import time
import os.path as path
import os
from sklearn.metrics import accuracy_score, roc_auc_score, f1_score, precision_score, recall_score, confusion_matrix
import pylab as pl
import CNN_INPUT
data = CNN_INPUT.read_data()
x = tf.placeholder(tf.float32, shape=[None, 64, 64, 1])
y_ = tf.placeholder(tf.float32, shape=[None, 2])

def weight_variable(shape):
  initial = tf.truncated_normal(shape, stddev=0.1)
  return tf.Variable(initial)
def bias_variable(shape):
  initial = tf.constant(0.1, shape=shape)
  return tf.Variable(initial)

def conv2d(x, W):
  return tf.nn.conv2d(x, W, strides=[1, 1, 1, 1], padding='SAME')
def max_pool_2x2(x):
  return tf.nn.max_pool(x, ksize=[1, 2, 2, 1],
                        strides=[1, 2, 2, 1], padding='SAME')

W_conv1 = weight_variable([3, 3, 1, 32])
b_conv1 = bias_variable([32])
x_image = tf.reshape(x, [-1,64,64,1])
h_conv1 = tf.nn.relu(conv2d(x_image, W_conv1) + b_conv1)
h_pool1 = max_pool_2x2(h_conv1)
#h_pool1 = tf.nn.dropout(h_pool1, dropout)


W_conv2 = weight_variable([3, 3, 32, 64])
b_conv2 = bias_variable([64])
h_conv2 = tf.nn.relu(conv2d(h_pool1, W_conv2) + b_conv2)
h_pool2 = max_pool_2x2(h_conv2)
#h_pool2 = tf.nn.dropout(h_pool2, dropout)

W_conv3 = weight_variable([5, 5, 64, 128])
b_conv3 = bias_variable([128])
h_conv3 = tf.nn.relu(conv2d(h_pool2, W_conv3) + b_conv3)
h_pool3 = max_pool_2x2(h_conv3)
#h_pool3 = tf.nn.dropout(h_pool3, dropout)

W_fc1 = weight_variable([8 * 8 * 128, 1024])
b_fc1 = bias_variable([1024])
h_pool3_flat = tf.reshape(h_pool3, [-1, 8*8*128])
h_fc1 = tf.nn.relu(tf.matmul(h_pool3_flat, W_fc1) + b_fc1)

keep_prob = tf.placeholder(tf.float32)
h_fc1_drop = tf.nn.dropout(h_fc1, keep_prob)

W_fc2 = weight_variable([1024, 2])
b_fc2 = bias_variable([2])

y_conv = tf.matmul(h_fc1_drop, W_fc2) + b_fc2

cross_entropy = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(labels=y_, logits=y_conv))
train_step = tf.train.AdamOptimizer(1e-4).minimize(cross_entropy)
correct_prediction = tf.equal(tf.argmax(y_conv,1), tf.argmax(y_,1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
init = tf.initialize_all_variables()

result = tf.argmax(y_conv,1)     #the prosessing result
result2 = y_conv              #the prosessing result

saver = tf.train.Saver()


with tf.name_scope('loss'):
    cross_entropy = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(labels=y_, logits=y_conv))
    tf.scalar_summary('loss',cross_entropy)
with tf.name_scope('train'):
    train_step = tf.train.AdamOptimizer(0.0001).minimize(cross_entropy)
correct_prediction = tf.equal(tf.argmax(y_conv,1), tf.argmax(y_,1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
saver = tf.train.Saver()
sess = tf.Session()
merged = tf.merge_all_summaries()
writer = tf.train.SummaryWriter("logs/", sess.graph)
init = tf.initialize_all_variables()

with tf.Session() as sess:
    sess.run(init)
    for i in range(600):
        batch = data.train.next_batch(90)
        sess.run(train_step,feed_dict={x: batch[0], y_: batch[1], keep_prob: 0.7})
        if i%5 == 0:
            train_accuracy = accuracy.eval(feed_dict={x:batch[0], y_: batch[1], keep_prob: 1.0})
            print("step %d, training accuracy %g"%(i, train_accuracy))
            test_accuracy = accuracy.eval(feed_dict={x:data.test.images, y_: data.test.labels, keep_prob: 1.0})
            print("step %d, test accuracy %g"%(i, test_accuracy))
            result = sess.run(merged,feed_dict={x: batch[0], y_: batch[1], keep_prob: 0.7})
            writer.add_summary(result,i)
        
    save_path = saver.save(sess, "./save_test.ckpt")
    print("Save to path: ", save_path)
    