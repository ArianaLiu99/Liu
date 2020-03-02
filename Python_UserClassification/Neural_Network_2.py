
# coding: utf-8


#!/usr/bin/python3

import tensorflow as tf
import numpy as np

result = []
def make_layer(inputs, in_size, out_size, activate=None):
    weights = tf.Variable(tf.random_normal([in_size, out_size]))
    basis = tf.Variable(tf.zeros([1, out_size]) + 0.1)
    result = tf.matmul(inputs, weights) + basis
    if activate is None:
        return result
    else:
        return activate(result)



import numpy as np
import xlrd
data = xlrd.open_workbook('data_sep.xls')
table = data.sheets()[1]
print (table.nrows,table.ncols)
print("The number of the train set is", round(table.nrows*0.9))
print("The number of the test set is", round(table.nrows*0.1))



#moving data from the previous sheet
from xlutils.copy import copy
import xlrd

old_workbook = xlrd.open_workbook('data_sep.xls')
new_workbook = copy(old_workbook)

new_worksheet = new_workbook.get_sheet(1)

data=xlrd.open_workbook('data_sep.xls')
sheet1=data.sheets()[0]
cols0=sheet1.col_values(13)

new_worksheet.write(0,14,"Label_pre")
for colIn in range(1,4918):
    new_worksheet.write(colIn,14,cols0[colIn])   
    
new_workbook.save('data_sep.xls')



train_start=1  #train staring row
train_end=4918  #train end row 
rows=train_end-train_start
train_values=[]
for x in range(train_start,train_end):
    t_values=[]
    row =table.row_values(x)
    for i in range(2,14):
        t_values.append(row[i])
    train_values.append(t_values)

train_data=np.array(train_values)

train_values1=[]
for y in range(train_start,train_end):
    t_values1=[]
    row =table.row_values(y)
    for j in range(13,14):
        t_values1.append(row[j])
    train_values1.append(t_values1)
train_label=np.array(train_values1)

test_start=4919  #test starting row
test_end=5463  #test end row 
rows=test_end-test_start
test_values=[]
for m in range(test_start,test_end):
    te_values=[]
    row =table.row_values(m)
    for z in range(2,14):
        te_values.append(row[z])
    test_values.append(te_values)
test_data=np.array(test_values)

test_values1=[]
for n in range(test_start,test_end):
    te_values1=[]
    row =table.row_values(n)
    for k in range(13,14):
        te_values1.append(row[k])
    test_values1.append(te_values1)
test_label=np.array(test_values1)



class BPNeuralNetwork:
    def __init__(self, session):
        self.session = session
        self.loss = None
        self.optimizer = None
        self.input_n = 0
        self.hidden_n = 0
        self.hidden_size = []
        self.output_n = 0
        self.input_layer = None
        self.hidden_layers = []
        self.output_layer = None
        self.label_layer = None

    def setup(self, layers):
        # set size args
        if len(layers) < 3:
            return
        self.input_n = layers[0]
        self.hidden_n = len(layers) - 2  # count of hidden layers
        self.hidden_size = layers[1:-1]  # count of cells in each hidden layer
        self.output_n = layers[-1]

        # build network
        self.input_layer = tf.placeholder(tf.float32, [None, self.input_n])
        self.label_layer = tf.placeholder(tf.float32, [None, self.output_n])
        # build hidden layers
        in_size = self.input_n
        out_size = self.hidden_size[0]
        self.hidden_layers.append(make_layer(self.input_layer, in_size, out_size, activate=tf.nn.tanh))
        for i in range(self.hidden_n-1):
            in_size = out_size
            out_size = self.hidden_size[i+1]
            inputs = self.hidden_layers[-1]
            self.hidden_layers.append(make_layer(inputs, in_size, out_size, activate=tf.nn.tanh))
        # build output layer
        self.output_layer = make_layer(self.hidden_layers[-1], self.hidden_size[-1], self.output_n)

    def train(self, cases, labels, limit=50, learn_rate=0.05):
        self.loss = tf.reduce_mean(tf.reduce_sum(tf.square((self.label_layer - self.output_layer)), reduction_indices=[1]))
        self.optimizer = tf.train.GradientDescentOptimizer(learn_rate).minimize(self.loss)

        self.session.run(tf.initialize_all_variables())
        for i in range(limit):
            self.session.run(self.optimizer, feed_dict={self.input_layer: cases, self.label_layer: labels})

    def predict(self, case):
        return self.session.run(self.output_layer, feed_dict={self.input_layer: case})

    def test(self):
        x_data = train_data
        y_data = train_label
        self.setup([12, 20, 10, 1]) 
        self.train(x_data, y_data)            

        for m in range(0,544):
            self.train(x_data, y_data)
            t_data = np.array([test_data[m]])
            result.append(self.predict(t_data))   
            print(self.predict(t_data))
        
        print("Finish training.")



def main():
    with tf.Session() as session:
        model = BPNeuralNetwork(session)
        model.test()

if __name__ == '__main__':
    main()


for i in range(0,544):
    if result[i]<=0.5:
        result[i]=0
    elif result[i]<=1.5:
        result[i]=1
    elif result[i]<=2.5:
        result[i]=2
    elif result[i]<=3.5:
        result[i]=3    
    else:
        result[i]=4
        
print(result)


#accuracy rate
accu2=0
for i in range (0,544):
    if int(test_label[i])==result[i]:
        accu2+=1
acc_rate2=accu2/544
print("The prediction accuracy rate of the second month is ", acc_rate2)



#Adding result to the data
from xlutils.copy import copy
import xlrd

old_workbook = xlrd.open_workbook('data_sep.xls')
new_workbook = copy(old_workbook)
new_worksheet = new_workbook.get_sheet(1)
data=xlrd.open_workbook('data_sep.xls')
sheet1=data.sheets()[1]

for colIn in range(4918,sheet1.nrows):
    new_worksheet.write(colIn,14,str(result[colIn-4919]))   
    
new_workbook.save('data_sep.xls')

