ERRORS = [
    ['ERROR 0 - FATAL_ERROR', 'System shutdown'],
    ['ERROR 1 - Address allocation failure','This address can not be allocated'],
    ['ERROR 2 - Memory allocation failure','Your allowed memory space is full'],
    ['ERROR 3 - String literal not terminated','You must provide a valid string'],
    ['ERROR 4 - Constant reassignation failure','You can not reassign a constant'],
    ['ERROR 5 - Variable recration failure','You can not create a variable who already exists'],
]

def show_error(id):
    print('\n--------------------------------\n')
    print(ERRORS[id][0],end=' ')
    print('(',ERRORS[id][1],')')
    exit(1)