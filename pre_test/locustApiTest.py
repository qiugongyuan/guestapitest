from locust import HttpUser,TaskSet,task
from random import randint
class UserBehavior(TaskSet):
    @task
    def uer_sign(self):
        number=randint(1,10)
        phone=18511852789+number
        str_phone=str(phone)
        self.client.post("api/user_sign/",data={"id":1,"phone":str_phone})

class WebSiteUer(HttpUser):
    tasks = [UserBehavior]
    min_wait = 0
    max_wait = 0