# 사용자 입력 처리 함수 제작
# get_data
# parameter 
    # start     : 시작값
    # end       : 종료값
    # input_str : 가이드 문구
# 사용자 입력은 input() 
# return 정수로 변환 된 입력값

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
        

print(get_num(1,10,))





# 변수에 기본값이 없어려 오류가 났었다
# 작업의 우선순위를 잘 생각해보자(오류나면 여튼 오류나서 반복한거지 무슨 오류인지 중요하지 않다)
# 리턴값 받아야하고, 리턴 받으면 함수가 끝나니 break가 필요 없다
# 과도하게 요구하지 말자
# 요소를 바꿔 줄 떄 작성법 제대로 확인