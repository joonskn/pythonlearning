# kor, eng, math 각 변수에 사용자로부터 값을 받아서
# avg 변수에 평균값을 저장하고
# 조건을 평균 60이상 kor,eng, math 변수의 각 값이 40 이상일 때
# 합격을 출력하는 프로그램

kor = int(input('국어 점수'))
eng = int(input('영어 점수'))
math = int(input('수학 점수'))
avg = (kor + eng + math)/3

if avg >= 60 and kor >= 40 and eng >= 40 and math >= 40:
    print(f"귀하의 평균 점수는 {avg:.1f}이고 국영수 {kor},{eng},{math} 점으로 합격입니다")
else:
    print('불합격')
