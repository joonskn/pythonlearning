# def change(obj):
#     obj[0] = 100

# data = [1,2,3]
# change(data)
# print(data)

# a = 10
# b = a
# b = 1000
# print(f'a={a}, b={b}')

# 얕은 복사: 변수는 리스트의 좌표값 1개를 같는다 -> b에 a의 좌표값을 삽입 -> 결론 같은 리스트
# 깊은 복사: 뒤에 .copy()
list_a = [1,2,3]
list_b = list_a.copy()
list_b[0] = 100
print(f'list_a={list_a}, list_b={list_b}')

