def calc(*args) :
    res = 0
    print(args) 
    print('len(args) : ', len(args))
    if len(args) <2 :
        print('수를 2개 이상 입력하세요')
        return res
    
    for num in args : 
        res += num        
        
    return res

print('calc() : ', calc())