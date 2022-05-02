class Zapangi:
    
    def __init__(self):
        self.p = {'우유':300, '콜라':500, '사이다':400, '환타':600}
        self.n = {1:'우유', 2:'콜라', 3:'사이다',4:'환타'}
        self.milk = 0
        self.cola = 0
        self.cider = 0
        self.fanta = 0
        self.money = 0      
    
    def menu(self):
        print('[메뉴정보]')
        i = 1
        for k, v in self.p.items():
            print(str(i)+'.', k, v, '원')
            i+=1
        print()
 
 
    def inputmoney(self):
        while True:
            try:
                self.money += int( input('돈 투입:') )
            except Exception as e:
                print(e)
                continue
            else:
                print('투입금액:', self.money)
                print()
                break
 
    def buy(self):
        try:
            n = int(input('번호선택(종료:0):'))
        except Exception as e:
            print(e)
        if self.money > 1999:
            print("돈이 초과되었습니다.")
            return False
        else:
            if n == 0:
                return False       
 
            elif n == 1:
                self.milk += 1
                if self.money >= self.p[ self.n[n] ]:
                    print( self.n[n], '구입완료' )
                    self.money = self.money - self.p[ self.n[n] ]
                    print('잔액:', self.money)
                else:
                    print('잔액부족')
                    self.inputmoney()
            elif n == 2:
                self.cola += 1
                if self.money >= self.p[ self.n[n] ]:
                    print( self.n[n], '구입완료' )
                    self.money = self.money - self.p[ self.n[n] ]
                    print('잔액:', self.money)
                else:
                    print('잔액부족')
                    self.inputmoney()
            elif n == 3:
                self.cider += 1
                if self.money >= self.p[ self.n[n] ]:
                    print( self.n[n], '구입완료' )
                    self.money = self.money - self.p[ self.n[n] ]
                    print('잔액:', self.money)
                else:
                    print('잔액부족')
                    self.inputmoney()
            elif n == 4:
                self.fanta += 1
                if self.money >= self.p[ self.n[n] ]:
                    print( self.n[n], '구입완료' )
                    self.money = self.money - self.p[ self.n[n] ]
                    print('잔액:', self.money)
                else:
                    print('잔액부족')
                    self.inputmoney()
            else:
                print('잘못된 번호')
 
        return True
    def select(self):
        print('구매한 우유: ', self.milk,'개')
        print('구매한 콜라: ', self.cola,'개')
        print('구매한 사이다: ', self.cider,'개')
        print('구매한 환타: ', self.fanta,'개')  
        
z = Zapangi()
z.menu()
z.inputmoney()
z.select()  

while z.buy():    
    print()
 
print('자판기 종료')
print('반환 : ', z.money, '원')

while z.select():
    print()