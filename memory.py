import json
import os
import re

import syntax
import errors

DATAS = {
    '0':'Mamba - DEV', # System version constant
    '1':['0','1','2'], # Locked addresses (only access via system)
    '2':[], # Const addresses (can be casted to variables)
}

MAX_MEMORY = 2048 # Maximum memory allowed

class Memory_Object:
    def __init__(self,name,value,init,is_const=False,address=None):
        load_storage()
        save_storage()
        self.name = name
        self.value = value
        self.var = [self.name,self.value]
        self.init = init
        self.is_const = is_const
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
            if key not in DATAS['1'] and DATAS[key][0] == self.name:
                return key

    def add_to_memory(self):
        if self.check_var() != None:
            self.address = self.check_var()
            if self.is_const:
                errors.show_error(4)
            elif self.init:
                errors.show_error(5)
        else:
            if self.is_const: DATAS['2'].append(str(self.address))
        DATAS[str(self.address)] = self.var
        save_storage()

def save_storage():
    if not os.path.exists(syntax.SYNTAX['json-file']):
        with open(syntax.SYNTAX['json-file'],'x'): ...
    with open(syntax.SYNTAX['json-file'], 'w') as f:
        json.dump(DATAS,f,indent=2)

def load_storage():
    if os.path.exists(syntax.SYNTAX['json-file']) and os.stat(syntax.SYNTAX['json-file']).st_size != 0:
        with open(syntax.SYNTAX['json-file'], 'r') as f:
            global DATAS
            DATAS = json.load(f)

def get_varnames():
    load_storage()
    vars = [DATAS[i][0] for i in DATAS if not i in DATAS['1']]
    return vars

def into_item(name,value,init,is_const=False,address=None):
    item = Memory_Object(name,value,init,is_const,address)

def clear_memory():
    global DATAS
    DATAS = {
        '0':'Mamba - DEV', # System version constant
        '1':['0','1','2'], # Locked addresses (only access via system)
        '2':[], # Const addresses (can be casted to variables)
    }
    save_storage()