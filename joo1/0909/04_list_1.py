age = 25
array = [23, 32, 103, "문자열", True, False,{'kor':10,'eng':20}]
print(array)
array_2 = [100, array]
print(array_2)
print(array_2[-1][-1]['eng'])

temp = [
    [1,2]   # temp[0] -- row 행
    [10,20] # temp[1] -- 20 = temp[1][1] 틀린거 temp[1,1]
    [30,40]
]