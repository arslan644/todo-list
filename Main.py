import sys, os, time, Menu, user_auth
from Todo_List import Todo_List
from tabulate import tabulate

todo_list = Todo_List()
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

def app_title():
    print(tabulate((["|     ToDo List      |"],)))

def save_tasks():
    if todo_list._count > 0:
        todo_list.save_data()
    else:
        todo_list.delete_file()

def main():
    #authenticate()
    show_menu()

def authenticate():
    clear_screen()
    app_title()
    print(tabulate((["1: Login", "2: Signup", "3: Exit"],), tablefmt="mixed_outline"))
    Selection = input("Select: ")
    match int(Selection):
        case 1:
            user_auth.login_user()
        case 2:
                user_auth.signup_user()
        case 3:
            clear_screen()
            sys.exit()
        case _:
            print('\033[31m Invalid Input\033[0m')
            time.sleep(2)
            authenticate()
        

def show_menu():
    clear_screen()
    app_title()
    open_current_menu()
    Menu.navi_menu()
    try:
        Menu.select_menu()
    except KeyboardInterrupt:
        exit_progarm()
    show_menu()
 
def open_current_menu():                  
    match Menu.current_menu:
        case Menu.main_menu:
            print(f"List Name: [\033[32m {todo_list.name} \033[0m]")
        case Menu.add_menu:
            add_task()
        case Menu.view_menu:
            view_tasks()
        case Menu.remove_menu:
            remove_task()
        case Menu.mark_menu:
            mark_task()
        case Menu.eixt_menu:
            exit_progarm()
        case _:
            show_menu()

def view_tasks(style_no=22):
    if todo_list.task_count <= 0:
        print(tabulate((['\033[47m \033[30m No Tasks \033[0m' ],), tablefmt="mixed_outline"))
    else:
        if len(sys.argv) > 1:
            todo_list.view(sys.argv[1])
        else:
            index = bound_in_range(style_no)
            todo_list.view(style=styles[index])
        
def bound_in_range(number):
    lower_bound = 0
    upper_bound = len(styles) - 1
    return max(min(number, upper_bound), lower_bound)

def add_task():
    print("(Note: Press 'ctr + c' to save)")
    print("Add Task:")
    print_previous_tasks()
    exit = False
    while not exit:
        try:
            new_task = input(f"{todo_list.task_count + 1}: ")
            verify_task_input(new_task)
            todo_list.add(new_task.strip())
        except KeyboardInterrupt:
            Menu.current_menu = Menu.main_menu
            exit = True
    show_menu()

def verify_task_input(new_task):
    if not new_task.strip():
        print('\033[31m can\'t add empty task \033[0m')
        time.sleep(1)
        show_menu()
    elif  already_in_list(new_task.strip()):
        print('\033[31m task already exist \033[0m')
        time.sleep(1)
        show_menu()
    
def already_in_list(new_task):
    if todo_list.task_count <= 0:
        return False
    
    for i in range(todo_list.task_count):
        if new_task in todo_list.tasks[i]:
            return True

def print_previous_tasks():
    if todo_list.task_count > 0:
        for i in range(todo_list.task_count):
            print(f"{i + 1}: {todo_list.tasks[i][0]}")

def mark_task():
    global input_taken
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
        Menu.current_menu = Menu.main_menu
        show_menu()

def mark_by_name(text):
    todo_list.mark_by_name(text)

def mark_by_index(text):
    index = int(text)
    count = todo_list.task_count
    if 0 < index <= count:
        todo_list.mark_by_index(index-1)
    else:
        print('\033[31m Selected Index is not in task list \033[0m')
        mark_task()

def exit_progarm():
    print("Are you Sure?")
    print(tabulate((["1-Yes", " 0-No"],), tablefmt="mixed_outline"))
    user_input = ""
    while user_input not in ["1", "0"]:
        try:
            user_input = input()
        except KeyboardInterrupt:
            show_menu()
        if user_input == "1":
            save_tasks()
            clear_screen()
            sys.exit()
        elif user_input == "0":
            Menu.current_menu = Menu.main_menu
            show_menu()
        else:
            print('\033[31m Invalid Selection \033[0m')

def remove_task():
    global input_taken
    if not input_taken:
        print(" Remove Task ")
        view_tasks()
        print("(Note: Press 'ctr + c' to go back)")
    try: 
        if todo_list.task_count == 0:
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
        Menu.current_menu = Menu.main_menu
        show_menu()

def remove_by_name(text):
    global input_taken
    if not todo_list.remove_by_name(text):
        print('\033[31m Task name is not in task list \033[0m')
        time.sleep(1)
        input_taken = False
        show_menu()

def remove_by_index(text):
    global input_taken
    index = int(text)
    count = todo_list.task_count
    if 0 < index <= count:
        todo_list.remove_by_index(index-1)
    else:
        print('\033[31m Selected Index is not in task list \033[0m')
        time.sleep(1)
        input_taken = False
        show_menu()
        #remove_task()

def clear_screen():
    if os.name == "posix": # POSIX systems (Linux, MacOS)
        os.system("clear")
    elif os.name == "nt":  # Windows
        os.system("cls")

if __name__ == "__main__":
    main()