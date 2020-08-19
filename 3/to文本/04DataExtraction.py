"""
本文件的作用是对 kddcup99 数据集进行部分数据提取,
由于原数据的数据量太大,个人的电脑可能无法跑完,所以
这一个步骤是非常有必要的
"""

# -*- coding:UTF-8 -*-
from __future__ import division
import numpy as np
from random import sample
from random import shuffle
import csv
import time
import pandas as pd
import random

# 定义经过归一化处理好后的原始数据路径
normalization_file = 'kddcup.data_10_percent_corrected.csv'

# 定义经过部分数据抽取后的新数据路径
extraction_file = 'data_train.csv'

# 定义数据的抽取间隔,同一个数据集的抽取,间隔尽量使用没有交集的比率,能够做到更好的泛化.如(0.17,0.13)
extraction_rate = 0.0003

def extract_data():
	# 定义存储数据的数组,便于后面进行统计
	with open(normalization_file, 'r') as data_source:
		# 获取源文件句柄
		csv_reader = csv.reader(data_source)
		# 打开输出文件
		data_file = open(extraction_file, 'w', newline = '')
		# 获取生成文件句柄
		csv_writer = csv.writer(data_file)
		
		srcdata = []
		for row in csv_reader:
			srcdata.append(np.array(row))

		print("特征数目：%d" % len(srcdata[0]))
		
		# 打乱原始数据,使得后续的操作更加具有泛化能力
		shuffle(srcdata)
		# 从打乱的原始数据中按照抽取率提取数据
		data = sample(srcdata, int(len(srcdata) * extraction_rate))
		# 将数据写入到文件中
		for row in data:
			# 读取当前行数据并写入到文件
			csv_writer.writerow(np.array(row))
		
		# 关闭文件
		data_file.close()

def get_test_cases():
	dataset = pd.read_csv('kddcup.data_10_percent_corrected.csv')
	test_cases = []
	targe_label = [0, 4, 5]
	labels = dataset.iloc[:, -1].values
	data = dataset.iloc[:, :].values
	while len(test_cases) < 11:
		index = random.randint(0, len(data) - 1)
		if labels[index] in targe_label:
			test_cases.append(data[index])
	data_file = open('testcases.csv', 'w', newline='')
	writer = csv.writer(data_file)
	for i in range(len(test_cases)):
		writer.writerow(test_cases[i])
	data_file.close()

	

if __name__ == '__main__':
	# start_time = time.clock()
	# print("Extracting...")
	# extract_data()
	# end_time = time.clock()
	# print("Duration time:", (end_time - start_time))

	get_test_cases()
