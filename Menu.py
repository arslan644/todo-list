class Menu:
    menues = {0: "Main Menu", 1: "Add Task", 2: "View Tasks", 3: "Remove Task"}
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        self._name = name