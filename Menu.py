import time
from tabulate import tabulate

class Menu:
    def __init__(self, name) -> None:
        self.name = name

    def __str__(self) -> str:
        return self.name

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        self._name = name
  
main_menu = Menu("Main Menu")
add_menu = Menu("Add Tasks")
view_menu = Menu("View Tasks")
remove_menu = Menu("Remove Tasks")
mark_menu = Menu("Mark Tasks")
eixt_menu = Menu("Exit")
current_menu = main_menu
available_menues = []
menues = [main_menu, add_menu, view_menu, remove_menu, mark_menu, eixt_menu]

def select_menu():
    global current_menu
    menu = input("Select: ")
    try:
        menu = int(menu)
        if 0 <= menu < len(available_menues):
            current_menu = available_menues[int(menu)]
        else:
            raise Exception
    except Exception:
        print('\033[31m Invalid Input\033[0m')
        time.sleep(1)
           
def open_current_menu():          
    print(current_menu)

def navi_menu():
    global available_menues
    index = 0
    available_menues = []
    nav_menu = ""
    for i in range(len(menues)):
        if menues[i] is current_menu:
            continue
        nav_menu += (f"[{index}-{menues[i].name}] ")
        available_menues.append(menues[i])
        index += 1   
    print(tabulate(([nav_menu],)))

def show():
    open_current_menu()
    navi_menu()
    select_menu()