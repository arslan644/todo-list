import sys, os, time
from Task import Task
from tabulate import tabulate

menues = {1: "Add Task", 2: "View Tasks", 3: "Remove Task", 4: "Mark Task", 5: "Exit"}
available_menu = []
current_menu = 1
task = Task()
input_taken = False
styles = [
        "plain",
        "simple",
        "github",
        "grid",
        "simple_grid",
        "rounded_grid",
        "heavy_grid",
        "mixed_grid",
        "double_grid",
        "fancy_grid",
        "outline",
        "simple_outline",
        "rounded_outline",
        "heavy_outline",
        "mixed_outline",
        "double_outline",
        "fancy_outline",
        "pipe",
        "orgtbl",
        "asciidoc",
        "jira",
        "presto",
        "pretty",
        "psql",
        "rst",
        "mediawiki",
        "moinmoin",
        "youtrack",
        "html",
        "unsafehtml",
        "latex",
        "latex_raw",
        "latex_booktabs",
        "latex_longtable",
        "textile",
        "tsv"
        ]

def main():
    show_menu()

def testing():
    print("checking")

def select_menu():
    global current_menu
    menu = input("Select: ")
    if not menu.isdigit() or int(menu) not in available_menu:
        print('\033[31m Invalid Input\033[0m')
        time.sleep(1)
        show_menu()
    else:
        current_menu = int(menu)
        show_menu()
    
def app_title():
    print(tabulate((["|     ToDo List      |"],)))

def view_tasks(style_no=22):
    if task.count <= 0:
        print(tabulate((['\033[47m \033[30m No Tasks \033[0m' ],), tablefmt="mixed_outline"))
    else:
        if len(sys.argv) > 1:
            task.view(sys.argv[1])
        else:
            index = bound_in_range(style_no)
            task.view(style=styles[index])
        
def bound_in_range(number):
    lower_bound = 0
    upper_bound = len(styles) - 1
    return max(min(number, upper_bound), lower_bound)

def show_menu():
    global current_menu
    clear_screen()
    app_title()
    open_current_menu()
    navi_menu(current_menu)
    select_menu()

def add_task():
    global current_menu
    print("(Note: Press 'ctr + c' to save)")
    print("Add Task:")
    print_previous_tasks()
    exit = False
    while not exit:
        try:
            verify_input(input(f"{task.count + 1}: "))
            
        except KeyboardInterrupt:
            current_menu = 2
            exit = True

def verify_input(new_task):
    if not new_task.strip():
        print('\033[31m can\'t add empty task \033[0m')
        time.sleep(1)
        show_menu()
    elif  already_in_list(new_task.strip()):
        print('\033[31m task already exist \033[0m')
        time.sleep(1)
        show_menu()
    task.add(new_task.strip())

def already_in_list(new_task):
    if task.count <= 0:
        return False
    
    for i in range(task.count):
        if new_task in task.tasks[i]:
            return True

def print_previous_tasks():
    if task.count > 0:
        for i in range(task.count):
            print(f"{i + 1}: {task.tasks[i][0]}")

def open_current_menu():         
    global current_menu           
    match current_menu:
        case 1:
            add_task()
            show_menu()
        case 2:
            view_tasks()
        case 3:
            remove_task()
        case 4:
            mark_task()
        case 5:
            exit_progarm()
        case _:
            show_menu()

def mark_task():
    global current_menu, input_taken
    if not input_taken:
        print(" Mark Task ")
        view_tasks()
        print("(Note: Press 'ctr + c' to go back)")
    try: 
        text = input("Select Task: ")
        input_taken = True
        if text.isdigit():
            mark_by_index(text)
        else:
            mark_by_name(text)
        input_taken = False
        show_menu()
    except KeyboardInterrupt:
        current_menu = 2
        show_menu()

def mark_by_name(text):
    task.mark_by_name(text)

def mark_by_index(text):
    index = int(text)
    count = task.count
    if 0 < index <= count:
        task.mark_by_index(index-1)
    else:
        print('\033[31m Selected Index is not in task list \033[0m')
        mark_task()

def exit_progarm():
    global current_menu
    print("Are you Sure?")
    print(tabulate((["1-Yes", " 0-No"],), tablefmt="mixed_outline"))
    user_input = ""
    while user_input not in ["1", "0"]:
        user_input = input()
        if user_input is "1":
            clear_screen()
            sys.exit()
        elif user_input is "0":
            current_menu = 2
            show_menu()
        else:
            print('\033[31m Invalid Selection \033[0m')

def remove_task():
    global current_menu, input_taken
    if not input_taken:
        print(" Remove Task ")
        view_tasks()
        print("(Note: Press 'ctr + c' to go back)")
    try: 
        if task.count is 0:
            raise KeyboardInterrupt
        text = input("Select Task: ")
        input_taken = True
        if text.isdigit():
            remove_by_index(text)
        else:
            remove_by_name(text)
        input_taken = False
        show_menu()
    except KeyboardInterrupt:
        current_menu = 2
        show_menu()



def remove_by_name(text):
    global input_taken
    if not task.remove_by_name(text):
        print('\033[31m Task name is not in task list \033[0m')
        time.sleep(1)
        input_taken = False
        show_menu()

def remove_by_index(text):
    global input_taken
    index = int(text)
    count = task.count
    if 0 < index <= count:
        task.remove_by_index(index-1)
    else:
        print('\033[31m Selected Index is not in task list \033[0m')
        time.sleep(1)
        input_taken = False
        show_menu()
        #remove_task()

def navi_menu(current_menu):
    global available_menu
    available_menu = []
    nav_menu = ""
    for menu in menues:
        if menu is current_menu or (task.count <= 0 and (menu is 3 or menu is 4)):
            continue
        nav_menu += (f"[{menu}-{menues[menu]}] ")
        available_menu.append(menu)
    print(tabulate(([nav_menu],)))

def clear_screen():
    if os.name == "posix": # POSIX systems (Linux, MacOS)
        os.system("clear")
    elif os.name == "nt":  # Windows
        os.system("cls")

if __name__ == "__main__":
    main()