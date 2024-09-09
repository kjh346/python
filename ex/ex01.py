while True:
    height = float(input('키 입력(m) : '))
    weight = float(input('몸무게 입력(kg) : '))
    bmi = weight/height/height
    print(bmi)
    if bmi > 25:
        print('비만')
    elif bmi > 23:
        print('과체중')
    elif bmi > 18.5:
        print('정상')
    else:
        print('저체중')
    if bmi == 0:
        break