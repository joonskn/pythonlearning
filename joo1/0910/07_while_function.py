import time

def display_second(count):
    count = count + 1
    print(f'{count}초')
    time.sleep(1) 
    return count

def is_User_countinue(count):
    if count % 5 == 0:
        user_input = input('To be continue(Y/y)').upper()
        if not user_input == 'Y':
            return False
    return True


is_continue = True
count = 0
while is_continue:
    count = display_second(count) # 1초 간격 출력
    is_continue = is_User_countinue(count) #5초 단위로 진행여부



# count가 함수 내부에 정의되어 있지 않음
# 함수 내에서 cout 정의하면 안됨 : 게속 초기화 함
# 로직 상 외부에서 카운트 가져와야 함
# 함수 종료 후 외부에 리턴 필요
# is컨티뉴는 받을거임