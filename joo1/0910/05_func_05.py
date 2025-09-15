# 가변매개변수
# 변수내부에서는 리스트로 간수합니다.
# 함수를 호출하는 쪽에서는 편하게 적습니다.
# 패킹,언패킹


def myFunc1(*args): #패킹이 동작
    for i in args:
        print(i)
myFunc1(10,20,50,60)

def myFunc1(args):
    for i in args:
        print(i)
myFunc1([10,20,50,60])


# 언패킹
a,b = [10,20]
print(f'a={a}')
print(f'b={b}')