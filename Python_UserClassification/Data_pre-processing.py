
# coding: utf-8

#import packages
import numpy as np
import scipy
import scipy.cluster.hierarchy as sch
from scipy.cluster.vq import vq,kmeans,whiten
import matplotlib.pylab as plt
dataset = np.loadtxt('rawdata.csv', delimiter=",")
points = dataset[:,2:12]

data=whiten(points)
#centroid = kmeans(data,max(cluster))[0]  
centroid = kmeans(data,5)[0]
print (centroid)

label=vq(data,centroid)[0]

num = [0,0,0,0,0]
for i in label:
    if(i == 0):
        num[0] = num[0] + 1
    elif(i == 1):
        num[1] = num[1] + 1
    elif(i == 2):
        num[2] = num[1] + 1
    elif(i == 3):
        num[3] = num[1] + 1
    else:
        num[4] = num[1] + 1
print ('num =',num)       
print ("Final clustering by k-means:\n",label)

from xlutils.copy import copy
import xlrd

# download the existing xls
old_workbook = xlrd.open_workbook('rawdata.xls')

# copy the existing excel to a new excel
new_workbook = copy(old_workbook)

# obtain the sheet
new_worksheet = new_workbook.get_sheet(0)

# write data
data=xlrd.open_workbook('rawdata.xls')
sheet1=data.sheets()[0]

for colIn in range(0,sheet1.nrows):
    new_worksheet.write(colIn,13,str(label[colIn]))   
    
# save the new xls
new_workbook.save('rawdata.xls')



# Dataset separating

import xlrd
import xlwt
data=xlrd.open_workbook('rawdata.xls')
table=data.sheets()[0]
print(table.nrows)
print(table.ncols)


f=xlwt.Workbook()
row0 = ["ID","Month","Cate","Point","TimeL","C","M","W","C1","C2","M1","Up","Down","Label_KM"]
sheet1=f.add_sheet('Jan',cell_overwrite_ok=True)
for c in range(0,len(row0)):
    sheet1.write(0,c,row0[c])
    
sheet2=f.add_sheet('Feb',cell_overwrite_ok=True)
for c in range(0,len(row0)):
    sheet2.write(0,c,row0[c])
    
sheet3=f.add_sheet('Mar',cell_overwrite_ok=True)
for c in range(0,len(row0)):
    sheet3.write(0,c,row0[c])

sheet4=f.add_sheet('Apr',cell_overwrite_ok=True)
for c in range(0,len(row0)):
    sheet4.write(0,c,row0[c])

sheet5=f.add_sheet('May',cell_overwrite_ok=True)
for c in range(0,len(row0)):
    sheet5.write(0,c,row0[c])

sheet6=f.add_sheet('Jun',cell_overwrite_ok=True)
for c in range(0,len(row0)):
    sheet6.write(0,c,row0[c])

sheet7=f.add_sheet('Jul',cell_overwrite_ok=True)
for c in range(0,len(row0)):
    sheet7.write(0,c,row0[c])

sheet8=f.add_sheet('Aug',cell_overwrite_ok=True)
for c in range(0,len(row0)):
    sheet8.write(0,c,row0[c])

sheet9=f.add_sheet('Sep',cell_overwrite_ok=True)
for c in range(0,len(row0)):
    sheet9.write(0,c,row0[c])

sheet10=f.add_sheet('Oct',cell_overwrite_ok=True)
for c in range(0,len(row0)):
    sheet10.write(0,c,row0[c])

sheet11=f.add_sheet('Nov',cell_overwrite_ok=True)
for c in range(0,len(row0)):
    sheet11.write(0,c,row0[c])

sheet12=f.add_sheet('Dec',cell_overwrite_ok=True)
for c in range(0,len(row0)):
    sheet12.write(0,c,row0[c])

f.save('data_sep.xls')


newdata=xlrd.open_workbook('data_sep.xls')
ntable1=newdata.sheets()[0]
ntable2=newdata.sheets()[1]
ntable3=newdata.sheets()[2]
ntable4=newdata.sheets()[3]
ntable5=newdata.sheets()[4]
ntable6=newdata.sheets()[5]
ntable7=newdata.sheets()[6]
ntable8=newdata.sheets()[7]
ntable9=newdata.sheets()[8]
ntable10=newdata.sheets()[9]
ntable11=newdata.sheets()[10]
ntable12=newdata.sheets()[11]


row=0
r1=1;r2=1;r3=1;r4=1;r5=1;r6=1;r7=1;r8=1;r9=1;r10=1;r11=1;r12=1;
for i in range (0,table.nrows):
    if (table.cell(i,1).value)== 201701.0:  
#        print(table.row_values(i))       
        for colIndex in range(0,table.ncols):
            sheet1.write(r1,colIndex,table.cell(i,colIndex).value)
#            print(r1)
#            print(table.cell(i,colIndex).value) 
        r1=r1+1
    elif (table.cell(i,1).value)== 201702.0:     
        for colIndex in range(0,table.ncols):
            sheet2.write(r2,colIndex,table.cell(i,colIndex).value)
        r2=r2+1
    elif (table.cell(i,1).value)== 201703.0:          
        for colIndex in range(0,table.ncols):
            sheet3.write(r3,colIndex,table.cell(i,colIndex).value)
        r3=r3+1
    elif (table.cell(i,1).value)== 201704.0:
        for colIndex in range(0,table.ncols):
            sheet4.write(r4,colIndex,table.cell(i,colIndex).value)
        r4=r4+1
    elif (table.cell(i,1).value)== 201705.0:  
        for colIndex in range(0,table.ncols):
            sheet5.write(r5,colIndex,table.cell(i,colIndex).value)
        r5=r5+1
    elif (table.cell(i,1).value)== 201706.0:  
        for colIndex in range(0,table.ncols):
            sheet6.write(r6,colIndex,table.cell(i,colIndex).value)
        r6=r6+1
    elif (table.cell(i,1).value)== 201707.0:  
        for colIndex in range(0,table.ncols):
            sheet7.write(r7,colIndex,table.cell(i,colIndex).value)
        r7=r7+1
    elif (table.cell(i,1).value)== 201708.0:  
        for colIndex in range(0,table.ncols):
            sheet8.write(r8,colIndex,table.cell(i,colIndex).value)
        r8=r8+1
    elif (table.cell(i,1).value)== 201709.0:  
        for colIndex in range(0,table.ncols):
            sheet9.write(r9,colIndex,table.cell(i,colIndex).value)
        r9=r9+1
    elif (table.cell(i,1).value)== 201710.0:  
        for colIndex in range(0,table.ncols):
            sheet10.write(r10,colIndex,table.cell(i,colIndex).value)
        r10=r10+1
    elif (table.cell(i,1).value)== 201711.0:  
        for colIndex in range(0,table.ncols):
            sheet11.write(r11,colIndex,table.cell(i,colIndex).value)
        r11=r11+1
    elif (table.cell(i,1).value)== 201712.0:  
        for colIndex in range(0,table.ncols):
            sheet12.write(r12,colIndex,table.cell(i,colIndex).value)
        r12=r12+1
#    row=row+1

f.save('data_sep.xls')

print ('OK')

