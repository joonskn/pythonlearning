import random
list_a = random.sample(range(11),7) # 0~10 중 중복되지 않은 임의의 7개
list_b = random.sample(range(11),7)

# 중복을 허용하면서 0~10 임의의 7개 추출
# random.randint(0,10) -> 임의의 1개
list_c = []
for _ in range(7):
    list_c.append(random.randint(0,10))

# 합집합
    # 사용연산자 | (파이프) -> or
set_a = {1,2,3}
set_b = {3,4,5}
unio_set = set_a | set_b
print(unio_set)
    # 메서드 .unio()
unio_set1 = set_a.union(set_b)
print(unio_set1)


# 교집합
#   연산자 & -> and
#   메서드 .inetsection()
set_a, set_b = {1,2,3,4} , {2,3,5}
print(set_a&set_b)
print(set_a.intersection(set_b))

# 차집합
#   연산자 -
print(set_a-set_b)
#   메서드 .differrence()
print(set_a.difference(set_b))