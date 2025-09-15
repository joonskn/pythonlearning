# 사용자로부터 점수를 입력 받아서 A,B,C,D,F 학점 출력
score = int(input('총점을 입력하세요: '))
print(f'귀하의 총점은 {score}점 입니다')

if score >= 90:
    print('A')
elif score >= 80:
    print('B')
elif score >= 70:
    print('C')
elif score >= 60:
    print('D')
elif 60> score:
    print('F')