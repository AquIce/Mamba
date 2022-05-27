from shell import *
from file import *

modes = ('shell', 'file')
mode = ''

while not mode in modes:
  mode = input('Which mode would you like to compile >>> ')

  if mode == 'shell': shell()
  elif mode == 'file': file()