# list, set, tuple, dict
result = dict([['name','age'], ['홍길동','20']])
print(type(result))
print(result)

# 두개의 리스트 1. ket 2. vlaue
# 이걸 딕셔너리로
names = ['홍길동','이순신','강감찬']
scores = [100, 99, 98]
students = {}
# 빈 딕셔너리 생성
# 변수에['키'] = 값 형태로 생성 - 순환문을 통해서
count = 0
for name in names :
    students[name] = scores [count]
    count +=1

for i in range(len(names)):
    students[names[i]] = scores[i]

print(students)