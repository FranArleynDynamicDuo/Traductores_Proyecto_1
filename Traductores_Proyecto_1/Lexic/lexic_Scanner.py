'''
Created on 22 de sept. de 2015

@author: francisco
'''

import ply.lex as lex

tokens = [ 'NAME','NUMBER','PLUS','MINUS','TIMES',
           'DIVIDE', 'EQUALS' ]

literals = ['=','+','-','*','/', '(',')']

t_ignore = ' \t'         
t_PLUS   = r'\+'
t_MINUS  = r'-'
t_TIMES  = r'\*'
t_DIVIDE = r'/'
t_EQUALS = r'='
t_NAME   = r'[a-zA-Z_][a-zA-Z0-9_]*'


def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

lex.lex()