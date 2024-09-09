while True : 
    ssn = input('주민번호를 입력하세요 : ')
    ssn1 = ssn.strip()
    ssn2 = ssn1.replace('-', '')
    
    if len(ssn2) != 13 :
        print('13자리 숫자를 입력하세요.')
        continue
    
    if not ssn2.isnumeric() : 
        print('숫자만 입력하세요.')
        continue
    
    if ssn2[6] not in ['1','2','3','4'] : 
        print('형식에 맞지 않습니다.')
        continue
    
    if ssn2[6] in ['1','3'] :
        print('남자')
    else : 
        print('여자')
        
    birth = ssn2[0:2]
    if ssn2[6] in ['1','2']:
        birth = '19' + birth
    if ssn2[6] in ['3','4']:
        birth = '20' + birth
    
    age = 2024 - int(birth)
    print(f'나이 : {age}')
    
    res = input('종료 하시겠습니까?(y)')
    if res.upper() == 'Y' : 
        exit()