import matplotlib.pyplot as plt
# 한글깨짐 해결
# 맷플롭에서 사용하는 폰트를 한글폰트로 변경
from matplotlib import font_manager, rc
font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family=font_name) 

x=[1,2,3,4]
y=[2,3,4,5]
plt.plot(x,y,marker='x',color='red',linestyle='--')

x1=[2,3,4,5]
y1=[1,2,3,4]
plt.plot(x1,y1)

plt.show()

