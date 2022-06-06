'''
 >>> Code by Lil_Tim
 >>> Useful Python Features
'''

def remove(string, substring,times=1):
    return string.replace(substring,'',times)

def to_list(string):
    list = []
    for i in string:
        list.append(i)
    return list

def to_string(list,separator=''):
    string = ''
    for i in list:
        string += str(i)
        if i != list[-1]:
            string += separator
    return string

def get_index(list,value,number=1):
    for i in range(len(list)):
        if list[i] == value:
            return i
        
        
def list_from_char_to_char(list, first_char, second_char):
    return list[list.index(first_char):list.rindex(second_char)+1]