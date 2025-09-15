# 가위 바위 보 게임  (컴퓨터 VS 휴먼)
# 가위 : 1 바위 : 2 보 : 3
# 규칙 : 컴퓨터가 임의로 숫자를 선택   : Random
# 인간이 숫자를 입력                  : input
# 승패를 기록                         
# 3번마다 계속할 지 물어본다         : for

import c14_games

for i in range(1,101):
    com_choice = c14_games.get_com_num()
    human_choice = c14_games.get_hu_num()
    c14_games.check_winner(com_choice,human_choice)
    if i % 3 == 0:
        is_continue = input('계속 할꺼야?:(Y/y)').upper()
        if not is_continue == 'Y':
            break
