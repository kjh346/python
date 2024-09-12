class 사람 :
    def cry(self, 소리) :
        for 변수 in 소리 :
            print(변수)
            
human=사람()
            
human.cry('엉엉')

class 사람1 : 
    def call(self, 이름, 번호) : 
        print(f'{이름}에게 {번호} 발신중')
        
human1 = 사람1()
human1.call('김철수','010-1234-5678')

class 사람2 : 
    def 개인정보(self, name) :
        print(name[0] + (len(name)-2)*'x' + name[-1])
        
human2 = 사람2()
human2.개인정보('유빛나라')