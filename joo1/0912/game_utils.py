def get_num(st=1,end=100,input_str='정수입력: '):
    while True:
        try:
            h_num = int(input(f'{input_str}({st}~{end}): '))
            if not st <= h_num <= end:
                raise ValueError(f'{st}~{end}범위 초과')
        except Exception as e :
            print(f'오류 : {e}')     
        else:
            return h_num
        

def check_winner(human, computer, game_his, count):
# 게임
    if human > computer:
        print('휴먼이 크다')
        game_his.append( (human,'크다') )
    elif human < computer:
        print('휴먼이 작다')
        game_his.append( (human,'작다') )
    else:
        print(f'정답이다. {count}회')
        for guess_value, state in game_his:
            print(f'{guess_value} - {state}')
        return True
    if count > 10:
        print('어이쿠')
        return True
    return False