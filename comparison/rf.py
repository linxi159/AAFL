# -*- coding: UTF-8 -*-
import numpy as np
from sklearn.ensemble import RandomForestClassifier
import math
import random
import operator
import csv

'''
@author:hm
@time:2022.01.03
'''

class SVM(object):
    def __init__(self):
        pass

    def loadDataset(self,filename, split, trainingSet, testSet):  # 加载数据集  split以某个值为界限分类train和test
        with open(filename, 'r') as csvfile:
            lines = csv.reader(csvfile)   #读取所有的行
            dataset = list(lines)     #转化成列表
            for x in range(len(dataset)-1):
                for y in range(29):
                    dataset[x][y] = float(dataset[x][y])
                 
                #if x < split*len(dataset) :   # 将所有数据加载到train和test中
                #    trainingSet.append(dataset[x])
                #else:
                #    testSet.append(dataset[x])
                        
                if random.random() < split:   # 将所有数据加载到train和test中
                    trainingSet.append(dataset[x])
                else:
                    testSet.append(dataset[x])
   
    def Run(self):
        trainingSet = []
        testSet = []
        split = 0.7
        self.loadDataset(r'GSE72056_melanoma_single_cell_revised_v2_gene_filtering_ben3388mal1257_deg_ben_mal_top14.csv', split, trainingSet, testSet)   #数据划分
        print('Train set: ' + str(len(trainingSet)))
        print('Test set: ' + str(len(testSet)))

        x_train, y_train = np.split(trainingSet, (28, ), axis=1)
        x_test, y_test = np.split(testSet, (28, ), axis=1)
            
        clf = RandomForestClassifier()
        clf.fit(x_train, y_train)
        #print(x_train.shape)
        acc = clf.predict(x_test) == y_test.flat
        accuracy = np.mean(acc)*100.0
        print('Accuracy: ' + repr(accuracy) + '%')
        print (y_test)
        return accuracy

def data_write_csv(file_name, datas):#file_name为写入CSV文件的路径，datas为要写入数据列表
    with open(file_name,'w',newline ='') as f:
        mywrite = csv.writer(f)
        mywrite.writerow(datas)    


if __name__ == '__main__':
    b = []
    cnt = 0
    c = 0
    for x in range(100):  
        cnt = cnt + 1
        a = SVM()
        tmp = a.Run()
        b.append(tmp)
        c = c + tmp
        
    file_name_data1 = './Accuracy_top14-1_rf/Accuracy_top14_100_times_rf.csv'
    
    data_write_csv(file_name_data1, b)   
    accuracy_data1 = c/cnt
    
    #求均值
    acc_mean_d1 = np.mean(b)
    #求方差
    acc_var_d1 = np.var(b)
    #求标准差
    acc_std_d1 = np.std(b,ddof=1)

    print("均值为: %f" %(acc_mean_d1))
    print("方差为: %f" %(acc_var_d1))
    print("标准差为: %f" %(acc_std_d1))

    print('Ave_accuracy_top14_100_times_rf: ' + repr(accuracy_data1) + '%')
 

