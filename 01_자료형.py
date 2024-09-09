
list = []

while True : 
    fruit = input('과일을 입력하세요 : ')
    
    if fruit in list : 
        continue
    
    list.append(fruit)
    
    if len(list) == 5 :
        break
    
print(list)

list.sort()
print(list)

if '오렌지' not in list : 
    list.insert(3, '오렌지')
    
print(list)