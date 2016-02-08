'''
Created on Feb 1, 2016

@author: francisco
'''

import ply.yacc as yacc;

# Get the token map from the lexer.  This is required.
from Proyecto_1.Lexer.Lexer import lexer;
from Proyecto_2.Parser import Expression
from Proyecto_2.Parser import Instruction
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

def p_empty(p):
    'empty :'
    pass

'''----------------------->   EXPRESIONES  <------------------------'''

def p_aritExpr(p):
    '''aritExpr : TkParAbre aritExpr TkParCierra
                | aritExpr TkSuma aritExpr
                | aritExpr TkResta aritExpr
                | aritExpr TkMult aritExpr
                | aritExpr TkDiv aritExpr
                | aritExpr TkMod aritExpr
                | TkNum
                | tkIdent '''
    if len(p) == 4:
        p[0] = Expression.ArithmethicExpression(p[1],p[2],p[3])
    elif len(p) == 2:                    
        p[0] = Expression.ArithmethicExpression(p[1])

def p_boolExpr(p):
    'boolExpr : TkParAbre boolExpr TkParCierra'
    '         | boolExpr TkConjuncion boolExpr'
    '         | boolExpr TkDisyuncion boolExpr'
    '         | TkNegacion boolExpr'
    '         | relExpr'
    '         | TkFalse'
    '         | TkTrue'
    '         | tkIdent'
    if len(p) == 4:
        p[0] = Expression.BooleanExpression(p[1],p[2],p[3])
    elif len(p) == 3:                    
        p[0] = Expression.BooleanExpression(p[1],p[2])        
    elif len(p) == 2:                    
        p[0] = Expression.BooleanExpression(p[1])

def p_relExpr(p):
    '''relExpr : TkParAbre relExpr TkParCierra
               | relExpr TkMenor relExpr
               | relExpr TkMenorIgual relExpr
               | relExpr TkMayor relExpr
               | relExpr TkMayorIgual relExpr
               | relExpr TkIgual relExpr         
               | aritExpr
               | tkIdent'''
    if len(p) == 4:
        p[0] = Expression.RelationalExpresion(p[1],p[2],p[3])
    elif len(p) == 2:                    
        p[0] = Expression.RelationalExpresion(p[1])

'''-----------------------> PROGRAMA GENERAL <------------------------'''

def p_program(p):
    # Camino 1: Hay un bloque create y un bloque execute
    # Camino 2: Hay un bloque execute
    '''program : TkCreate botCreateList TkExecute execute TkEnd
               | TkExecute execute TkEnd'''
    if len(p) == 6:
        p[0] = Expression.Program(createSet = p[2],executeSet = p[4])
    if len(p) == 4:
        p[0] = Expression.Program(createSet = None,executeSet = p[2])
 
'''---------------------------> CREATE <----------------------------'''

def p_botCreateList(p):
    '''botCreateList :    botCreate botCreateList
                     |    empty''' # Asi cortamos la lista'''
    
    if len(p) == 3:
        p[0] = p[0].append(p[1])
        p[0] = p[0].extend(p[2])
    
def p_botCreate(p):
    '''botCreate :       TkInt  TkBot TkIdent botDeclaracionList TkEnd
                 |       TkBool TkBot TkIdent botDeclaracionList TkEnd
                 |       TkChar TkBot TkIdent botDeclaracionList TkEnd'''
    p[0] = Instruction.CreateInstruction(p[1],p[3],p[4])

def p_botDeclaracionList(p):
    '''botDeclaracionList :    botDeclaracion botDeclaracionList
                          |    empty'''
    if len(p) == 3:
        p[0] = p[0].append(p[1])
        p[0] = p[0].extend(p[2])

def p_botDeclaracion(p):
    '''botDeclaracion  :    TkOn TkActivation TkDosPuntos botInstruccionList TkEnd
                    |       TkOn TkDeactivation TkDosPuntos botInstruccionList TkEnd
                    |       TkOn boolExpr TkDosPuntos botInstruccionList TkEnd
                    |       TkOn TkDefault TkDosPuntos botInstruccionList TkEnd'''
    p[0] = Instruction.BotDeclaration(p[2],p[3],p[4])

def p_botInstruccionList(p):
    '''botInstruccionList  :    botInstruccion botInstruccionList 
                           |    empty''' # Asi cortamos la lista
    if len(p) == 3:
        p[0] = p[0].append(p[1])
        p[0] = p[0].extend(p[2])                           

def p_botInstruccion(p):
    '''botInstruccion :    TkStore TkNum TkPunto
                   |       TkStore TkCaracter TkPunto
                   |       TkCollect TkPunto
                   |       TkRecieve TkPunto
                   |       Tkdrop TkNum TkPunto
                   |       Tkdrop TkCaracter TkPunto
                   |       TkSend TkPunto     
                   |       TkRead TkPunto
                   |       TkLeft TkPunto
                   |       TkRight TkPunto
                   |       TkUp TkPunto
                   |       TkDown TkPunto''' # Asi cortamos la lista
    if len(p) == 4:
        p[0] = Instruction.BotInstruction(p[1],p[2])
    if len(p) == 3:
        p[0] = Instruction.BotInstruction(p[1])

''' -----------------------> INSTRUCCIONES <-------------------------- '''

def p_execute(p):
    '''execute :    execCont execute
               |    TkEnd'''
    p[0].append(p[1])
    if len(p) == 3:
        p[0] = p[0].extend(p[2])
    pass   


def p_identList(p):
    '''identList   :    TkIdent TkPunto
                   |    TkIdent TkComa identList'''
    p[0].append(p[1])
    if len(p) == 4:
        p[0].extend(p[3])

def p_execCont(p):
    '''execCont    :    activate
                   |    deactivate
                   |    advance
                   |    conditional
                   |    while''' # Asi cortamos la lista'''
    p[0] = p[1]

def p_conditional(p):
    '''conditional  :    TkIf boolExpr TkDosPuntos cont TkElse cont TkEnd
                    |    TkIf boolExpr TkDosPuntos cont TkEnd'''
    if len(p) == 7:
        p[0] = Instruction.ConditionalInstruction(p[2],p[4],p[6])
    elif len(p) == 5:
        p[0] = Instruction.ConditionalInstruction(p[2],p[4])

def p_while(p):
    '''while        :    TkWhile boolExpr TkDosPuntos cont TkEnd'''
    p[0] = Instruction.whileInstruction(p[2],p[4])

def p_activate(p):
    '''activate     :    TkActivate identList'''
    p[0] = Instruction.ActivateInstruction(p[2])
    
def p_deactivate(p):
    '''deactivate     :    TkDeactivate identList'''
    p[0] = Instruction.DeactivateInstruction(p[2])    
    
def p_advance(p):
    '''advance     :    TkAdvance identList'''
    p[0] = Instruction.AdvanceInstruction(p[2])      

# Build the parser
parser = yacc.yacc()
