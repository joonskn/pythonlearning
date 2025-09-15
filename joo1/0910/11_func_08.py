# 간단한 함수
# 함수 내의 로직이 한술로 표현 가능한 함수
def my_add(a,b):
    return a+b

# 람다 함수 -> 한줄로 표현한 함수 제작 키워드 lambda
# 간단한 함수를 즉석에서 만들 때 유용(쓰고나면 버림)
# 이름 없이 구현(기능만)
# 특징 무조건 값을 티런하는 함수 -> return 사용 안함
test = lambda a,b: a+b

a,b = 10, 20
print(f'{a}+{b} = {test(a,b)}')

