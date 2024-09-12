f=open('ex/2019-2024_강수량.csv','r',encoding='utf-8')
import csv
csvfile = csv.reader(f, delimiter=',')
header = next(csvfile)

x=[]
y=[]

for line in csvfile:
    yyyy,mm = line[0].split('-')
    
    x.append(mm)
    y.append(float(line[2]))
    
    if mm == '12' : 
        x = []
        y = []
