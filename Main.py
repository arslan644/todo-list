import sys, os
from Task import Task
from tabulate import tabulate


task = Task()
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
    clear_screen()
    display_title()
    main_menu()
    take_input()

def take_input():
    input("Select: ")

def display_title():
    print(tabulate(["ToDo List"]))

def view_tasks(style_no=0):
    styles
    if len(sys.argv) > 1:
        task.view(sys.argv[1])
    else:
        index = bound_in_range(style_no)
        task.view(style=styles[index])
        
def bound_in_range(number):
    lower_bound = 0
    upper_bound = len(styles) - 1
    return max(min(number, upper_bound), lower_bound)

def main_menu():
    menu = [ [" 1-", "Add Task"], [" 2-", "View Tasks"] ]
    print(f'\n{tabulate(menu, tablefmt="plain")}\n')

def navi_menu():
    menu = [["0-Back", "00-Main Menu"]]
    print(tabulate(menu))

def clear_screen():
    os.system("cls")

if __name__ == "__main__":
    main()