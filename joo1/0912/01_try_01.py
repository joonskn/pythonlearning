# 오류를 피하기 -> 예외처리
#  .isdigit 숫자로만 되어있는지 확인하는 메소드
#  .split 공백(혹은 특수 지정) 기준으로 값을 나눠주는 것
#  print(,end= 프린트 맨 마지막 줄에 뭘 할지)

try:
    num1,num2 = map(int, input("공백을 기준으로 두개의 숫자를 입력>").split())

    calc_lists = [num1+num2, num1-num2, num1*num2,num1/num2]

    print('1. 더하기',end='\t')
    print('2. 빼기',end='\t\t')
    print('3. 곱하기',end='\t')
    print('4. 나누기')
    choice = int(input('원하는 결과는?'))
    print(f'결과 = {calc_lists[choice-1]}')
except:
    print('오류발생')
finally:    #트라이 구문이 외부의 리소스를 가져왔을 때 리소스 사용 종료를 위해 
    pass
print('프로그램 종료')

# print("원의 반지름:", number_input_a)
# print('원의 둘레:', 2*3.14*number_input_a)
# print('원의 넓이:', 3.14*number_input_a*number_input_a)

# 좀비프로세스,데드락