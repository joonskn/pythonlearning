# 변수 클래그 vs 인스턴스

class StudentMng():
    name = '홍길동' #클래스변수


s1 = StudentMng() 
s2 = StudentMng() 
s3 = StudentMng() 

# s1.name = '이순신' #인스턴스 변수
# 클래스변수    : 클래스가 기본적으로 가지고 있는 변수
# 인스턴스 변수 : 특정 객체가 가지고 있는 독립적인 변수

print(s1.name, s2.name, s3.name)
s1.name = '강감찬'
StudentMng.name ='이순신'
del s1.name
print(s1.name, s2.name, s3.name)

print(s1.__dict__)

# 클래스 변수 = 모든 객체가 참조하는 변수
# 그러나 객체가 변수를 재할당 받으면 해당 객체는 더이상 참조하지 않는다