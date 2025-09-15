# 랜덤 라이브러리 가져오기
import random

# 랜덤 라이브러리 중 sample 함수 호출, 범위(range)에서 n개 추출
ran_num = random.sample(range(100),5)

# 범위 내의 정수 랜덤하게 1개 생성
ran_int = random.randint(0,10)

ran_num.append(ran_int)

#  50이 있는지 조사
print(50 in ran_num)
print(ran_num)

print('-'*50)

# 삭제
del ran_num[0]
print(ran_num)

removed_number = ran_num.pop(0)
print(ran_num)
print(removed_number)

# clear 
print('444')
ran_num.clear()
print(ran_num)