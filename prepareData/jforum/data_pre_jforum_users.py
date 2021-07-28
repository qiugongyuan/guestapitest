import time

import pymysql

conn = pymysql.connect(
    host='127.0.0.1',
    user='root',
    passwd='1234',
    db='jforum',
    port=3306,
    charset='utf8')
cur = conn.cursor()
count = 5

while count <= 8:
    count += 1
    str_count = str(count)
    username = "test" + str_count
    useremail = 'test' + str_count + "@mail.com"
    sql1 = 'insert into jforum_users (`user_id`,`user_active`,`username`,`user_password`,`user_session_time`,`user_session_page`,`user_lastvisit`,`user_regdate`,`user_level`,' \
           '`user_posts`,`user_timezone`,`user_style`,`user_lang`,`user_dateformat`,`user_new_privmsg`,`user_unread_privmsg`,' \
           '`user_last_privmsg`,`user_emailtime`,`user_viewemail`,`user_attachsig`,`user_allowhtml`,`user_allowbbcode`,`user_allowsmilies`,' \
           '`user_allowavatar`,`user_allow_pm`,`user_allow_viewonline`,`user_notify`,`user_notify_always`,`user_notify_text`,`user_notify_pm`,' \
           '`user_popup_pm`,`rank_id`,`user_avatar`,`user_avatar_type`,`user_email`,`user_icq`,`user_website`,`user_from`,`user_sig`,' \
           '`user_sig_bbcode_uid`,`user_aim`,`user_yim`,`user_msnm`,`user_occ`,`user_interests`,`user_biography`,`user_actkey`,' \
           '`gender`,`themes_id`,`deleted`,`user_viewonline`,`security_hash`,`user_karma`,`user_authhash`)' \
           'VALUES ( "' + str_count + '", 1, "' + username + '", "81dc9bdb52d04dc20036dbd8313ed055", 0,0, NULL,"2021-07-19+12:00:00", NULL, 0,"",NULL,"","%d/%M/%Y %H:%i", 0,0, NULL, NULL,0,1,0,1,1,1,1,1,1,0,0,1,1,0,NULL,' \
                                                             '0, " ' + useremail + '", NULL, NULL,NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL,NULL, NULL, NULL, NULL, NULL,1, NULL, NULL,NULL);'
    cur.execute(sql1)
    conn.commit()
    sql2 = 'insert into jforum_user_groups(group_id,user_id) VALUES(3,"' + str_count + '")'
    cur.execute(sql2)
    conn.commit()
    print('数字' + str(count))
print("已经插入完成")
cur.close()
conn.close()
