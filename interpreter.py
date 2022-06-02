import os

import memory
import errors
import syntax
import features

MAX_CODE_LINES = 1000

def code_input():
    code = []
    temp = ''
    os.system('cls')
    print('Mamba interpreter - (c) Lil_Tim\n')
    while temp != syntax.SYNTAX['end-code-line']:
        temp = input('>>> ')
        code.append(temp)
    return code

def execute(code):
    line = features.to_list(code)
    vars = memory.get_varnames()
    open = False
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
            if i in ['\'','"']: open = not open; continue
            elif i == ' ' and not open: continue
            value += i
        if open: errors.show_error(3)
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
            if i in ['\'','"']: open = not open; continue
            elif i == ' ' and not open: continue
            value += i
        if open: errors.show_error(3)
        memory.into_item(var_name, value, True)
    for i in vars:
        if code.startswith(i):
            if i in memory.DATAS['2']:
                errors.show_error(4)
            temp = features.to_list(features.remove(features.remove(code,i),'='))
            value = ''
            for j in temp:
                if j in ['\'','"']: open = not open; continue
                elif j == ' ' and not open: continue
                value += j
            if open: errors.show_error(3)
            memory.into_item(i, value, False)

code = code_input()

for line in code:
    if line != '':
        execute(line)

memory.clear_memory()