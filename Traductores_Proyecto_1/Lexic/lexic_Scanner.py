'''
Created on 22 de sept. de 2015

@author: francisco
'''

import ply.lex as lex

tokens = ['TkComa','TkPunto','TkDosPuntos','TkParAbre','TkParCierra','TkSuma','TkResta',
          'TkMult','TkDiv','TkMod','TkConjuncion','TkDisyuncion','TkNegacion','TkMenor',
          'TkMenorIgual','TkMayor','TkMayorIgual','TkIgual']




t_TkComa = r','
t_TkPunto = r'\.'
t_TkDosPuntos = r':'
t_TkParAbre = r'\(' 
t_TkParCierra = r'\)'
t_TkSuma = r'\+' 
t_TkResta = r'-' 
t_TkMult = r'\*' 
t_TkDiv = r'/' 
t_TkMenor = r'<' 
t_TkMenorIgual = r'<=' 
t_TkMayor = r'>' 
t_TkMayorIgual = r'>=' 
t_TkIgual = r'=' 

# Caracteres Ignorados

t_ignore = " \t"


lex.lex()