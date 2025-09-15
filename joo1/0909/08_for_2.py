# 0~100 사이의 랜덤한 숫자 10개를 리스트로 저장
import random
numbers = random.sample(range(100),10)

# 짝수만 출력
print(numbers)

# numbers 데이터 중에 짝수만 찾아서 새로운 리스트에 저장
# 1. 리스트를 순환한다
# 2. 순환하면서 각 데이터가 짝수인지 판단한다
# 3. 짝수이면 미리 준비한 리스트에 추가한다
# 4. 순환이 끝나면 리스트 출력 및 len으로 확인

even_num = []

for i in numbers:
    if i  % 2 == 0:
        even_num.append(i)

print(f'짝수 리스트는 {even_num}이고, 총 {len(even_num)}개 입니다.')
