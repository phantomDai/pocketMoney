# -*- coding: utf-8 -*-
import xgboost as xgb
bst = xgb.Booster({'nthread':4}) #init model
bst.load_model("0001.model") # load data
from sklearn.model_selection import train_test_split
data = []
flag=[]
fr = open("data3.csv","r")
for line in fr.readlines():
    curLine = line.strip().split(',')
    data.append([float(curLine[0])])
    flag.append(int(curLine[1]))
X_train, X_test, y_train, y_test = train_test_split(data, flag, test_size=0.2, random_state=1234565) # 数据集分割
dtest = xgb.DMatrix(X_test)
pre=bst.predict( dtest )
print pre