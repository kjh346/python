f = open('새파일1.txt', 'r' , encoding='utf-8')

line = f.readline()
print(line)

while True : 
    line = f.readline()
    print(line)
    if not line : break
    
f.close()