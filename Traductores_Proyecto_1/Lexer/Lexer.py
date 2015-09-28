# -*- encoding: utf-8 -*-
'''
Created on 22 de sept. de 2015

@author: francisco
'''

import sys

import ply.lex as lex

tokens = ['TkCreate','TkExecute',
          'TkRecieve','TkActivate','TkAdvance',
          'TkOn','TkDeactivate',
          'TkIf','TkElse','TkWhile','TkEnd',
          'TkStore','TkCollect','TkDrop','TkLeft','TkRight','TkUp','TkDown',
          'TkRead','TkSend',
          'TkActivation','TkDeactivation','TkCustomCondition','TkDefault',
          'TkIdent','TkNum','TkCaracter','TkFalse','TkTrue',
          'TkInt','TkBool','TkChar',
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
t_TkRecieve = r'recieve'
t_TkAdvance = r'advance'

# Condicionales y Ciclos

t_TkIf = r'if'
t_TkElse = r'else'
t_TkWhile = r'while'

##################### Instrucciones de Robot ###################################

# Basicas

t_TkStore = r'store'
t_TkCollect = r'collect'
t_TkDrop = r'drop'

# Movimiento

t_TkLeft = r'left'
t_TkRight = r'right'
t_TkUp = r'up'
t_TkDown = r'down'

# Entrada y Salida

t_TkRead = r'read'
t_TkSend = r'send'

##################### Condiciones ##############################################

t_TkOn = r'on'
t_TkActivation = r'activation'
t_TkDeactivation = r'deactivation'
t_TkDefault = r'default'

##################### Expresiones ##############################################

# Tipos de datos

t_TkInt = r'int'
t_TkBool = r'bool'
t_TkChar = r'char'

# Literales

t_TkIdent = '[a-zA-Z][a-zA-Z0-9_]*'
t_TkNum = '[0-9]+'
t_TkCaracter = "'(.)'"
t_TkFalse = r'false'
t_TkTrue = r'true'

# Separadores

t_TkComa = r','
t_TkPunto = r'\.'
t_TkDosPuntos = r':'
t_TkParAbre = r'\(' 
t_TkParCierra = r'\)'

# Operadores

t_TkSuma = '\+' 
t_TkResta = r'-'
t_TkMult = r'\*' 
t_TkDiv = r'/' 
t_TkMod = r'%' 
t_TkConjuncion = r'/\\' 
t_TkDisyuncion = r'\\/' 
t_TkNegacion = r'~' 
t_TkMenor = r'<' 
t_TkMenorIgual = r'<=' 
t_TkMayor = r'>' 
t_TkMayorIgual = r'>=' 
t_TkIgual = r'=' 

# Caracteres Ignorados

t_ignore_spaces = '\s+'

# Comentarios a ser ignorados por el lexer

def t_COMMENT(t):
    
    '\$-*([^\-]|((\-)+[^ \$]))*(\-)(\$)'
    pass
    # No return value. Token discarded
 
# Regla para calcular el numero de linea en el que se encuentra el token

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
    t.lexer.current = t.lexer.lexpos - 1      # Added new

'''
# Calculo de columna en la que se encuentra el numero de columna
def find_column(input,token):
    last_cr = str(input).rfind('\n',0,token.lexpos)
    if last_cr < 0:
        last_cr = 0
    column = (token.lexpos - last_cr) + 1
    return column
'''
   
# Regla para manejar los caracteres invalidos
def t_error(t):
    print('Error: Caracter inesperado "%s" en la fila %s columa %s' % 
          (t.value[0],t.lineno,t.lexer.lexpos - t.lexer.current))
    t.lexer.skip(1)
    t.lexer.error_Found = True



# Build the lexer
lexer = lex.lex()
