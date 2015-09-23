'''
Created on 22 de sept. de 2015

@author: francisco
'''

import ply.lex as lex

tokens = ['TkCreate','TkExecute',
          'TkStore','TkRecieve','TkActivate','TkAdvance',
          'TkOn','TkDeactivate',
          'TkIf','TkElse','TkWhile','TkEnd',
          'TkStore','TkCollect','TkDrop','TkLeft','TkRight','TkUp','TkDown',
          'TkRead','TkSend',
          'TkActivation','TkDeactivation','TkCustomCondition','TkDefault',
          'TkIdent','TkNum','TkFalse','TkTrue',
          'TkInt','TkBool','TkCaracter',
          'TkComa','TkPunto','TkDosPuntos','TkParAbre','TkParCierra',
          'TkSuma','TkResta','TkMult','TkDiv','TkMod','TkConjuncion',
          'TkDisyuncion','TkNegacion','TkMenor','TkMenorIgual',
          'TkMayor','TkMayorIgual','TkIgual']

##################### Estructura de un Programa ################################

t_TkCreate = r'create'
t_TkExecute = r'execute'
t_TkEnd = r'end'

##################### Instrucciones de Controlador #############################

t_TkActivate = r'activate'
t_TkDeactivate = r'deactivate'
t_TkStore = r'store'
t_TkRecieve = r'recieve'
t_TkAdvance = r'advance'

##################### Instrucciones de Robot ###################################

t_TkStore = r'store'
t_TkCollect = r'collect'
t_TkDrop = r'drop'

# Movimiento

t_TkLeft = r'left'
t_TkRight = r'right'
t_TkUp = r'up'
t_TkDown = r'down'

t_TkOn = r'on'

# Condicionales y Ciclos

t_TkIf = r'if'
t_TkElse = r'else'
t_TkWhile = r'while'

# Entrada y Salida

t_TkRead = r'read'
t_TkSend = r'send'

t_TkActivation = r'activation'
t_TkDeactivation = r'deactivation'
#t_TkCustomCondition = r'end'
t_TkDefault = r'default'

# Literales

t_TkIdent = '[a-zA-Z][a-zA-Z0-9_]*'
t_TkNum = '[0-9]+'
t_TkCaracter = '"."'
t_TkFalse = r'false'
t_TkTrue = r'true'

# Tipos de datos

t_TkInt = r'int'
t_TkBool = r'bool'
t_TkChar = r'char'


# Separadores

t_TkComa = r','
t_TkPunto = r'.'
t_TkDosPuntos = r':'
t_TkParAbre = r'(' 
t_TkParCierra = r')'

# Operadores

t_TkSuma = r'+' 
t_TkResta = r'-' 
t_TkMult = r'*' 
t_TkDiv = r'/' 
t_TkMod = r'%' 
t_TkConjuncion = '/\\' 
t_TkDisyuncion = '\\/' 
t_TkNegacion = r'~' 
t_TkMenor = r'<' 
t_TkMenorIgual = r'<=' 
t_TkMayor = r'>' 
t_TkMayorIgual = r'>=' 
t_TkIgual = r'=' 

# Caracteres Ignorados

t_ignore = '\n | \t'

# Comentarios a ser ignorados por el lexer

def t_COMMENT(t):
    r'\#.*'
    pass
    # No return value. Token discarded

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

lex.lex()