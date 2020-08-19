# -*- coding: utf-8 -*-
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

from xgboost import XGBClassifier
# 模型初始化设置
from sklearn import metrics
import xgboost

clf = XGBClassifier()
import numpy as np
clf.fit(np.mat(train_x), train_y)
y_pre= clf.predict(np.mat(test_x))
y_pro= clf.predict_proba(np.mat(test_x))[:,1]
print"Accuracy : %.4g" % metrics.accuracy_score(test_y, y_pre)
print ('Recall: %.4f' % metrics.recall_score(test_y, y_pre,average='macro'))
print ('F1-score: %.4f' % metrics.f1_score(test_y, y_pre,average='macro'))
print ('Precesion: %.4f' % metrics.precision_score(test_y, y_pre,average='macro'))

ff = open("predict2.csv", "w")
for i in range(len(test_x)):
    ff.write(str(test_x[i])+","+ str(test_y[i])+","+str(y_pre[i])+ "\n")
ff.close()

#保存模型
clf.save_model('0002.model')
#加载模型

#bst = xgboost.Booster({'nthread':4}) #init model
#bst.load_model("0001.model") # load data
#预测
#bst.predict( xgmat )