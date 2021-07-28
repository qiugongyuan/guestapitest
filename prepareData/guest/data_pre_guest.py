import time

import pymysql
conn =pymysql.connect(
    host='127.0.0.1',
    user='root',
    passwd='1234',
    db='guest_test',
    port=3306,
    charset='utf8')
cur =conn.cursor()
count = 0
now_time=time.time()
while count < 10:
    count += 1
    str_count=str(count)
    realname="kara"+str_count
    phone=18511852789+count
    email='kara'+str_count+"@mail.com"
    #now_time='2021-09-08 12:00:00' 赋予一个死的定义的时间
    dt_time=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())#获取当前动态时间
    sql = 'INSERT INTO sign_guest_new ( `realname`, `phone`, `email`, `sign`, `event_id`,`create_time`) VALUES (" '+realname+'" , '+str(phone)+', "'+email+'",0,1," '+dt_time+'");'
    cur.execute(sql)
    conn.commit()
    print('数字'+str(count))
print("已经插入完成")
cur.close()
conn.close()