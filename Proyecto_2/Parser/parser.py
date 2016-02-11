#Created on Feb 1, 2016
#@author: francisco

import ply.yacc as yacc;

# Get the token map from the lexer.  This is required.
from Proyecto_1.Lexer.Lexer import tokens as botTokens
from Proyecto_2.Parser import Expression
from Proyecto_2.Parser import Instruction

tokens = botTokens;

#-----------------------> PROGRAMA GENERAL <------------------------

def p_program(p):
    # Camino 1: Hay un bloque create y un bloque execute
    # Camino 2: Hay un bloque execute
    '''program : TkCreate botCreateList TkExecute execute TkEnd
               | TkExecute execute TkEnd'''
    
    # POR AQUI NO ESTA PASANDO
    if len(p) == 6:
        p[0] = Instruction.Program(createSet = p[2],executeSet = p[4])
    if len(p) == 4:
        p[0] = Instruction.Program(createSet = None,executeSet = p[2])
    p.set_lineno(0,p.lineno(1)) 

#----------------------->   EXPRESIONES  <------------------------'''

def p_empty(p):
    'empty :'
    pass

def p_expression(p):
    '''expression : TkParAbre expression TkParCierra
                  | expression TkSuma expression
                  | expression TkResta expression
                  | expression TkMult expression
                  | expression TkDiv expression
                  | expression TkMod expression
                  | expression TkConjuncion expression
                  | expression TkDisyuncion expression
                  | expression TkMenor expression
                  | expression TkMenorIgual expression
                  | expression TkMayor expression
                  | expression TkMayorIgual expression
                  | expression TkIgual expression
                  | TkNegacion expression                  
                  | TkNum                    
                  | TkFalse
                  | TkTrue                        
                  | TkIdent'''
    if len(p) == 4:
        if ((p[2] == "+") or (p[2] == "-") or (p[2] == "*") or (p[2] == "/") or (p[2] == "%")):
            p[0] = Expression.ArithmethicExpression(p[1],p[2],p[3])
        elif ((p[2] == "/\\") or (p[2] == "\/")):
            p[0] = Expression.BooleanExpression(p[1],p[2],p[3])
        elif ((p[2] == "<") or (p[2] == "<=") or (p[2] == ">") or (p[2] == ">=") or (p[2] == "=")):
            p[0] = Expression.RelationalExpresion(p[1],p[2],p[3])    
        elif ((p[1] == "(") and (p[3] == ")")):
            p[0] = Expression.BooleanExpression(p[1],p[2],p[3])                     
    elif len(p) == 3:             
        p[0] = Expression.BooleanExpression(expresion1= p[2], operador = p[1])        
    elif len(p) == 2:                    
        p[0] = p[1]   


#---------------------------> CREATE <----------------------------

def p_botCreateList(p):
    '''botCreateList :    botCreate botCreateList
                     |    empty''' # Asi cortamos la lista'''
    
    if len(p) == 3:
        if p[0] == None:    
            p[0] = [p[1],p[2]]      
        else:    
            p[0] = p[0].append(p[1])
            p[0] = p[0].extend(p[2])
    
def p_botCreate(p):
    '''botCreate :       TkInt  TkBot TkIdent botDeclaracionList TkEnd
                 |       TkBool TkBot TkIdent botDeclaracionList TkEnd
                 |       TkChar TkBot TkIdent botDeclaracionList TkEnd'''
    p[0] = Instruction.CreateInstruction(p[1],p[3],p[4])
    p.set_lineno(0,p.lineno(1)) 

def p_botDeclaracionList(p):
    '''botDeclaracionList :    botDeclaracion botDeclaracionList
                          |    empty'''
    if len(p) == 3:
        if p[0] == None:
            p[0] = [p[1],p[2]]  
        else:          
            p[0] = p[0].append(p[1])
            p[0] = p[0].extend(p[2])
            
def p_botDeclaracion(p):
    '''botDeclaracion  :    TkOn TkActivation TkDosPuntos botInstruccionList TkEnd
                    |       TkOn TkDeactivation TkDosPuntos botInstruccionList TkEnd
                    |       TkOn expression TkDosPuntos botInstruccionList TkEnd
                    |       TkOn TkDefault TkDosPuntos botInstruccionList TkEnd'''
    p[0] = Instruction.BotDeclaration(p[2],p[4])
    p.set_lineno(0,p.lineno(1)) 
    

def p_botInstruccionList(p):
    '''botInstruccionList  :    botInstruccion botInstruccionList 
                           |    empty''' # Asi cortamos la lista
    if len(p) == 3:
        if p[0] == None:
            p[0] = [p[1],p[2]]
        else:
            p[0] = p[0].append(p[1])
            p[0] = p[0].extend(p[2])

def p_botInstruccion(p):
    '''botInstruccion :    TkStore TkNum TkPunto
                   |       TkStore TkCaracter TkPunto
                   |       TkCollect TkPunto
                   |       TkCollect TkIdent TkPunto                   
                   |       TkRecieve TkPunto
                   |       TkDrop TkNum TkPunto
                   |       TkDrop TkCaracter TkPunto
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
# -----------------------> INSTRUCCIONES <--------------------------

def p_execute(p):
    '''execute :    execCont execute
               |    empty''' # Asi cortamos la lista'''

    if len(p) == 3:
        if p[0] == None:
            p[0] = [p[1]]
        else:
            p[0].append(p[1])
            p[0] = p[0].extend(p[2])


def p_identList(p):
    '''identList   :    TkIdent TkPunto
                   |    TkIdent TkComa identList'''
    if p[0] == None:
        p[0] = [p[1]]
    else:
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
    '''conditional  :    TkIf expression TkDosPuntos execCont TkElse execCont TkEnd
                    |    TkIf expression TkDosPuntos execCont TkEnd'''
    if len(p) == 8:
        p[0] = Instruction.ConditionalInstruction(p[2],p[4],p[6])
    elif len(p) == 6:
        p[0] = Instruction.ConditionalInstruction(p[2],p[4])

def p_while(p):
    '''while        :    TkWhile expression TkDosPuntos execCont TkEnd'''
    p[0] = Instruction.whileInstruction(p[2],p[4])

def p_activate(p):
    '''activate     :    TkActivate identList'''
    p[0] = Instruction.ActivateInstruction(p[2])
    p.set_lineno(0,p.lineno(1)) 
    
def p_deactivate(p):
    '''deactivate     :    TkDeactivate identList'''
    p[0] = Instruction.DeactivateInstruction(p[2])    
    
def p_advance(p):
    '''advance     :    TkAdvance identList'''
    p[0] = Instruction.AdvanceInstruction(p[2])      
    
# Error rule for syntax errors
def p_error(p):
    if p is not None:
        print("Syntax error (%s) at line %s column %s"%(
                                                        p.value ,
                                                        p.lexer.lineno -18,
                                                        p.lexer.lexpos - p.lexer.current
                                                        )
            )
        exit()
    else:
        print("Syntax error at EOF")
        exit()
# Lista de precedencia en los operandos
#
precedence = (
    ('left','TkParAbre','TkParCierra'),
    ('left','TkMult','TkDiv','TkMod'),
    ('left','TkSuma','TkResta'),
    ('left','TkMenor','TkMenorIgual','TkMayor','TkMayorIgual'),
    ('left','TkIgual'),
    ('left','TkNegacion'),
    ('left','TkConjuncion'),
    ('left','TkDisyuncion'),
)

# Build the parser
BotParser = yacc.yacc(start='program',debugfile="debug.txt")
