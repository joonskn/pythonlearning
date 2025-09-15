# 딕셔너리 정실을 이용한 리스트의 요소를 카운트
# max함수를 이용해서 기준을 value로 바꿔서 가장 큰 value에 해당하는 키
# aothem .get() 사ㅛㅇ

# 키를 이용해서 값을 가져오는 방법
dict_1 = {'사과':10, '포도':20}
# 포도읙밧
print(dict_1['포도']) #인덱스방시
print(dict_1.get('포도'))
print(dict_1.get('포도',0))

# 자료구조에서 가장 큰 값을 찾는 내장함수(내장함수) max
print(max(dict_1,key=dict_1.get))

# 정렬
list_1 = [5,3,54,2]
print(sorted(list_1))
print(sorted(list_1,reverse=True)) #역순 방법 1
print(sorted(list_1)[::-1]) #역순 방법 2

# dict
dict_1 = {'국어':80,'국사':100,'영어':98,'수학':88}
print(sorted(dict_1)) #키 기준으로
print(sorted(dict_1, key=dict_1.get)) #value를 기준으로 키를 정려
