def remove(string, substring,times=1):
    return string.replace(substring,'',times)

def to_list(string):
    list = []
    for i in string:
        list.append(i)
    return list

def to_string(list):
    string = ''
    for i in list:
        string += i
    return string