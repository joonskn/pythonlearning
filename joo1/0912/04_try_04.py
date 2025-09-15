# raise 예외 발생
try:
    print('정상코드')
    print('예외 발생')
    raise "이런"
    # raise ValueError('테스트')
except Exception as e:
    print(f'에러 : {e}, {e.__class__.__name__}')


# 주로 쓰는건 벨류, NotImplementedError
