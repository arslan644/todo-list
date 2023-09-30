textColors = {  
                "black":    "\x1b[30m", 
                "red":      "\x1b[31m",
                "green":    "\x1b[32m",
                "yellow":   "\x1b[33m",
                "blue":     "\x1b[34m",
                "magenta":  "\x1b[35m",
                "cyan":     "\x1b[36m",
                "white":    "\x1b[37m",
            }
bgColors = {
                "black":    "\x1b[40m",
                "red":      "\x1b[41m",
                "green":    "\x1b[42m",
                "yellow":   "\x1b[43m",
                "blue":     "\x1b[44m",
                "magenta":  "\x1b[45m",
                "cyan":     "\x1b[46m",
                "white":    "\x1b[47m",
            }

def remove_last_occurence(string, character):
    last_index = string.rfind(character)
    if last_index != -1:
        return string[:last_index] + string[last_index+1:]
    else:
        raise ValueError("Character not in string")

def list_to_string(l=[]):
    s = ""
    for i in l:
        s += f"{i}, "
    return remove_last_occurence(s, ", ")

def printColoredText(text, color, reset = True):
    print(f"{textColors[color]}{text}")
    if reset:
        resetFormatting()

def changeTextColor(color, text="", reset = True):
    print(f'{textColors[color]}{text}', end='')
    if reset:
        resetFormatting()

def changeBgColor(bgcolor, text="", reset= True):
    print(f'{bgColors[bgcolor]}{text}', end='')
    if reset:
        resetFormatting()
    
def getColoredText(text, color):
    return f'{textColors[color]}{text}'

def resetFormatting():
    print(f'\x1b[0m', end='')