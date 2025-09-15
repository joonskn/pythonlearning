# while 무한 반복
# whil 조건 :

import time

count = 0
is_continue = True
while is_continue:
    count += 1
    print(f'{count}초')
    time.sleep(0) # sleep()  숫자만큼 지연(초) 한다
    
    # 5초 단위로 사용자한테 계속 할건지 물여본다 "To be continue(y/n)"
    if count % 5 == 0:
        user_input = input('To be continue(Y/y)').upper()
        if not user_input == 'Y':
            is_continue = False