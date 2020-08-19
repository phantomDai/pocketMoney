"""
此代码主要实现的是对已经初步处理好的数据进行归一化处理
输入: 输入的数据是经过字符串转整形数字的数据
输出: 输出的数据是归一化后的数据,取值范围都在[0,1]
数据归一化方式: (a(i) - min(a)) / (max(a) - min(a))


参考网址: http://www.cnblogs.com/leoo2sk/archive/2010/09/20/k-means.html
		https://blog.csdn.net/com_stu_zhang/article/details/6987632
"""
# -*- coding:UTF-8 -*-
from __future__ import division
import numpy as np
import csv
import time
import math

# 定义初步处理好后的数据路径 定义经过归一化处理好后的数据路径
# handled_file = 'kddcup.data_10_percent_corrected.csv'
# normalization_file = 'kddcup.data_10_percent_corrected_normalization.csv'

handled_file = "kddcup.testdata.unlabeled_10_percent.csv"
normalization_file = 'kddcup.testdata.unlabeled_10_percent_normalization.csv'


def get_column_maxvalue(matrix):
    """获取训练数据中每一列的最大值"""

    temp_list = []
    for j in range(len(matrix[0])):
        one_list = []
        for i in range(len(matrix)):
            one_list.append(np.float64(matrix[i][j]))
        temp_list.append(max(one_list))
    return temp_list


def data_normalization():
    data_source = open(handled_file, 'rb')
    temp_data = np.loadtxt(data_source, delimiter=',', skiprows=0)
    data_source.close()
    # 定义存储数据的数组,便于后面进行统计
    data_array = np.array(temp_data)

    # 统计当前每一列数据中的最大值和最小值
    # 参考网址: https://blog.csdn.net/com_stu_zhang/article/details/6987632
    # 其中 num_outbound_cmds 自定义其最大连接次数为10000次,同时只对连续型特征进行处理
    # 41种特征中,共有32种连续型,9种离散型
    # maxcolums = [58329, 1379963888, 1309937401, 3, 14,
    #              101, 5, 7479, 7468, 100, 5, 9, 10000,
    #              511, 511, 1, 1, 1, 1, 1, 1, 1,
    #              255, 255, 1, 1, 1, 1, 1, 1, 1, 1
    #              # 最后一个是当前数据包类型,0为正常,其余的是异常数据包.共 22(训练出现) + 17(测试出现) + 1(正常数据) 40种类型
    #              # 所以最后一列不进行量化,只需要除以1即可
    #     , 1]
    # 因为所有的连续型特征的数据的最小值都是0,所以其归一化后的映射数据
    # 区间公式为 a(i) / max(a)

    # 转换数据类型为 float64,注意：原始测试数据在此处进行处理会报错，因为在136489和136497两条数据错误，需要删除掉
    data_temp = np.array(data_array, dtype=np.float64)

    # 获取数据的行和列
    array_row_num = len(data_temp)
    array_column_num = len(data_temp[0])

    print("rows: %d" % array_row_num)
    print("columns: %d" % array_column_num)

    # 记录每一列的最大值
    column_max_value = get_column_maxvalue(data_temp)

    data_file = open(normalization_file, 'w', newline='')
    # 获取生成文件句柄
    csv_writer = csv.writer(data_file)

    # 对所有的数据进行归一化处理
    # for column_index in range(array_column_num):
    #     line = []
    #     # array_row_num - 1 的目的是忽略最后一列的label
    #     for row_index in range(array_row_num):
    #         line.append(data_temp[column_index][row_index] / column_max_value[column_index])

    for row_index in range(0, array_row_num):
        line = []
        for column_index in range(0, array_column_num):
            if math.isclose(0.0, column_max_value[column_index], rel_tol=1e-5):
                line.append(column_max_value[column_index])
            else:
                line.append(data_temp[row_index][column_index] / column_max_value[column_index])
        # 写入到文件
        csv_writer.writerow(line)
    # 关闭文件
    data_file.close()


if __name__ == '__main__':
    print("starting...")
    start_time = time.clock()
    data_normalization()
    end_time = time.clock()
    print("Duration time:", (end_time - start_time))  # 输出程序运行时间
