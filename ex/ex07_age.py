def input_jumin():
    while True : 
        a = input("주민등록번호를 입력하세요 : ")
        if len(a) == 13 and a.isdigit() :
            return a
        else :
            print('13자리 숫자를 입력하세요')
            
b = input_jumin()
print(f'입력된 주민번호 = {b}')

def count_jumin(b):
    birth = int(b[:2])
    gender = int(b[6])
    if gender in [1, 2] :
        c = 2024 - (birth + 1900)
    elif gender in [3, 4] : 
        c = 2024 - (birth + 2000)
    else : 
        print('주민등록번호 형식이 아닙니다.')
        exit()
    
    if gender in [1, 3] : 
        d = '남자'
    elif gender in [2, 4] :
        d = '여자'
    else :
        print('주민등록번호 형식이 아닙니다.')
        exit()
    
    return c, d

c, d = count_jumin(b)
print(f'{c}살, {d}')