import time
import random

import pymysql

conn = pymysql.connect(
    host='127.0.0.1',
    user='root',
    passwd='1234',
    db='jforum',
    port=3306,
    charset='utf8')
cur = conn.cursor()
i=106
while i <= 107:
    userId=6+random.randint(0,3)
    forumId=random.randint(1,4)
    topicId=i
    postId=i
    createDate=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    print(createDate)
    print(userId)
    print(forumId)
    #sql1='insert into jforum_topics VALUES ("'+str(topicId)+'","'+str(forumId)+'","jmeter测试",' \
    #    '"'+str(userId)+'","'+str(createDate)+'",1,0,0,0,0,"'+str(i)+'","'+str(i)+'",0,0);'
    #print(sql1)
    sql2='''insert into jforum_topics VALUES ({},{},"jmeter",{uid}, "{cdate}",1,0,0,0,0,{},{},0,0)'''.format(topicId, forumId, topicId, topicId, uid=userId, cdate = createDate)
    #关键字参数必须跟随在位置参数后面
    cur.execute(sql2)
    conn.commit()
    print('数字' + str(i))
    i=i+1

print("已经插入完成")
cur.close()
conn.close()
