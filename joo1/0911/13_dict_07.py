# enumerate, zip, items, keys, values
# map, 정렬 -> 람다함수
# 함수의 파라매터 키워드파라메터, 가변키워드 파라메터

list_a = ['사과','포도','딸기']
for index,value in enumerate(list_a):
    print(f'{index}:{value}')
# list_a = ['사과','포도','딸기']
# for i in enumerate(list_a):
#     print(i)

# index,value = (0,'포도')
# for idx,data in enumerate(list_a):
#     print(f'idx = {idx} data={data}')

# names = ['홍길동','이순신']
# age = [25,35]
# print(list(zip(names,age)))
# print(dict(zip(names,age)))

# for name, age in zip(names, age):
#     print(f'name={name},age={age}')

# # .items()
# dict_1 = {'취미':'수영','좋아하는 음식':'떡볶이'}
# print(f'dict_1 = {dict_1}')
# print(f'keys() = {dict_1.keys()}')
# print(f'values() = {dict_1.values()}')
# print(f'items = {dict_1.items()}')
