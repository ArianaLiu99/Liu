
# coding: utf-8


import xlrd
import xlwt
import numpy as np
data = xlrd.open_workbook('data_sep.xls')

pre_result=[]
for x in range(4918,5462):
    one_result=[]
#    row =table.row_values(x)
    for i in range(0,12):
        table = data.sheets()[i]
        one_result.append(table.cell(x,14).value)
    pre_result.append(one_result)

pre_results=np.array(pre_result)
print(pre_results)
print(pre_results[0])



f=xlwt.Workbook()
row0 = ["month","grade"]
sheet1=f.add_sheet('User1',cell_overwrite_ok=True)
for c in range(0,2):
    sheet1.write(0,c,row0[c]) 
    
for i in range(1,13):
    sheet1.write(i,0,i)
    
for j in range (1,13):
    sheet1.write(j,1,pre_results[0][j-1])

f.save('user_grade.xls')



import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas import DataFrame,Series
from sklearn.cross_validation import train_test_split
from sklearn.linear_model import LinearRegression
 
user1 = pd.read_excel('user_grade.xls')
user1 = DataFrame(user1)
user1.head()


#scatter plot
plt.scatter(user1.month,user1.grade,color = 'red',label = "user1")
plt.xlabel("Month")
plt.ylabel("User1 Grade")
plt.show()



X_train,X_test,Y_train,Y_test = train_test_split(user1.month,user1.grade,train_size=0.8)

plt.scatter(X_train, Y_train, color="darkgreen", label="train data")
plt.scatter(X_test, Y_test, color="red", label="test data")
 
plt.legend(loc=1)
plt.xlabel("Month")
plt.ylabel("User1 Grade")
plt.show()



model = LinearRegression()

X_train = X_train.values.reshape(-1,1)
X_test = X_test.values.reshape(-1,1)
 
model.fit(X_train,Y_train)
 
a  = model.intercept_
b = model.coef_
 
y_train_pred = model.predict(X_train)
plt.plot(X_train, y_train_pred, color='blue', linewidth=2, label="best line")
 
plt.scatter(X_train, Y_train, color='darkgreen', label="train data")
plt.scatter(X_test, Y_test, color='red', label="test data")

plt.legend(loc=1)
plt.xlabel("Month")
plt.ylabel("User1 Grade")
plt.show()
 
print("Fitting parameters: intercept",a,",regression coefficient：",b)
print("Best Fitting Line: Y = ",round(a,2),"+",round(b[0],2),"* X")



import keras
import numpy as np
import matplotlib.pyplot as plt
from keras.models import Sequential
from keras.layers import Dense, Activation
from keras.optimizers import SGD

model = Sequential()

model.add(Dense(units=10, input_dim=1))
model.add(Activation('tanh'))
model.add(Dense(units=1))
model.add(Activation('tanh'))

sgd = SGD(lr=0.3)

model.compile(optimizer=sgd, loss='mse')

for step in range(3):
    cost = model.train_on_batch(user1.month,user1.grade)
    if step % 6 == 0:
        print('cost: ', cost)

W, b = model.layers[0].get_weights()
print('W：', W, ' b: ', b)
print(len(model.layers))

y_pred = model.predict(user1.month)

plt.scatter(user1.month,user1.grade)
plt.plot(user1.month,user1.grade, 'r-', lw=2, label="best line")
plt.legend(loc=1)
plt.xlabel("Month")
plt.ylabel("User1 Grade")
plt.show()



u1 = pre_results[0]
WA_result=(int(u1[0])*1+int(u1[1])*2+int(u1[2])*3+int(u1[3])*4+int(u1[4])*5+int(u1[5])*6+int(u1[6])*7+
           int(u1[7])*8+int(u1[8])*9+int(u1[9])*10+int(u1[10])*11+int(u1[11])*12)/98
print("Result of weighted average is",WA_result)
print("The user grade prediction of the first user by weighted average is ", round(WA_result))

