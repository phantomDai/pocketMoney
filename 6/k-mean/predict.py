# -*- coding: utf-8 -*-
from sklearn.datasets import load_iris
import xgboost as xgb
from xgboost import plot_importance
from matplotlib import pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score   # 准确率
# 加载样本数据集
data = []
flag=[]
fr = open("flag11.csv","r")
for line in fr.readlines():
    curLine = line.strip().split(',')
    data.append([float(curLine[0]),float(curLine[1])])
    flag.append(int(curLine[2]))
X_train, X_test, y_train, y_test = train_test_split(data, flag, test_size=0.2, random_state=1234565) # 数据集分割

# 算法参数
params = {
    'booster': 'gbtree',
    'objective': 'multi:softmax',
    'num_class': 5,
    'gamma': 0.1,
    'max_depth': 6,
    'lambda': 2,
    'subsample': 0.7,
    'colsample_bytree': 0.7,
    'min_child_weight': 3,
    'silent': 1,
    'eta': 0.1,
    'seed': 1000,
    'nthread': 4,
}

plst = params.items()


dtrain = xgb.DMatrix(X_train, y_train) # 生成数据集格式
num_rounds = 500
model = xgb.train(plst, dtrain, num_rounds) # xgboost模型训练

# 对测试集进行预测
dtest = xgb.DMatrix(X_test)
y_pred = model.predict(dtest)
#保存模型结果
ff = open("predict3.csv", "w")
for i in range(len(X_test)):
    ff.write(str(X_test[i])+","+ str(y_test[i])+","+str(y_pred[i])+ "\n")
ff.close()

# 显示重要特征
plot_importance(model)
plt.show()





from sklearn import metrics

# print ('AUC: %.4f' % metrics.roc_auc_score(test_y, ypred))
print ('ACC: %.4f' % metrics.accuracy_score(y_test, y_pred))
print ('Recall: %.4f' % metrics.recall_score(y_test, y_pred,average='micro'))
print ('F1-score: %.4f' % metrics.f1_score(y_test, y_pred,average='micro'))
print ('Precesion: %.4f' % metrics.precision_score(y_test, y_pred,average='micro'))
# metrics.confusion_matrix(test_y, y_pred)
#
# from pylab import mpl
#
# mpl.rcParams['font.sans-serif'] = ['SimHei']
# xgb.plot_importance(bst)

#保存模型
model.save_model('0001.model')
#加载模型

#bst = xgb.Booster({'nthread':4}) #init model
#bst.load_model("model.bin") # load data
#预测
#bst.predict( xgmat )