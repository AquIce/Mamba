'''
 >>> Code by Lil_Tim
 >>> Useful Python Features
'''

def remove(string: str, substring: str,times : int = 1) -> str:
    return string.replace(substring,'',times)

def to_list(string:str) -> list:
    list = []
    for i in string:
        list.append(i)
    return list

def to_string(list:list,separator=''):
    string = ''
    for i in list:
        string += str(i)
        if i != list[-1]:
            string += separator
    return string
        
        
def list_from_char_to_char(list:list, first_char:str, second_char:str) -> list:
    return list[list.index(first_char):to_string(list).rindex(second_char)+1]