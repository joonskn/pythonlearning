# pip install pymysql mysql을 접속 할 수 있는 라이브러리
# pip install dotenv  env 쓸수 있는 라이브러리
import pymysql
from dotenv import load_dotenv   #env 로드
import os  #os 해야 환경변수를 세팅해주는거

# .env 로드
load_dotenv()

# 1. DB를 연결
conn = pymysql.connect(
    host= os.getenv('DB_HOST'),
    user= os.getenv('DB_USER'),
    passwd= os.getenv('DB_PASSWORD'),
    database= os.getenv('DB_NAME')
)
print('접속 성공')
conn.close() # 접속 해제

# 2. 각 테이블 별 CRUD
    # C -> insert
    # R -> select
    # U -> update
    # D -> delete
# 3. 액션 = 메소드
    # 회원가입
    # 상품 정보 출력
    # 상품 구입
    # 상품 정보 입력
    # 대쉬보드 : 고객별 상품별 구매 회수, 평균 구매액
# 4. 기능구현과 테스트가 끝나면 streamlit으로 ui구성
    # 템플릿 화면 보고 유사한 형태로 구현