import pandas as pd
from sqlalchemy import create_engine

def insert_to_db(csv_file_path):
    # SQLAlchemy를 사용하여 데이터베이스 엔진 생성
    engine = create_engine('mysql+pymysql://root:@127.0.0.1/samsung', encoding='utf-8')

    # CSV 파일을 Pandas DataFrame으로 읽기
    try:
        df = pd.read_csv(csv_file_path, header=None)  # 헤더가 없는 경우 header=None
        df.columns = ['Date', 'Open', 'High', 'Low', 'Close', 'AdjClose', 'Volume']  # 컬럼명 지정

        # 데이터베이스에 DataFrame 삽입
        df.to_sql('testDB', con=engine, if_exists='append', index=False)
        print('Data inserted successfully.')
        
    except Exception as e:
        print("An error occurred:", e)

if __name__ == '__main__':
    csv_file = 'path/to/your/csvfile.csv'  # 실제 CSV 파일 경로로 업데이트
    insert_to_db(csv_file)