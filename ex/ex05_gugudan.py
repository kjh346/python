
money = input('금액을 넣어주세요 : ')
price = [800, 1300, 1500, 400, 700]
print(price)
index = input('번호를 입력해주세요')
print(price[int(index)-1])
change = int(money) - price[int(index)-1]
print(change)
coin500 = change // 500
coin100 = (change % 500) // 100
print(coin500, coin100)