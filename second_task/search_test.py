import time

from locust import HttpUser, task, between


class User(HttpUser):
    wait_time = between(1, 5)

    @task
    def mainPage(self):
        self.client.get("/")
        self.client.get("https://www.n11.com/")

    @task(2)
    def search(self):
        for item_id in range(10):
            self.client.get(f"/arama?q=phone{item_id}")
            time.sleep(1)
