# -*- coding: utf-8 -*-
import  numpy as np
data = []
flag=[]
fr = open("data2.csv","r")
for line in fr.readlines():
    curLine = line.strip().split(',')
    data.append([float(curLine[0])])
    flag.append(int(curLine[1]))
# 训练集和测试集
from sklearn.cross_validation import train_test_split

train_x, test_x, train_y, test_y = train_test_split(data, flag, random_state=0)
print np.mat(train_x)
