class Star:

    type = 'star'
    x = 100
    #class 변수

    def change(): #class 함수
        x = 200 #이 x는 지역변수.
        print('x is', x)

#생성자가 없고 , self 를 사용 하지 않음
#
print('x Is', Star.x)
Star.change()
print('x Is', Star.x)

star = Star()
print('x Is', star.x)
star.change()
# Error  TypeError: change() takes 0 positional arguments but 1 was given
#파이썬은 객체에 대해 객체의 함수를 호출하면 실제로, star.change(Star)이런식으로호출된다.
#객체 자기자신이 들어간다.
#def change는 파라미터를 받지 않는데 (Star)로 받ㅇㅆ기에 오류가 발생.
#꼭 위치에 self를 쓸 필요는 없다. 다만 , 그것의 의미를 명확하게 해주기 위해서 ..
#파이썬의 변수는 그자체가 포인터이다.

