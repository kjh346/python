
while True : 
    money = input('금액을 넣어주세요 : ')
    price = [800, 1300, 1500, 400, 700]
    print(price)
    index = input('번호를 입력해주세요')
    print(price[int(index)-1])
    change = int(money) - price[int(index)-1]
    print(f'거스름돈 : {change}')
    coin500 = change // 500
    coin100 = (change % 500) // 100
    print(f'500원 : {coin500}개, 100원 : {coin100}개')
    res = input('종료하시겠습니까 : ')
    if res == 'y' : 
        exit()

