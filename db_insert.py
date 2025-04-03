import pymysql
import csv

def insert_to_db(csv_file_path):
    # 데이터베이스 연결
    conn = pymysql.connect(host='127.0.0.1', user='root', password='', 
                           db='samsung', charset='utf8')
    try:
        with conn.cursor() as curs:
            # CSV 파일 열기
            with open(csv_file_path, 'r', encoding='utf-8') as f:
                csvReader = csv.reader(f)

                # DB col : Date, Open, High, Low, Close, Adj Close, Volume
                # 기본적으로 CSV에 헤더가 없다고 가정
                for row in csvReader:
                    if len(row) != 7:  # 데이터 길이가 7이 아닐 경우 건너뛰기
                        print("Invalid row:", row)
                        continue
                    
                    # 데이터 변수 할당
                    Date, Open, High, Low, Close, AdjClose, Volume = row
                    
                    # SQL 쿼리 실행
                    sql = """
                    INSERT INTO samsung.testDB (Date, Open, High, Low, Close, AdjClose, Volume) 
                    VALUES (%s, %s, %s, %s, %s, %s, %s)
                    """
                    curs.execute(sql, (Date, Open, High, Low, Close, AdjClose, Volume))
                    print('Insert completed for date:', Date)
                
                # 모든 변경 사항 커밋
                conn.commit()
    except Exception as e:
        print("An error occurred:", e)
    finally:
        # 데이터베이스 연결 종료
        conn.close()