a = 0
b = 0
a = int(input('수를 입력하세요 : '))
b = int(input('하나더 입력하세요 : '))
c = a + b
print(f'a + b = {c}')

str1 = '안녕하세요'
d = str1.lower()

print(d)

exit()

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


