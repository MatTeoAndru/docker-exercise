from locust import HttpUser, TaskSet, task, between

class MyUser(TaskSet):
    @task
    def cpu_task(self):
        self.client.get("/cpu_5")  # Adjust the seconds as needed

    @task
    def ram_task(self):
        self.client.get("/ram_1_5")  # Adjust the GB and seconds as needed

class MyLocust(HttpUser):  # Update 'Locust' to 'HttpUser'
    tasks = [MyUser]
    wait_time = between(1, 3)  # Adjust the wait time between tasks
