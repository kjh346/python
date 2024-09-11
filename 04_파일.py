f = open('새파일.txt', 'w')
f.close()

f = open('새파일1.txt', 'w', encoding='utf-8')
f.write('안녕하세요\n')
f.write('반가워요\n')

for i in range(1,20) :
    f.write(f'{i}번째 줄입니다.\n' )

f.close()