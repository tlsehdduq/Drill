class Player:
    type = 'Player'

    def __init__(self):
        self.x = 100

    def where(self):
        print(self.x)

player = Player()
player.where()
#클래스 변수사용
print(Player.type)


#클래스 함수호출
Player.where()  #error// where() missing 1 required positional argument: 'self'
Player.where(player)

#객체를 찍어낼때는싱글톤처럼이용하기위해서는 맴버변수 필요없이 클래스 바로밑에 클래스변수
#글로벌 객체로써 유일하게 하나만 존재하는 객체로 생각할 수 있다.
#