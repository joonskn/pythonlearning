# 명령어는 모두 실행
# 조건문을 이용하면 특정 명령문은 실되지 않게 할수 있다
# 조건문 기본 양식 ' if 조건 :  
#                       들여쓰기 '
age = 20
if age >= 18:
    print('성인입니다.')
    print('조건문은 True 입니다.')
print('if 상관 없이 무조건 나옴')

# 조건에 맞으면 합격 그렇지 않으면 불합격
score = 50
if score >= 60:
    print('합격')
else:
    print('불합격')

temp = float(input('온도'))
if temp >= 30:
    print('덥다')
elif temp > 20:
    print('따뜻하다')
elif temp > 10:
    print('따뜻하다')
else:
    print('춥다')