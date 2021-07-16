from locust import HttpLocust, TaskSet, task, HttpUser


# 定义用户行为
class UeserBehavior(TaskSet):
    # userBehavior类继承TeskSet类，用于描述用户行为

    @task
    # @task指定一个定义的用户行为类
    def baidu_page(self):
        self.client.get("/")
    # baidu_page()方法表示一个用户行为，访问百度首页。使用@task装饰该方法为一个事务。client.get（）用于指定请求的路径“/”。
    # 因为是百度首页，所以指定为根路径


class WebSiteUser(HttpUser):
    tasks = [UeserBehavior]
    min_wait = 3000  # 执行事务之间用户等待时间的下界，单位ms
    max_wait = 6000  # 执行事务之间用户等待时间的上界，单位ms
