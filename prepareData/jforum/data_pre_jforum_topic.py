import time
import random

import pymysql

conn = pymysql.connect(
    host='localhost',
    user='root',
    passwd='123456',
    db='jforum',
    port=3306,
    charset='utf8')
cur = conn.cursor()
i=3
while i <=20:
    userId=6+random.randint(0,3)
    forumId=random.randint(3,5)
    topicId=i
    postId=i
    createDate=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    print(createDate)
    print(userId)
    print(forumId)
    #sql1='insert into jforum_topics VALUES ("'+str(topicId)+'","'+str(forumId)+'","jmeter测试",' \
    #    '"'+str(userId)+'","'+str(createDate)+'",1,0,0,0,0,"'+str(i)+'","'+str(i)+'",0,0);'
    #print(sql1)str
    sql2='''insert into jforum_topics VALUES ({},{},"LOVELY RAN {topId}",{uid},"{cdate}",1,0,0,0,0,{},{},0,0)'''.format(topicId, forumId, topicId, topicId, topId=topicId, uid=userId, cdate = createDate)
    #关键字参数必须跟随在位置参数后面
    sql3='''insert into jforum_posts VALUES ({},{},{},{},"{cdate}","127.0.0.1",1,0,1,1,null,0,1,0,0)'''.format(postId,topicId,forumId,userId,cdate= createDate)
    sql4='insert into jforum_posts_text VALUES ({},"[b]hello ranran[/b]","jmeter")'.format(postId)
    cur.execute(sql2)
    conn.commit()
    cur.execute(sql3)
    conn.commit()
    cur.execute(sql4)
    conn.commit()
    print('数字' + str(i))
    i = i + 1
print("已经插入完成")
cur.close()
conn.close()
