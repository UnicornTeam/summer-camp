# coding=utf-8
import os.path as path
import os
import numpy as np
from PIL import Image
import utils
from utils import DataSet
from sklearn.preprocessing import OneHotEncoder
try:
  import cPickle as pickle
except ImportError:
  import pickle

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
    #print("-----------")
    #print(xx)
    return xx

def read_data(test_rate = 0.1, one_hot=True):
    """read .dat data"""
    # read data
    true_inf = []
    fake_inf = []
    X = []
    i = 1
    filee = open('/home/summit/DDI/leftGFSK_DOWN.dat','rb')
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
                if k1+k2==0:
                    break
                X.append(joint_col(k1,k2,k3,k4,k5,k6,k7,k8,k9,k10,k11,k12,k13,k14,k15,k16))
                a = np.array(X)
                #print(i)
                i = i + 1
            else:
                data = np.array(X)
                data = data.reshape(data.shape[0], data.shape[1],1) / 3.
                X = []
                true_inf.append(data)
                i = 1
    finally:
        filee.close()        
        true_inf = np.stack(true_inf, axis = 0)
    
    X = []
    i = 1
    filee = open('/home/summit/DDI/leftGFSK_UP.dat','rb')
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
                if k1+k2==0:
                    break
                X.append(joint_col(k1,k2,k3,k4,k5,k6,k7,k8,k9,k10,k11,k12,k13,k14,k15,k16))
                a = np.array(X)
                #print(i)
                i = i + 1
            else:
                data = np.array(X)
                data = data.reshape(data.shape[0], data.shape[1],1) / 3.
                X = []
                fake_inf.append(data)
                i = 1
    finally:
        filee.close()        
        fake_inf = np.stack(fake_inf, axis = 0)
        
    # split train set and test 划分训练和数测试据集
    test_split_true_inf = np.random.rand(true_inf.shape[0]) < test_rate
    test_split_fake_inf = np.random.rand(fake_inf.shape[0]) < test_rate

    test_true_inf = true_inf[test_split_true_inf, :, :, :]
    test_label_true_inf = np.ones([test_true_inf.shape[0]])
    train_true_inf = true_inf[np.logical_not(test_split_true_inf), :, :, :]
    train_label_true_inf = np.ones([train_true_inf.shape[0]])

    test_fake_inf = fake_inf[test_split_fake_inf, :, :, :]
    test_label_fake_inf = np.ones([test_fake_inf.shape[0]])*2
    train_fake_inf = fake_inf[np.logical_not(test_split_fake_inf), :, :, :]
    train_label_fake_inf = np.ones([train_fake_inf.shape[0]])*2

    test_infs = np.concatenate((test_true_inf, test_fake_inf), axis = 0)
    train_infs = np.concatenate((train_true_inf, train_fake_inf), axis = 0)
    
    test_labels = np.concatenate((test_label_true_inf, test_label_fake_inf), axis = 0)
    train_labels = np.concatenate((train_label_true_inf, train_label_fake_inf), axis = 0)
    
    if one_hot == True:
        test_labels = test_labels.reshape(test_labels.shape[0], 1)    
        train_labels = train_labels.reshape(train_labels.shape[0], 1)
        enc = OneHotEncoder()
        enc.fit(test_labels)
        test_labels = enc.transform(test_labels).toarray()
        train_labels = enc.transform(train_labels).toarray()
    #print("test_labels")
    #print(test_labels)
    #print("test_pics")
    #print(test_pics)
    #print("train_labels")
    #print(train_labels)
    #print("train_pics")
    #print(train_pics)
    
    data = utils.get_data(train = DataSet(images = train_infs, labels = train_labels),
                    test = DataSet(images = test_infs, labels = test_labels))
    print("type(data) line156")
    print(type(data))
    return data
