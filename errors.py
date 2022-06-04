'''
 >>> Code by Lil_Tim
 >>> Mamba Programming Language
'''

ERRORS = [
    ['0 - ERROR - FATAL_ERROR', 'System shutdown'],
    ['1 - ERROR - Address allocation failure','This address can not be allocated'],
    ['2 - ERROR - Memory allocation failure','Your allowed memory space is full'],
    ['3 - ERROR - String literal not terminated','You must provide a valid string'],
    ['4 - ERROR - Constant reassignation failure','You can not reassign a constant'],
    ['5 - ERROR - Variable recration failure','You can not create a variable who already exists'],
    ['6 - ERROR - List literal not terminated','You must provide a valid list'],
    ['7 - ERROR - Invalid  pointer address','A pointer must design a variable or a constant'],
]

def show_error(id):
    print('\n--------------------------------\n')
    print(ERRORS[id][0],end=' ')
    print('(',ERRORS[id][1],')')
    exit(1)