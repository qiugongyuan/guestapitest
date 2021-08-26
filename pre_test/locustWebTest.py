from locust import TaskSet, task, HttpUser


# web性能测试

class UserBehavior(TaskSet):
    def on_start(self):
        self.login()

    def login(self):
        self.client.post("index", {"username": "admin", "password": "admin123456"})

    @task(2)
    def event_manage(self):
        self.client.get("event_manage")

    @task(2)
    def guest_manage(self):
        self.client.get("guest_manage")

    @task(1)
    def search_phone(self):
        self.client.get("search_phone", params={"phone": '15330235994'})


class WebSiteUser(HttpUser):
    tasks = [UserBehavior]
    min_wait = 3000
    max_wait = 6000
