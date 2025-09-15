# # 딕셔너리
#     # .items, keys(), values()
# dict_1 = {
#     '국' : 100,
#     '영' : 80,
#     '수' : 88 
# }
# print(dict_1)

# # 정렬
#     # sorted()
# print(dict_1.items())
# print(dict(sorted(dict_1.items(),key=lambda data:data[1])))
# print(dict(sorted(dict_1.items(),key=lambda data:data[1],reverse=True)))
# # max()
#     # max()
# #Q.'가장 점수가 높은 학생의 이름을 출력하는 코드를 작성해 보세요.'
# scores = {
#     'Alice': 88,
#     'Bob': 95,
#     'Charlie': 91,
#     'David': 85
# }
# print(max(scores,key=scores.get))
'''--------------------'''
# enumerate()
    # 순환문에서 리스트를 감싸면 (인덱스,리스트 값) 형태로 만듬
'''학생들의 이름이 저장된 리스트가 있습니다. 이 리스트의 인덱스를 학번처럼 사용해서, 
이름을 키로, 학번을 값으로 하는 딕셔너리를 만들어 보세요.
단, 학번은 1부터 시작합니다.'''
students = ["지민", "서연", "민준", "하늘"]
students_id = {}
for i,j in enumerate(students):
    students_id[j] = i+1
print(students_id)    



# # zip()
#     # 여러개의 iterable(리스트,셋 등등) 들을 각 원소를 쌍으로 하는 집합으로 만듬
#     # (1,2), ('사과','배')
#     # [(1,'사과'),(2,'배')]
# # Q.각 학생의 이름과 점수를 묶어서 출력해 보세요.
# names = ['Alice', 'Bob', 'Charlie']
# scores = [85, 92, 78]
# print(dict(zip(names,scores)))

# # map()
#     # iterableg한 객체의 각 요소에 특정 함수를 적용
#     # map(int,['1','2']) -> [1,2]
# # Q.섭씨 온도를 화씨 온도로 변환
# # F=9/5​×C+32
# temperatures_celsius = [0, 10, 20, 30, 40]
# print(list(map(lambda data: (9/5*data)+32, temperatures_celsius)))
