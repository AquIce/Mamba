def compile(code):
  print('Code compiled')
  for i in code:
    cut = True
    if i.startswith(' '):
      cut = False