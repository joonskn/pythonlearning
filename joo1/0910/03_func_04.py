# 다양한 매개변수
    # 기본매개변수 default parameter

def myAdd(num1=1, num2=10, num3 = 100):  # 기본 매개변수는 맨 뒤에서 부터 채워준다
    return num1+num2 + num3

result1 = myAdd()
result2 = myAdd(2)
result3 = myAdd(2,3)
result4 = myAdd(2,3,4)

print(result1, result2, result3, result4)


