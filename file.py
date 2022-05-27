import os
from compiler import *

def file():
  os.system('cls')
  fileToCompile = input('File to compile >>> ')

  with open(fileToCompile, 'r') as file:
    code = file.readlines()

  compile(code)