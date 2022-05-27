all = {
  'keys':{
    'var': {
      'pre':('const','global'),
      '':['set','']
    },
    'func':('func','function'),
    'object':'obj',
    'loops': {
      'for':'for',
      'while': 'while',
      'do-while':{
        'pre':'do(...)while',
        'open':'...'
      }
    }
  },
  'symbols':{
    'first':'§',
    'func': {
      'start':'<',
      'end':'>'
    },
    'loops': {
      'start':'<',
      'end':'>'
    },
    'args':{
      'start':'(',
      'delimiter':',',
      'end':')'
    },
    'ol-comment':'#',
    'ml-comment': {
      'start':'#*',
      'end':'*#'
    }
  },
  'operators': {
    'invert':'!',
    'arithmetic':('','+','-','*','/','^','!^'),
    'assign':'=',
    'reassign':'',
    'comparison':{
      'sup':('>','>='),
      'equal':('==',)
    }
  }
}

all['operators']['reassign'] = (i + all['operators']['assign'] for i in all['operators']['arithmetic'])
for i in all['operators']['reassign']:
  print(i)