import csv

f = open('ex/강수량.csv', 'r', encoding = 'utf-8')

csvfile = csv.reader(f, delimiter=',')

header = next(csvfile)
x = []
y = []

for line in csvfile : 
    # print(line)
    x.append(line[0].replace('2023-',''))
    y.append(float(line[2]))
    
import matplotlib.pyplot as plt
# 한글깨짐 해결
# 맷플롭에서 사용하는 폰트를 한글폰트로 변경
from matplotlib import font_manager, rc
font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family=font_name) 

plt.plot(x,y)
plt.show()