import os,sqlite3
db_file=os.path.join(os.path.dirname(__file__),'test.db')
if os.path.isfile(db_file):
    os.remove(db_file)

conn=sqlite3.connect(db_file)
cursor=conn.cursor()
cursor.execute('create table user(id varchar(20) primary key, name varchar(20),score int)')
cursor.execute(r"insert into user values ('A-001','Adam',95)")
cursor.execute(r"insert into user values ('A-002','Bart',62)")
cursor.execute(r"insert into user values ('A-003','Lisa',78)")
cursor.close()
conn.commit()
conn.close()

def get_score_in(low,high):
    try:
        conn=sqlite3.connect(db_file)
        cursor=conn.cursor()
        sql='select u.name from user u where u.score>=? and u.score<=? order by u.score'
        cursor.execute(sql,(low,high))
        values=cursor.fetchall()
        return list(map(lambda x: x[0],values))
    except BaseException as e:
        print(e)
    finally:
        cursor.close()
        conn.commit()
        conn.close()

print(get_score_in(80,95))
print(get_score_in(60,80))
print(get_score_in(60,100))
assert get_score_in(80,95)==['Adam']
assert get_score_in(60,80)==['Bart','Lisa']
assert get_score_in(60,100)==['Bart','Lisa','Adam']
print('Pass')
