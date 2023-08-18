from tabulate import tabulate

class Task:
    def __init__(self):
        self.task = []
        self.count = len(self.task)

    def __str__(self):
        return f"task: {self.task}"
    
    @property
    def task(self):
        return self._task
    
    @task.setter
    def task(self, task):
        self._task = task

    def view(self, style="grid"):
        headers = [ "No", "Task", "Status" ]
        print(tabulate(self.task, headers=headers, tablefmt=style, showindex=range(1, self.count + 1)))
    
    def remove_by_index(self, index):
        del self.task[index]

    def remove_by_name(self, name):
        for i in range(len(self.task)):
            if name in self.task[i]:
                del self.task[i]

    #☐ 🗹
    def add(self, task, status="Pending"):
        self.task.append([task, status])

    @property
    def count(self):
        self._count = len(self.task)
        return self._count
    
    @count.setter
    def count(self, count):
        self._count = count
        