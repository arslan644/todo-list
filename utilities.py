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
