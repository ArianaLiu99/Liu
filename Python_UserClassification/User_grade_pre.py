
# coding: utf-8



#Integrate the twelve results of each user
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
print(pre_result)
print(pre_results)



#Voting method
user_grade_pre=[]

for i in range (0,544):
    inde=[0,0,0,0,0]
    for j in range (0,12):
        if (int(pre_results[i][j])==0):
            inde[0]+=1
        elif (int(pre_results[i][j])==1):
             inde[1]+=1
        elif (int(pre_results[i][j])==2):
             inde[2]+=1
        elif (int(pre_results[i][j])==3):
             inde[3]+=1
        else:
             inde[4]+=1
    
    if(inde.index(max(inde))==0):
        user_grade_pre.append(0)
    elif(inde.index(max(inde))==1):
        user_grade_pre.append(1)
    elif(inde.index(max(inde))==2):
        user_grade_pre.append(2)
    elif(inde.index(max(inde))==3):
        user_grade_pre.append(3)
    else:
        user_grade_pre.append(4)
    
print(user_grade_pre)    



#Read the original labels from raw data
import xlrd
import xlwt
import numpy as np
data1 = xlrd.open_workbook('rawdata.xls')
table1 = data1.sheets()[0]

user_label = []
for r in range(59004,65535):
    l_value=[]
    row =table1.row_values(r)
    for c in range(13,14):
        l_value.append(row[c])
    user_label.append(l_value)
user_labels=np.array(user_label)
print(user_labels)



print(user_labels[0])
print(user_labels.shape)


step = 12
user_labels2 = [user_labels[i:i+step] for i in range(0,len(user_labels),step)]
print(user_labels2[0])
print(np.array(user_labels2).size)
print(user_labels2[0][1])
print(int(user_labels2[0][1]))



#Voting method
user_grade_label=[]

for i in range (0,544):
    inde1=[0,0,0,0,0]
    for j in range (0,12):
        if (int(user_labels2[i][j])==0):
            inde1[0]+=1
        elif (int(user_labels2[i][j])==1):
             inde1[1]+=1
        elif (int(user_labels2[i][j])==2):
             inde1[2]+=1
        elif (int(user_labels2[i][j])==3):
             inde1[3]+=1
        else:
             inde1[4]+=1
    
    if(inde1.index(max(inde1))==0):
        user_grade_label.append(0)
    elif(inde1.index(max(inde1))==1):
        user_grade_label.append(1)
    elif(inde1.index(max(inde1))==2):
        user_grade_label.append(2)
    elif(inde1.index(max(inde1))==3):
        user_grade_label.append(3)
    else:
        user_grade_label.append(4)
    
print(user_grade_label)   
print(np.array(user_grade_label).size)


#Result comparation, get the accuracy rate
accu_pre=0
for i in range (0,544):
    if user_grade_pre[i]==user_grade_label[i]:
        accu_pre+=1
acc_rate_pre=accu_pre/544
print("The prediction accuracy rate of the prediction model is ", acc_rate_pre)