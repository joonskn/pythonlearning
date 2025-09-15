# 사용자 입력 처리 함수 제작
# get_data
# parameter 
    # start     : 시작값
    # end       : 종료값
    # input_str : 가이드 문구
# 사용자 입력은 input() 
# return 정수로 변환 된 입력값



# 랜덤정수 선택 컴퓨터값
import random as rd
import game_utils as gu

start, end = 1,1000
computer = rd.randint(start,end)

count = 0
game_his = []
while True:
    count += 1
    human = gu.get_num(start,end)
    # 승자선택 로직
    if gu.check_winner(human,computer,game_his,count):
        break


        