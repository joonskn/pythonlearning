# 선거시스템
# 유권자 들은 기호로 투표, 결과를 리스트에 저장
#  ex 1,2,3
# 투표는 순환문을 이용해서 유권자가 10명이라면 10번 순환 후보자(1~5) 선택
# 리스트에 있는 각 번호의 회수를 구해서 당선자를 출력

cadidate = ['홍길동','이순신','강감찬','율곡','신사임당']
vote = []
counts = 10
result = {}

def test(data,key):
    for i in data:
        ket(1)

# for _ in range(counts):
#     vote.append(int(input('투표하자(1~5): ')))

vote = [1,2,3,4,5,1,2,3,1,1]

# 딕셔너리
for i in vote:
    if i in result:
        result[i] += 1
    else:
        result[i] = 1
print(f'result ={result}')

# 키의 값을 가져올 때, 딕셔너변수[키값] <-없으면 에러
# 딕셔너리변수,get('키값)<-_없어도 에러는 아님
max_key = max(result,key=result.get)
print(f'당선자 : {cadidate[max_key-1]} 득표수 : {result[max_key]}')

# 빈도수 세주는 기능
import collections
datas =[1,2,3,1,2,3,4,2,1]
print(collections.Counter(datas))
# conter라는 형식이라 dict로 감싸줘야 한다
print(dict(collections.Counter(datas)))