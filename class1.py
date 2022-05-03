# class1.py
#1) 클래스를 정의
class Person:
    #초기화 메서드
    def __init__(self):
        #자기 멤버변수를 초기화
        self.name = "default name"
    # 인스턴스 메서드
    def print(self):
        print("my name is {0}".format(self.name))

#2) 인스턴스 복사본 생성
p1 = Person()
p2 = Person()
p2.name = "전우치"

#3) 메서드 호출
p1.print()
p2.print()

