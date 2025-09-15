import random

def com_num():
    return random.randint(1,3)

def hu_num():
    return int(input('1, 2, 3! : '))

def gbv(com_choi,hu_choi):
    if com_choi - hu_choi == 0:
        print('비겼다')
    elif com_choi - hu_choi == -1 or com_choi - hu_choi == 2:
        print('휴승')
    elif com_choi - hu_choi == 1 or com_choi - hu_choi == -2:
        print('컴승')