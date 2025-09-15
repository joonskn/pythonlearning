# 딕셔너리 CRUD

# 딕셔너리의 생성
dict_s = {
    "중식" : "칠리새우",
    "한식" : "새우전",
    "일식" : "에비텐"
}
# 딕셔너리에서 값을 출력
print(dict_s)
print('-'*10)
# 딕셔너리에서 값을 추가
dict_s['스페인'] = '감바스'
print(dict_s)
print('-'*10)
# 딕셔너리에서 삭제
del dict_s['일식']
print(dict_s)
print('-'*10)
# 딕셔너리 특정 키의 데이터를 수정
dict_s['중식'] = "향라대하"
print(dict_s)
print('@'*10)

my_bag ={'필통':'파란색', '공책':'수학공책', '지갑':'분홍색'}
# 출력
print(my_bag)
# 공책 출력
print(my_bag['공책'])
# 지갑을 가죽지갑으로 변셩
my_bag['지갑'] = '가죽지갑'
# 하얀 물통 추가
my_bag['물통'] = '하얀색'
# 공책을 버려
del my_bag['공책']
print('-'*10)
print(my_bag)
print('@'*10)

# 순환문과 연결
for i in my_bag:
    print(f'key = {i} : value= {my_bag[i]}')










# enumerate(), zip(), items(), keys(), values()
# map(), 정렬 -> 람다함수를 적용 
# 함수의 파라메터, 키워드파라메터, 가변 키워드 파라메터