import os, json, Database
from tabulate import tabulate

class Todo_List:
    def __init__(self):
        Database.connect("TODO")
        self.check_data()
        self.get_name()
        self.task_count = len(self.tasks)
        

    def __str__(self):
        return f"task: {self.tasks}"
    
    @property
    def tasks(self):
        return self._task
    
    @tasks.setter
    def tasks(self, task):
        self._task = task

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        self._name = name

    def get_name(self):
        while not self.name:
            self.name = input("Name your list: ") 

    def load_data(self, file_name):
        with open(file_name, "r") as f:    
            content = f.read()
            if content:
                data = json.loads(content)
                self.name = next(iter(data.keys()))
                self.tasks = data[self.name]
            
    def check_data(self):
        file_name = "Data.json"
        if os.path.exists(file_name):
            self.load_data(file_name)
        else:
            self.name = ""
            self.tasks = []
 
    def save_data(self):
        file_name = f"Data.json"
        with open(file_name, "w") as f:
            json.dump({self.name: self.tasks}, f)

    def delete_file(self):
        file_name = f"{self.name}_Data"
        if os.path.exists(file_name):
            os.remove(file_name)

    def view(self, style="grid"):
        headers = [ "No", "Task", "Status" ]
        print(tabulate(self.tasks, headers=headers, tablefmt=style, showindex=range(1, self.task_count + 1)))
    
    def mark_by_index(self, index):
        pending = "\033[33m Pending \033[0m"
        complete = "\033[32m Complete \033[0m"
        if self.tasks[index][1] == pending:
            self.tasks[index][1] = complete
        else:
            self.tasks[index][1] = pending

    def mark_by_name(self, name):
        print("to be implemented")

    def remove_by_index(self, index):
        del self.tasks[index]

    def remove_by_name(self, name):
        for i in range(len(self.tasks)):
            if name in self.tasks[i]:
                del self.tasks[i]
                return True
        return False

    def add(self, task, status="\033[33m Pending \033[0m"):
        self.tasks.append([task, status])

    @property
    def task_count(self):
        self._count = len(self.tasks)
        return self._count
    
    @task_count.setter
    def task_count(self, count):
        self._count = count
        