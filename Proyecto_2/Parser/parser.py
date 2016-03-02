#Created on Feb 1, 2016
#@author: francisco

import ply.yacc as yacc;
from copy import deepcopy

# Get the token map from the lexer.  This is required.
from Proyecto_1.Lexer.Lexer import tokens as botTokens
from Proyecto_2.Parser import Expression
from Proyecto_2.Parser import Instruction
from Proyecto_3.contextAnalisis.contextAnalisis import SymbolTable
from Proyecto_3.contextAnalisis.contextAnalisis import Symbol
from Proyecto_3.contextAnalisis.contextAnalisis import expressionAnalisis

tokens = botTokens;
sintBotSymbolTable = SymbolTable(None);

#-----------------------> PROGRAMA GENERAL <------------------------

def p_program(p):
    # Camino 1: Hay un bloque create y un bloque execute
    # Camino 2: Hay un bloque execute
    '''program : TkCreate botCreateList finishBotList TkExecute executeList TkEnd
               | TkExecute executeList TkEnd'''
    if len(p) == 7:
        p[0] = Instruction.Program(createSet = p[2],executeSet = p[4])
        global sintBotSymbolTable
        if sintBotSymbolTable.emptyTable():
            sintBotSymbolTable = sintBotSymbolTable.getUpperLevel()
    if len(p) == 4:
        p[0] = Instruction.Program(createSet = None,executeSet = p[2])

def p_finishBotList(p):
    # Regla vacia que permite ejecutar una instruccion apenas se terminen 
    # las declaraciones de bots
    "finishBotList :"
    global sintBotSymbolTable
    sintBotSymbolTable = SymbolTable(deepcopy(sintBotSymbolTable))

#----------------------->   EXPRESIONES  <------------------------'''

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
                  | expression TkDesigual expression
                  | TkNegacion expression
                  | TkCaracter                
                  | TkNum                    
                  | TkFalse
                  | TkTrue                        
                  | TkIdent'''
    if len(p) == 4:
        if ((p[2] == "+") or (p[2] == "-") or (p[2] == "*") or (p[2] == "/") or (p[2] == "%")):
            p[0] = Expression.ArithmethicExpression(p[1],p[2],p[3])
        elif ((p[2] == "/\\") or (p[2] == "\/")):
            p[0] = Expression.BooleanExpression(p[1],p[2],p[3])
        elif ((p[2] == "<") or (p[2] == "<=") or (p[2] == ">") or (p[2] == ">=") or (p[2] == "=") or
              (p[2] == "/=")):
            p[0] = Expression.RelationalExpresion(p[1],p[2],p[3])    
        elif ((p[1] == "(") and (p[3] == ")")):
            p[0] = Expression.ParentizedExpression(p[1],p[2],p[3])   
        
        global sintBotSymbolTable
        if (expressionAnalisis(sintBotSymbolTable,p[0],p.lexer.lineno -18,p.lexer.lexpos - p.lexer.current)):
            pass
        else:
            exit()                  
    elif len(p) == 3:             
        p[0] = Expression.BooleanExpression(expresion1= p[2], operador = p[1])
        global sintBotSymbolTable
        if (expressionAnalisis(sintBotSymbolTable,p[0],p.lexer.lineno -18,p.lexer.lexpos - p.lexer.current)):
            pass
        else:
            exit()        
    elif len(p) == 2:                    
        p[0] = p[1]   


#---------------------------> CREATE <----------------------------

def p_botCreateList(p):
    '''botCreateList :    botCreateList botCreate 
                     |    botCreate''' # Asi cortamos la lista'''
    
    if len(p) == 3:
        p[0] = p[1]
        p[0].append(p[2])
    elif len(p) == 2:
        p[0] = []
        p[0].append(p[1])
    
def p_botCreate(p):
    '''botCreate :       TkInt  TkBot TkIdent botDeclaracionList TkEnd
                 |       TkBool TkBot TkIdent botDeclaracionList TkEnd
                 |       TkChar TkBot TkIdent botDeclaracionList TkEnd'''
    p[0] = Instruction.CreateInstruction(p[1],p[3],p[4])
    symbol = Symbol(p[3],p[1],None)
    global sintBotSymbolTable
    sintBotSymbolTable = sintBotSymbolTable.addToTable(p[3],symbol)

def p_botDeclaracionList(p):
    '''botDeclaracionList :    botDeclaracionList botDeclaracion 
                          |    botDeclaracion'''
    if len(p) == 3:
        p[0] = p[1]
        p[0].append(p[2])
    elif len(p) == 2:
        p[0] = []
        p[0].append(p[1])
            
            
