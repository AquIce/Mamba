'''
 >>> Code by Lil_Tim
 >>> Mamba Programming Language
'''

import json
import os

import syntax
import errors

DATAS = {
    '0':'Mamba - DEV', # System version constant
    '1':['0','1','2','3','4'], # Locked addresses (only access via system)
    '2':[], # Const addresses (can be casted to variables)
    '3':[], # Pointer addresses
    '4':[], # List addresses
}

MAX_MEMORY = 2048 # Maximum memory allowed

def set_memory_limit(memory_limit):
    global MAX_MEMORY
    MAX_MEMORY = memory_limit

class Memory_Object:
    def __init__(self,name,value,init,is_const=False,is_pointer=False,address=None):
        load_storage()
        save_storage()
        self.name = name
        self.value = value
        self.var = [self.name,self.value]
        self.init = init
        self.is_const = is_const
        self.is_pointer = is_pointer
        self.address = address

        if self.address == None: self.address = self.find_free_address()
        if self.check_address(): self.add_to_memory() 
        else: errors.show_error(1) # Invalid address

    def check_address(self):
        if str(self.address) in DATAS['1']+DATAS['2']: return False 
        else:return True

    def find_free_address(self):
        for i in range(MAX_MEMORY):
            if not str(i) in DATAS:
                return i
        errors.show_error(2) # Memory full

    def check_var(self):
        for key in DATAS:
            if key not in DATAS['1'] and DATAS[key][0] == self.name: return key

    def add_to_memory(self):
        global DATAS
        if self.check_var() != None:
            key = self.check_var()
            self.address = self.check_var()
            if key in DATAS['2']:
                errors.show_error(4)
            elif self.init:
                errors.show_error(5)
        else:
            if self.is_const: DATAS['2'].append(str(self.address))
            if self.is_pointer: DATAS['3'].append(str(self.address))
        DATAS[str(self.address)] = self.var
        save_storage()

def save_storage(dict = None):
    if dict is None:
        dict = DATAS
    if not os.path.exists(syntax.SYNTAX['json-file']):
        with open(syntax.SYNTAX['json-file'],'x'): ...
    with open(syntax.SYNTAX['json-file'], 'w') as f:
        json.dump(dict,f,indent=2)

def load_storage():
    if os.path.exists(syntax.SYNTAX['json-file']) and os.stat(syntax.SYNTAX['json-file']).st_size != 0:
        with open(syntax.SYNTAX['json-file'], 'r') as f:
            global DATAS
            DATAS = json.load(f)

def get_address(varname):
    for key in DATAS:
        if key not in DATAS['1'] and DATAS[key][0] == varname:
            return key

def get_varnames():
    load_storage()
    vars = [DATAS[i][0] for i in DATAS if not i in DATAS['1']]
    return vars

def into_item(name,value,init,is_const=False,is_pointer=False,address=None):
    item = Memory_Object(name,value,init,is_const,is_pointer,address)

def clear_memory():
    save_storage({
        '0':'Mamba - DEV', # System version constant
        '1':['0','1','2','3','4'], # Locked addresses (only access via system)
        '2':[], # Const addresses (can be casted to variables)
        '3':[], # Pointer addresses
        '4':[], # List addresses
    })