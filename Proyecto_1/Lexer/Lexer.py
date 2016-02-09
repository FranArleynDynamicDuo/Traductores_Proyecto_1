'''
Created on 22 de sept. de 2015

@author: francisco
'''

import ply.lex as lex


# Lista de tipos de tokens
tokens = ['TkNum','TkCaracter','TkCollect',
          'TkComa','TkPunto','TkDosPuntos','TkParAbre','TkParCierra',
          'TkSuma','TkResta','TkMult','TkDiv','TkMod','TkConjuncion',
          'TkDisyuncion','TkNegacion','TkMenor','TkMenorIgual',
          'TkMayor','TkMayorIgual','TkIgual','TkIdent']

reserved = {
    'create' : 'TkCreate',
    'execute' : 'TkExecute',
    'end' : 'TkRecieve',
    'activate' : 'TkActivate',
    'advance' : 'TkAdvance',
    'on' : 'TkOn',
    'deactivate' : 'TkDeactivate',
    'if' : 'TkIf',
    'else' : 'TkElse',
    'while' : 'TkWhile',
    'end' : 'TkEnd',
    'store' : 'TkStore',
    'recieve' : 'TkRecieve',
    'drop' : 'TkDrop',
    'left' : 'TkLeft',
    'right' : 'TkRight',
    'up' : 'TkUp',
    'down' : 'TkDown',
    'read' : 'TkRead',
    'send' : 'TkSend',
    'activation' : 'TkActivation',
    'deactivation' : 'TkDeactivation',
    'default' : 'TkDefault',
    'false' : 'TkFalse',
    'true' : 'TkTrue',
    'int' : 'TkInt',
    'bool' : 'TkBool',
    'char' : 'TkChar',
    'bot' : 'TkBot',
}
tokens += reserved.values()


##################### Expresiones ##############################################

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

# Literales

t_TkNum = '[0-9]+'
t_TkCaracter = "'(.)'"

#t_TkIdent = '[a-zA-Z][a-zA-Z0-9_]*'
def t_TkCollect(t):
    r'collect as|collect'
    return t

#t_TkIdent = '[a-zA-Z][a-zA-Z0-9_]*'
def t_TkIdent(t):
    r'[a-zA-Z][a-zA-Z0-9_]*'
    if t.value in reserved:
        t.type = reserved[ t.value ]
    return t



# Caracteres Ignorados

t_ignore_spaces = '\s+' # Se ignoran los espacios en blanco de cualquier tipo

# Comentarios a ser ignorados por el lexer

def t_COMMENT(t):
    
    '\$-([^\-]|((\-)+[^\$]))*(\-)(\$)'
    pass
    # No se hace nada con el contenido de los comentarios
 
# Regla para calcular el numero de linea en el que se encuentra el token

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
    t.lexer.current = t.lexer.lexpos - 1
   
# Regla para manejar los caracteres invalidos
def t_error(t):
    print('Error: Caracter inesperado "%s" en la fila %s columa %s' % 
          (t.value[0],t.lineno,t.lexer.lexpos - t.lexer.current))
    t.lexer.skip(1)
    t.lexer.error_Found = True

# Creamos el lexer
botLexer = lex.lex()
