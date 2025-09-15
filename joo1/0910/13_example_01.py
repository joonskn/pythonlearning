
# 규칙 : 컴퓨터가 임의로 숫자를 선택    : random 이용
# 사람이 숫자를 입력                   : input
# 승패를 기록                         : 의사코드
# 3번 마다 계속 할지 물어본다          : 순환문(지금은 while)


import c13_rule_gbv
import c13_rule_winper

i = 0
result_t = []
result_s = []

while True:
    i += 1
    com_choi = c13_rule_gbv.com_num()
    hu_choi = c13_rule_gbv.hu_num()
    c13_rule_gbv.gbv(com_choi,hu_choi)
    c13_rule_winper.gbv_result(com_choi,hu_choi,result_t,result_s)
    if i % 3 == 0:
        is_continue = input('더 할래? 할거면 (Y/y) ').upper()
        if not is_continue == 'Y':
            fcal = c13_rule_winper.cal(result_t,result_s)
            c13_rule_winper.fwp(fcal)
            break 








# print(f'컴{com_choi} : 휴{hu_choi}로 결과는 {re}의 승리입니다.')




# wi = [] 
# wis = []
# wiper = (len(wis)/len(wi))*100
# print(f'승률 {wiper}%')







# while True:
#     if qwe % 3 == 0:
#         a = input('계속 할거야? y/n').upper
#         if a == 'N':
#             return False
#         elif a == 'Y':
#             continue
#         else:
#             print('y or n')