def p_botDeclaracion(p):
    '''botDeclaracion  :    TkOn TkActivation TkDosPuntos botInstruccionList TkEnd
                    |       TkOn TkDeactivation TkDosPuntos botInstruccionList TkEnd
                    |       TkOn expression TkDosPuntos botInstruccionList TkEnd
                    |       TkOn TkDefault TkDosPuntos botInstruccionList TkEnd'''
    p[0] = Instruction.BotDeclaration(p[2],p[4])     
    

def p_botInstruccionList(p):
    '''botInstruccionList  :    botInstruccionList botInstruccion  
                           |    botInstruccion''' # Asi cortamos la lista
    if len(p) == 3:
        p[0] = p[1]
        p[0].append(p[2])
    elif len(p) == 2:
        p[0] = []
        p[0].append(p[1])


def p_botInstruccion(p):
    '''botInstruccion :    TkStore expression TkPunto
                   |       TkDrop expression TkPunto    

                   |       TkCollect TkPunto
                   |       TkCollect TkAs TkIdent TkPunto                   

                   |       TkRecieve TkPunto
                   |       TkSend TkPunto     
                   |       TkRead TkPunto
                   |       TkRead TkAs TkIdent TkPunto
                   
                   |       TkLeft expression TkPunto
                   |       TkRight expression TkPunto
                   |       TkUp expression TkPunto
                   |       TkDown expression TkPunto

                   |       TkLeft TkPunto
                   |       TkRight TkPunto
                   |       TkUp TkPunto
                   |       TkDown TkPunto'''  # Asi cortamos la lista
    if len(p) == 5:
        p[0] = Instruction.BotInstruction(p[1],p[3])
        if p[3] != "me":
            symbol = Symbol(p[3],"int",None)
            global sintBotSymbolTable
            sintBotSymbolTable = sintBotSymbolTable.addToTable(p[3],symbol)
    elif len(p) == 4:
        p[0] = Instruction.BotInstruction(p[1],p[2])
    elif len(p) == 3:
        p[0] = Instruction.BotInstruction(p[1])


# -----------------------> INSTRUCCIONES <--------------------------

def p_execute(p):
    '''executeList :    executeList execCont 
                   |    execCont''' # Asi cortamos la lista'''

    if len(p) == 3:
        p[0] = p[1]
        p[0].append(p[2])
    elif len(p) == 2:
        p[0] = []
        p[0].append(p[1])


def p_identList(p):
    '''identList   :    identList TkComa TkIdent
                   |    identList TkPunto
                   |    TkIdent'''
    if len(p) == 4:
        p[0] = p[1]
        p[0].append(p[3])
        global sintBotSymbolTable
        if not sintBotSymbolTable.searchForSymbol(p[3]):
            print("Simbolo No Declarado --> " + p[3] + " ("
                  + str(p.lexer.lineno -18) + "," + str(p.lexer.lexpos - p.lexer.current) + ")")
    elif len(p) == 3:
        p[0] = p[1]
    elif len(p) == 2:
        p[0] = []
        p[0].append(p[1])    
        global sintBotSymbolTable
        if not sintBotSymbolTable.searchForSymbol(p[1]):
            print("Simbolo No Declarado --> " + p[1] + " ("
                  + str(p.lexer.lineno -18) + "," + str(p.lexer.lexpos - p.lexer.current) + ")")

def p_execCont(p):
    '''execCont    :    activate
                   |    deactivate
                   |    advance
                   |    conditional
                   |    while
                   |    program''' # Incorporacion de alcance
    p[0] = p[1]
        
def p_conditional(p):
    '''conditional  :    TkIf expression TkDosPuntos executeList TkElse executeList TkEnd
                    |    TkIf expression TkDosPuntos executeList TkEnd'''
    if len(p) == 8:
        p[0] = Instruction.ConditionalInstruction(p[2],p[4],p[6])
    elif len(p) == 6:
        p[0] = Instruction.ConditionalInstruction(p[2],p[4])


def p_while(p):
    '''while        :    TkWhile expression TkDosPuntos executeList TkEnd'''
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

precedence = (
    ('left','TkParAbre','TkParCierra'),
    ('left','TkMult','TkDiv','TkMod'),
    ('left','TkSuma','TkResta'),
    ('left','TkMenor','TkMenorIgual','TkMayor','TkMayorIgual','TkDesigual'),
    ('left','TkIgual'),
    ('left','TkNegacion'),
    ('left','TkConjuncion'),
    ('left','TkDisyuncion'),
)

# Build the parser
BotParser = yacc.yacc(start='program',debugfile="debug.txt")
