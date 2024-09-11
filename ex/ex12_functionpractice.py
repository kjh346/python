def gugu(dan) :
    i = 1
    result = []
    while i < 10 :
        result.append(dan * i)
        i += 1
    
    return result

result = gugu(2)
print(result)

def threeandfive() :
    sum = 0 
    for i in range(1,1001) :
        if i % 3 == 0 or i % 5 == 0:
            sum += i 
    print(sum)
 
threeandfive()

import math

def get_total_page(m, n) :
    print(math.ceil(m/n))
    
get_total_page(1000,15)