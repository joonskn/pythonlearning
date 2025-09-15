# 논리 연산자를 사용
# 나이가 18이상(성인) 이면서 주민번호를 가진사람은 "입장가능" "입장불가"
has_id = True
age = int(input('나이:'))

if has_id and age>=18:
    print('입장가능')
else:
    print('입장불가능')