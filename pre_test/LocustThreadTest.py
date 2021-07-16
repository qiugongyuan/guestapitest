import requests
import threading
from time import time

base_url="http://127.0.0.1:8000"

#签到线程
def sign_thread(start_user,end_user):
    for i in range(start_user,end_user):
        phone=18511852789+i
        datas={'id':1,'phone':phone}
        r=requests.post(base_url+'/api/user_sign/',data=datas)
        result=r.json()
        try:
            assert result['message']=="sign success"
        except AssertionError as e:
            print("phone:"+str(phone)+",user sign fail!")
#设置用户分组
lists={1:5,5:10}

#创造线程组
threads=[]
#创建线程
for start_user,end_user in lists.items():
    t=threading.Thread(target=sign_thread,args=(start_user,end_user))
    threads.append(t)

if __name__=='__main__':
    start_time=time()

    #启动线程
    for i in range(len(lists)):
        threads[i].start()
    for i in range(len(lists)):
        threads[i].join()
    #结束时间
    end_time=time()
    print("start time:"+str(start_time))
    print("end time:"+str(end_time))
    print("run time:"+str(end_time-start_time))