# 함수
# 함수명 add
# parameter는 2개 op1, op2
# 결과를 반환한다.

# 생성
def add(op1, op2):
    result = op1 + op2
    return result
#  사용
print(add(1,2))
numbers = [ add(10,20), add(10,20), add(10,20)]
two_num_hab = add(10,30)


# 매개변수 받아서 출력하는 함수
# 함수명 : show_number
# 매개변수 명 : data
def show_number(data):
    print(f'numbers = {data}')

show_number(add(10,30))

def aaa(a):
    return len(a)

print(aaa('아아아가나'))

def aaa2():
    a = input('글자 수 알고 싶은 단어 : ')
    print(len(a))
    

aaa2()