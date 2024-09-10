def a() :
    a = int(input('첫 수를 입력하세요 : '))
    b = int(input('두번째 수를 입력하세요 : '))
    c = input('연산자를 입력하세요 : ')
    
    if c == '+' :
        d = a + b
    elif c == '-' :
        d = max(a,b) - min(a,b)
    elif c == '*' :
        d = a * b
    elif c == '/' :
        d = max(a,b) / min(a,b)
    elif c not in ['+','-','*','/'] :
        print('연산자를 다시 입력하세요')
    
    print(d)

