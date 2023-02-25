
import pymysql


#host = db 서버 주소
#user = db 로그인 아이디
#password = db 로그인 아이디에 해당하는 비밀번호
#db = 데이터 베이스 이름
#connect - 데이터 베이스 연결 ( 해당 정보를 con 이라는 변수에 저장 )
con = pymysql.connect(host='127.0.0.1', user='root', password='1234', db='python', charset='utf8')

# 명령을 입력할 수 있는 cursor 를 가져와서 cur 이라는 변수에 저장.
cur = con.cursor()

# database 서버 - database 들을 관리.
# database - table 들을 관리.
# table - column 들을 관리.
# column - 변수와 동일한 개념.

# 문자열 - ''
# 테이블, 컬럼이름 - ``

# table 생성 쿼리문
# create table `테이블이름` (컬럼 정보)
#   - 컬럼 정보 : `컬럼이름` 타입 (not null) (default 'value')

# cur.execute("create table if not exists `test` (`num` int, `name` text)")
#
# li = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
#
# for index, text in enumerate(li):
#     cur.execute(f"insert into `test` (`num`,`name`) values({index +1}, '{text}')")
#
# con.commit()


#select `컬럼명` from `테이블명`
#   - where `컬럼명`=값 (해당 컬럼의 값이 우측의 값과 같은 컬럼만 선택)
cur.execute("select * from `test`")

#해당 커서는 결과값의 위치에 있게됨.
#fetchall() 모든 결과를 반환 -> tuple
#fetchmany(10) 10개만 반환  -> tuple
#fetchone() 1개만 반환      -> tuple

# # delete from `테이블명` where ~~
# cur.execute("delete from `test` where `num` = 5")
# con.commit()

rows = cur.fetchall()

# #update `테이블명` set `컬럼명`=값 where ~~
# cur.execute("update `test` set `name` = 'abcd' where `num` = 1")
# con.commit()



print(rows)
