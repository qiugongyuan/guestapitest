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
while i <=50:
    userId=6+random.randint(0,3)
    forumId=random.randint(3,5)
    topicId=i
    postId=i
    createDate=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    print(createDate)
    print(userId)
    print(forumId)
    sql1='''insert into jforum_topics VALUES ({},{},"LOVELY RAN {topID}",{uid},"{cdate}",1,0,0,0,0,{},{},0,0)'''.format(topicId, forumId, topicId, topicId+2, topID=topicId,uid=userId, cdate = createDate)
    #关键字参数必须跟随在位置参数后面
    #????这个LOVELY RAN怎样拼接成可变的字符串????
    sql2='''insert into jforum_posts VALUES ({},{},{},{},"{cdate}","127.0.0.1",1,0,1,1,null,0,1,0,0)'''.format(postId,topicId,forumId,userId,cdate= createDate)
    sql3='insert into jforum_posts VALUES({},{},{},{},"{cdate}","127.0.0.1",1,0,1,1,null,0,1,0,0)'.format(i+1,topicId,forumId,userId,cdate=createDate)
    sql4='insert into jforum_posts VALUES({},{},{},{},"{cdate}","127.0.0.1",1,0,1,1,null,0,1,0,0)'.format(i+2,topicId,forumId,userId,cdate=createDate)
    sql5='insert into jforum_posts_text VALUES ({},"[b]hello ranran {postD}[/b]","jmeter")'.format(postId,postD=postId)
    sql6='insert into jforum_posts_text VALUES ({},"[b]ranran love car reply {topID}[/b]","jmeter")'.format(postId+1,topID=topicId+1)
    sql7='insert into jforum_posts_text VALUES ({},"[b]ranran love car reply {topID}[/b]","jmeter")'.format(postId+2,topID=topicId+2)
    cur.execute(sql1)
    conn.commit()
    cur.execute(sql2)
    conn.commit()
    cur.execute(sql3)
    conn.commit()
    cur.execute(sql4)
    conn.commit()
    cur.execute(sql5)
    conn.commit()
    cur.execute(sql6)
    conn.commit()
    cur.execute(sql7)
    conn.commit()
    print('数字' + str(i))
    i = i + 3
print("已经插入完成")
cur.close()
conn.close()
