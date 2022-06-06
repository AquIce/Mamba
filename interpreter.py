'''
 >>> Code by Lil_Tim
 >>> Mamba Programming Language
'''

# Import all modules
import os
import atexit

# Import local files
import memory
import errors
import syntax
import features

# Call the clear_memory function when the code exits
atexit.register(memory.clear_memory)

def code_input():
    '''
    Display coding interface and return entered code
    '''
    code = []
    temp = ''
    os.system('cls')
    print('Mamba interpreter - (c) Lil_Tim\n')
    # Loop while the line is not equal to the exit line code (_end)
    while temp != syntax.SYNTAX['end-code-line']:
        temp = input('>>> ')
        code.append(temp)
    return code

def get_list(values):
    '''
    Return a formated list of values
    '''
    open = False
    listDelOpen = False
    final = ''
    # Delete the first character if it is a space
    if values[0] == ' ':
        values = values[1:]
    # Remove the start list character ([) and the end list character (])
    list = features.list_from_char_to_char(values,syntax.SYNTAX['list']['start'],syntax.SYNTAX['list']['stop'])[1:-1]
    for i in list:
        if i in ['\'','"']: open = not open
        elif i in [syntax.SYNTAX['list']['start'],syntax.SYNTAX['list']['stop']] and not open:
            listDelOpen = not listDelOpen; 
            if i == syntax.SYNTAX['list']['start']: 
                temp = get_list(list).split(',')
                print(list,temp)
                list = features.remove(list,temp)
                print(list)
                final += temp
        elif i == ' ' and not open: continue
        final += i
        
    return final

def execute(code):
    '''
    Execute the specified code with Mamba interpreter
    '''
    line = features.to_list(code)
    open = False
    listDelOpen = False
    if code == syntax.SYNTAX['end-code-line']:
        return
    elif code == syntax.SYNTAX['pause-code-line']:
        input('Press enter to continue...')
    elif line[0]+line[1] == syntax.SYNTAX['const']:
        temp = line[2:]
        const_name,value = '',''
        for i in temp:
            if i == ' ': continue
            elif i == '=': break
            else: const_name += i
        temp2 = features.to_string(temp).split('=')[1]
        for i in temp2:
            if i in ['\'','"']: open = not open
            elif i == syntax.SYNTAX['list']['start'] and not open: 
                listDelOpen = not listDelOpen; 
                if i == syntax.SYNTAX['list']['start']: 
                    get_list(temp2)
            elif i == ' ' and not open: continue
            value += i
        if open: errors.show_error(3)
        if listDelOpen: errors.show_error(6)
        memory.into_item(const_name, value, True, True)
    elif line[0] == syntax.SYNTAX['var']:
        temp = line[1:]
        var_name,value = '',''
        for i in temp:
            if i == ' ': continue
            elif i == '=': break
            else: var_name += i
        temp2 = features.to_string(temp).split('=')[1]
        for i in temp2:
            if i in ['\'','"']: open = not open
            elif i in [syntax.SYNTAX['list']['start'],syntax.SYNTAX['list']['stop']] and not open:
                listDelOpen = not listDelOpen; 
                if i == syntax.SYNTAX['list']['start']: 
                    print(get_list(temp2))
            elif i == ' ' and not open: continue
            value += i
        if open: errors.show_error(3)
        if listDelOpen: errors.show_error(6)
        memory.into_item(var_name, value, True)
    elif line[0] == syntax.SYNTAX['pointer']:
        temp = line[1:]
        name,value = '',''
        for i in temp:
            if i == ' ': continue
            elif i == '=': break
            else: name += i
        temp2 = features.remove(features.to_string(temp).split('=')[1],' ')
        for i in temp2:
            if i in ['\'','"']: errors.show_error(7)
            elif i in ['[',']']: errors.show_error(7)
            value += i
        if open: errors.show_error(3)
        if listDelOpen: errors.show_error(6)
        vars = memory.get_varnames()
        if value in vars:
            addr = memory.get_address(value)
            memory.into_item(name,addr, True,is_pointer=True)
    vars = memory.get_varnames()
    for i in vars:
        if code.startswith(i):
            if i in memory.DATAS['2']:
                errors.show_error(4)
            temp = features.to_list(features.remove(features.remove(code,i),'='))
            value = ''
            for j in temp:
                if j in ['\'','"']: open = not open
                elif i in ['[',']']: listDelOpen = not listDelOpen; continue
                elif j == ' ' and not open: continue
                value += j
            if open: errors.show_error(3)
            if listDelOpen: errors.show_error(6)
            memory.into_item(i, value, False)

def exec(code):
    for line in code:
        if line != '':
            execute(line)

code = code_input()
exec(code)