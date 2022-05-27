import os
from compiler import *

def shell():
  os.system('cls')
  code = []
  rep = True
  line = 'NONE'
  while line != '':
    line = input('>>> ')
    code.append(line)
  compile(code)