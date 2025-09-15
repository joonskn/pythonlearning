# deict
# 키와 값의 쌍으로 구성 {key:value,key:value}
# 순서 X (set의 성질)
# 키는 중복 안됨
# 키는 변하지 않는 자료형만 가능(문자열,숫자,튜플)
# CRUD 가능
# 접근법 : 키값으로(인덱스X)
# C(크리에이트)
student = {
    "name" : "홍길동",
    "age" : 20,
    "major" : "컴퓨터"
}

# R(리드)
print(f"student['name'] = {student['name']}")

# U(업데이트)
student['name'] = '이순신'
print(f"student['name'] = {student['name']}")

# D(딜리트)
del student["name"]
print(f"student = {student}")

# 추가 = 업데이트
student['addr'] = '서울시 강남구'
print(f"student = {student}")