'''
Created on 22 de sept. de 2015

@author: francisco
'''

import ply.lex as lex

tokens = ['TkCreate','TkIdent','TkNum','TkFalse','TkTrue','TkCaracter',
          'TkComa','TkPunto','TkDosPuntos','TkParAbre','TkParCierra','TkSuma','TkResta',
          'TkMult','TkDiv','TkMod','TkConjuncion','TkDisyuncion','TkNegacion','TkMenor',
          'TkMenorIgual','TkMayor','TkMayorIgual','TkIgual']

# Palabras Clave

t_TkComa = r'create'
t_TkIdent = r'[a-zA-Z_][a-zA-Z0-9_]*'
t_TkNum = '[0-9]+'
t_TkFalse = r'false'
t_TkTrue = r'true'
t_TkCaracter = '.'

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

t_ignore = r'\n | \t'


lex.lex()