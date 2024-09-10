def hello(name) : 
    print(name, '님 환영합니다.')

def add(a,b) : 
    return a+b

def gugudan(dan) : 
    i = 1
    while i < 10 :
        print(dan,'*',i,'=',dan * i)
        i += 1
        
def getGender() : 
    ssn = input('주민번호를 입력하세요')
    if len(ssn) != 13 :
        print('주민번호는 13자리 수입니다')
    gender = int(ssn[6])
    if gender in [1,3] : 
        print('남자')  
    elif gender in [2,4] : 
        print('여자')
    else :
        print('제대로 입력하시지')
        
def getAll(name, ssn) : 
    birth = int(ssn[0:2])
    gender = int(ssn[6])
    if gender in [1,3] :
        gender = '남자'
    elif gender in [2,4] : 
        gender = '여자'
    
    print(f'당신은 {gender}, {birth}년생, {name}입니다.')
    
    
# def calc(*args) :
#     res = 0
#     print(args) 
#     print('len(args) : ', len(args))
#     if len(args) <2 :
#         print('수를 2개 이상 입력하세요')
#         return res
    
#     for num in args : 
#         res += num        
        
#     return res

def calc(operator, num1, num2) :
    if operator == '+' :
        return num1 + num2
    if operator == '-' :
        return num1 - num2
    if operator == '*' : 
        return num1 * num2
    if operator == '/' :
        return num1 / num2
    else :
        print('연산자를 입력하세요')
    
def avg(*nums) :
    sum = 0
    for num in nums : 
        sum += num
    return sum/len(nums)

hello('재헌')
gugudan(5)
getAll('재헌','9507081030310')
print(calc('*', 1, 2))
print(avg(1,2,3,4))