f= open('ex/강수량.csv', 'r', encoding='utf-8')

while True : 
    line = f.readline()
    print(line)
    
    a,b,c = line.split(',')
    print(f'{a} {b} {c}')
    
    if not line : break