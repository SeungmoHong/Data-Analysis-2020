import json
import pymysql

with open('mysql.json', 'r') as file:
    config_str = file.read()
config = json.loads(config_str)

conn = pymysql.connect(
    host = config['host'],
    user = config['user'],
    password = config['password'],
    database = config['database']
)
# 1번문제
sqlEagles = '''
CREATE TABLE IF NOT EXISTS Eagles (back_no INT NOT NULL, name varchar(10) , position TEXT, PRIMARY KEY(back_no));
'''
sqlPicher_stats ='''
CREATE TABLE IF NOT EXISTS Pitcher_stats (back_no INT NOT NULL, ERA INT, IP TEXT, SO INT)
'''
sqlInsertPlayer = '''
insert into Eagles(back_no, name, position) values(54,'서균', '투수'),(5,'윤대경','투수'),(62,'강재민','투수'),(37,'김진영','투수'),(48,'장웅정','투수'),(67,'송윤준','투수'),(53,'김민우', '투수')
'''
sqlInsertStats = '''
insert into Pitcher_stats(back_no, ERA, IP, SO) values(54, 0.00, '7 1/3', 1),(5, 1.59, '51', 42), (62, 2.57, '49', 57),(37, 2.57, '54', 56), (48, 3.52, '7 2/3', 5), (67, 4.30, '23', 16),(53, 4.34, '132 2/3', 124)
'''
cur = conn.cursor()
cur.execute(sqlEagles)
conn.commit()
cur.execute(sqlPicher_stats)
conn.commit()
cur.execute(sqlInsertPlayer)
conn.commit()
cur.execute(sqlInsertStats)
conn.commit()

#2번문제
sqlBoyGroup = '''
CREATE TABLE IF NOT EXISTS Boy_Group (id integer primary key auto_increment, group_name varchar(10) ,구성원 TEXT, 데뷔일자 DATE,소속사 TEXT)
'''

sqlSong='''
CREATE TABLE IF NOT EXISTS Song (song_id integer primary key auto_increment, song_name TEXT ,group_id TEXT, 발표날짜 DATE,작곡가 TEXT, 도입부가사 TEXT)
'''

sqlInsertBoyGroup = '''
insert into Boy_Group(group_name, 구성원, 데뷔일자, 소속사) values('EXO', '7', '2012-04-08','SM엔터테인먼트'),('BTS', '7', '2013-06-13', '빅히트 엔터테인먼트'),('빅뱅','4','2006-08-19','YG 엔터테인먼트'),('Highlight','4','2017-03-20','어라운드어스 엔터테인먼트'),('B1A4','3','2011-04-14','WM엔터테인먼트' )
'''

sqlInsertSong = '''
insert into Song(song_name, group_id, 발표날짜, 작곡가, 도입부가사) values('첫 눈', 'EXO', '2013-12-09', 'KENZIE, 김정배', '첫눈 오는 이런 오후에 너에게 전화를 걸 수만 있다면'),('Love Shot','EXO', '2018-12-13', 'Mike Woods, Kevin White', '차갑도록 서롤 겨눈 채 날이 선 듯 그 목소리엔'),('Dynamite', 'BTS', '2020-08-24', 'David Stewart, Jessica Agombar', 'Cos ah ah I’m in the stars tonight'),('작은 것들을 위한 시', 'BTS', '2019-04-12', 'Halsey, RM', '모든 게 궁금해 How’s your day Oh tell me'),('하루하루', '빅뱅', '2008-08-08', 'G-DRAGON, Daishi Dance', '떠나가 Ye the finally I reallize That I`m nu`ttin without you'),('거짓말', '빅뱅', '2007-08-16', '용감한 형제, G-DRAGON', 'ye love is pain to all my brokenhearted people'),('얼굴 찌푸리지 말아요', 'Highlight', '2017-03-20', 'Good Life', '오늘따라 유난히 웃지 않는 네가 왠지 슬퍼 보여'),('사랑했나봐', 'Highlight', '2018-11-20', 'Good Life', '그리운 하늘에 떠오른 그대가 맘을 들춰내고 또 날 춥게 해'),('잘자요 굿나잇', 'B1A4', '2012-05-24', '진영', '그래요 오늘은 먼저 자요 그대 잠들면 나도 잘게요'), ('이게 무슨 일이야','B1A4', '2013-05-06', '진영', 'every day yeah yeah yeah yeah every day yeah yeah yeah yeah')
'''

cur = conn.cursor()
cur.execute(sqlBoyGroup)
conn.commit()
cur.execute(sqlSong)
conn.commit()
cur.execute(sqlInsertBoyGroup)
conn.commit()
cur.execute(sqlInsertSong)
conn.commit()

# 3번문제

sqlUsers = '''
CREATE TABLE IF NOT EXISTS Users (사용자 text ,비밀번호 text);
'''
sqlInsertUser = '''
insert into Users(사용자,비밀번호) values('admin', 1234), ('user', 1234)
'''

cur.execute(sqlUsers)
conn.commit()
cur.execute(sqlInsertUser)
conn.commit()



cur.close()
conn.close()