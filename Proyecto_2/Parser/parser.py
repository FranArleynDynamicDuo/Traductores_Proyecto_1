'''
Created on Feb 1, 2016

@author: francisco
'''

import ply.yacc as yacc;

# Get the token map from the lexer.  This is required.
from Proyecto_1.Lexer.Lexer import lexer;
tokens = lexer.tokens;

# ESTOS SON EJEMPLOS DE LAS EXPRESIONES, HAY QUE HACER EXPRESIONES ASI PARA CADA TIPO DE TOKEN DE
# ESTA LISTA


'''
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
'''

# def p_expression_plus(p):
#     'expression : expression PLUS term'
#     p[0] = p[1] + p[3]
# 
# def p_expression_minus(p):
#     'expression : expression MINUS term'
#     p[0] = p[1] - p[3]
# 
# def p_expression_term(p):
#     'expression : term'
#     p[0] = p[1]
# 
# def p_term_times(p):
#     'term : term TIMES factor'
#     p[0] = p[1] * p[3]
# 
# def p_term_div(p):
#     'term : term DIVIDE factor'
#     p[0] = p[1] / p[3]
# 
# def p_term_factor(p):
#     'term : factor'
#     p[0] = p[1]
# 
# def p_factor_num(p):
#     'factor : NUMBER'
#     p[0] = p[1]
# 
# def p_factor_expr(p):
#     'factor : LPAREN expression RPAREN'
#     p[0] = p[2]
# 
# # Error rule for syntax errors
# def p_error(p):
#     print("Syntax error in input!")


# Build the parser
parser = yacc.yacc()
