# -*- coding: utf-8 -*-
data = []
flag=[]
fr = open("data2.csv","r")
for line in fr.readlines():
    curLine = line.strip().split(',')
    data.append(float(curLine[0]))
    flag.append(int(curLine[1]))



# 训练集和测试集
from sklearn.cross_validation import train_test_split

train_x, test_x, train_y, test_y = train_test_split(data, flag, random_state=0)
ccc=[]
for i in train_y:
    if i not in ccc:
        ccc.append(i)
print ccc
ccc1=[]
for i in test_y:
    if i not in ccc1:
        ccc1.append(i)
print ccc1


# 模型初始化设置
import xgbot as xgb

dtrain = xgb.DMatrix(train_x, label=train_y)
dtest = xgb.DMatrix(test_x)

# booster:
params = {'learning_rate': 0.1,
          'max_depth': 5,
          'num_boost_round':20,
          'objective': 'multi:softmax',
          'random_state': 27,
          'silent':0,
          'num_class':5,
          'eval_metric': 'mlogloss'
          }

watchlist = [(dtrain, 'train')]

# 建模与预测:NUM_BOOST_round迭代次数和数的个数一致
bst = xgb.train(params, dtrain, num_boost_round=50, evals=watchlist)
ypred = bst.predict(dtest)
print (type(ypred))
print (ypred[0])
ff = open("predict.csv", "w")
for i in range(len(test_x)):
    ff.write(str(test_x[i])+","+ str(test_y[i])+","+str(ypred[i])+ "\n")
ff.close()
# 设置阈值, 输出一些评价指标，>0.5预测为1，其他预测为0
#y_pred = (ypred >= 0.5) * 1
#
# from sklearn import metrics
#
# print ('AUC: %.4f' % metrics.roc_auc_score(test_y, ypred))
# print ('ACC: %.4f' % metrics.accuracy_score(test_y, y_pred))
# print ('Recall: %.4f' % metrics.recall_score(test_y, y_pred))
# print ('F1-score: %.4f' % metrics.f1_score(test_y, y_pred))
# print ('Precesion: %.4f' % metrics.precision_score(test_y, y_pred))
# metrics.confusion_matrix(test_y, y_pred)
#
# from pylab import mpl
#
# mpl.rcParams['font.sans-serif'] = ['SimHei']
# xgb.plot_importance(bst)

#保存模型
bst.save_model('0001.model')
#加载模型

#bst = xgb.Booster({'nthread':4}) #init model
#bst.load_model("model.bin") # load data
#预测
#bst.predict( xgmat )