from tabulate import tabulate

class Task:
    def __init__(self):
        self.tasks = []
        self.count = len(self.tasks)

    def __str__(self):
        return f"task: {self.tasks}"
    
    @property
    def tasks(self):
        return self._task
    
    @tasks.setter
    def tasks(self, task):
        self._task = task

    def view(self, style="grid"):
        headers = [ "No", "Task", "Status" ]
        print(tabulate(self.tasks, headers=headers, tablefmt=style, showindex=range(1, self.count + 1)))
    
    def mark_by_index(self, index):
        if self.tasks[index][1] is "\033[33m Pending \033[0m":
            self.tasks[index][1] = "\033[32m Complete \033[0m"
        else:
            self.tasks[index][1] = "\033[33m Pending \033[0m"

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

    #☐ 🗹
    def add(self, task, status="\033[33m Pending \033[0m"):
        self.tasks.append([task, status])

    @property
    def count(self):
        self._count = len(self.tasks)
        return self._count
    
    @count.setter
    def count(self, count):
        self._count = count
        