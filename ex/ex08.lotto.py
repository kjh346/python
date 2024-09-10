import random

while True : 
    lotto = []
    i = 0
    while len(lotto) < 6 : 
        a = random.randint(1,47)
        if a in lotto : 
            continue
        else :
            lotto.append(a)

    print(lotto)
    
