f = open('ex/2.연설문.txt', 'r', encoding='utf-8')
# print(f.read())

dic = {}
while True : 
    line = f.readline()
    
    if not line : 
        break
    line.replace('\n','').replace('.','').replace(',','')
    word_list = line.split(' ')
    
    for word in word_list :
        if word in dic :
            dic[word] += 1
        else :
            dic[word] = 1
    
    
sorted(dic.items())
print(dic)