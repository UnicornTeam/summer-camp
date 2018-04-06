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

def work(k1):
    u=1
    xx=[]
    while u<256:
        r1=0
        if u&k1:
            r1=1
        else :
            r1=0
        u<<=1
        r2=0
        if u&k1:
            r2=1
        else:
            r2=0
        u<<=1
        xx.append(r1*2+r2)
    return xx


def joint_col(k1,k2,k3,k4,k5,k6,k7,k8,k9,k10,k11,k12,k13,k14,k15,k16):
    xx = []
    x1 = []
    x1 = work(k1)
    xx.extend(x1)
    x1 = work(k2)
    xx.extend(x1)
    x1 = work(k3)
    xx.extend(x1)
    x1 = work(k4)
    xx.extend(x1)
    x1 = work(k5)
    xx.extend(x1)
    x1 = work(k6)
    xx.extend(x1)
    x1 = work(k7)
    xx.extend(x1)
    x1 = work(k8)
    xx.extend(x1)
    x1 = work(k9)
    xx.extend(x1)
    x1 = work(k10)
    xx.extend(x1)
    x1 = work(k11)
    xx.extend(x1)
    x1 = work(k12)
    xx.extend(x1)
    x1 = work(k13)
    xx.extend(x1)
    x1 = work(k14)
    xx.extend(x1)
    x1 = work(k15)
    xx.extend(x1)
    x1 = work(k16)
    xx.extend(x1)
    return xx


def cnnresult():
    with tf.Session() as sess:
        load_path = saver.restore(sess, "./save_test.ckpt")  #read the trained model
        filee = open('./fakerms1.1m1.dat','rb')
        i=1
        X=[]
        true_inf=[]
        try:
            while True:
                if(i!=65):
                    lines1=filee.read(1)
                    lines2=filee.read(1)
                    lines3=filee.read(1)
                    lines4=filee.read(1)
                    lines5=filee.read(1)
                    lines6=filee.read(1)
                    lines7=filee.read(1)
                    lines8=filee.read(1)
                    lines9=filee.read(1)
                    lines10=filee.read(1)
                    lines11=filee.read(1)
                    lines12=filee.read(1)
                    lines13=filee.read(1)
                    lines14=filee.read(1)
                    lines15=filee.read(1)
                    lines16=filee.read(1)
                    k1=ord(lines1)
                    k2=ord(lines2)
                    k3=ord(lines3)
                    k4=ord(lines4)
                    k5=ord(lines5)
                    k6=ord(lines6)
                    k7=ord(lines7)
                    k8=ord(lines8)
                    k9=ord(lines9)
                    k10=ord(lines10)
                    k11=ord(lines11)
                    k12=ord(lines12)
                    k13=ord(lines13)
                    k14=ord(lines14)
                    k15=ord(lines15)
                    k16=ord(lines16)
                    X.append(joint_col(k1,k2,k3,k4,k5,k6,k7,k8,k9,k10,k11,k12,k13,k14,k15,k16))
                    #print(i)
                    i = i + 1
                else:
                    data = np.array(X)
                    data = data.reshape(64, 64,1) / 3.
                    true_inf.append(data)
                    break
        finally:
            filee.close() 
            true_inf = np.stack(true_inf, axis = 0)
        true_inf = true_inf.reshape(1, 64, 64, 1)
        prosess_result = result.eval(feed_dict={x:true_inf, keep_prob: 1.0})
        return prosess_result  #将结果由ndarry转化为int

result = cnnresult()
if(result==0):
    message = "TRUE"
if(result==1):
    message = "FAKE"
    
print(message)