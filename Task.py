from tabulate import tabulate

class Task:
    def __init__(self):
        self.task = []

    def __str__(self):
        return f"task: {self.task}"
    
    @property
    def task(self):
        return self._task
    
    @task.setter
    def task(self, task):
        self._task = task

    def view(self, style="pretty"):
        headers = [ "No", "Task", "Status" ]
        print(tabulate(self.task, headers=headers, showindex="always", tablefmt=style))
    
    def remove(self):
        ...
    #☐ 🗹
    def add(self, task, status="☐"):
        self.task.append([task, status])

    
