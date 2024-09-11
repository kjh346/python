f= open('ex/강수량.csv', 'r', encoding='utf-8')

x=[]
y=[]
while True : 
    line = f.readline()
    print(line)
    if not line : break
    
    a,b,c = line.split(',')
    x.append(a)
    y.append(c.replace('\n', ''))
    
    
    
print(x)
print(y)