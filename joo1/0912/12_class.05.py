# 학생
# 이름,,나이  학생정보 출력,\ 과목과 점수, 총점, 평균, 학점
# 변수 : 이름, 나이\ 과목과 점수, 총점, 평균 , 학점
# 함수 : 학생정보를 출력,\ 총점 함수 , 평균, 학점

students = [] # 학생들
class StudentsMng():
    def __init__(self):
        self.name = ''
        self.age = 0
    def info_student(self):
        print(f'이름 : {self.name}, 나이 : {self.age}')

s1 = StudentsMng()
s1.name = '홍길동'
s1.age = 25
students.append(s1)

s2 = StudentsMng()
s2.name = '이순신'
s2.age = 35
students.append(s2)


students[0].info_student()

print(students)