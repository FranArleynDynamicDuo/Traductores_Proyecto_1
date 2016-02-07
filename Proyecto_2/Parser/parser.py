'''
Created on Feb 1, 2016

@author: francisco
'''

import ply.yacc as yacc;

# Get the token map from the lexer.  This is required.
from Proyecto_1.Lexer.Lexer import lexer;
from Proyecto_2.Parser import Expression
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

'''-----------------------> BLOQUE INICIAL <------------------------'''

def p_program(p):
    'program : bloque'
    p[0] = Expression.Program() # Modificado por Arleyn
    pass

def p_bloque(p):
    '''bloque : TkCreate create
              | TkExecute execute'''
    pass

'''---------------------------> CREATE <----------------------------'''
    
def p_create(p):
    '''create :    TkInt  TkBot TkIdent declaracion 
              |    TkBool TkBot TkIdent declaracion
              |    TkChar TkBot TkIdent declaracion'''
    pass

def p_declaracion(p):
    '''declaracion  :    TkOn TkActivation TkDosPuntos instruccion 
                    |    TkOn TkDeactivation TkDosPuntos instruccion
                    |    TkOn TkCustomCondition TkDosPuntos instruccion
                    |    TkOn TkDefault TkDosPuntos instruccion'''
    pass

def p_instruccion(p):
    '''instruccion :    TkStore TkNum TkPunto instruccion
                   |    TkStore TkCaracter TkPunto instruccion
                   |    TkCollect TkPunto                 // FALTA ALGO "as"
                   |    TkRecieve TkPunto instruccion
                   |    Tkdrop TkNum TkPunto instruccion
                   |    Tkdrop TkCaracter TkPunto instruccion
                   |    TkSend TkPunto instruccion     
                   |    TkRead TkPunto instruccion     // FALTA ALGO "as"
                   |    TkLeft TkPunto instruccion
                   |    TkRight TkPunto instruccion
                   |    TkUp TkPunto instruccion
                   |    TkDown TkPunto instruccion    
                   |    end'''
    pass

def p_end(p):
    '''end :     TkEnd end
           |     declaracion
           |     create
           |     bloque'''
    pass

''' -----------------------> INSTRUCCIONES <-------------------------- '''

def p_execute(p):
    '''execute :    TkActivate identList
               |    TkDeactivate identLits'''
    p[0] = Expression.Execute(p[1],p[2]) # Agregado por Arleyn
    pass   


def p_identList(p):
    '''identList   :    TkIdent TkPunto cont
                   |    TkIdent TkComa identList'''
    pass  

def p_cont(p):
    '''cont    :    TkAdvance identList cont
               |    TkDeactivate identList cont
               |    conditional cont
               |    while cont
               |    TkEnd'''
    pass

def p_conditional(p):
    '''conditional  :    TkIf boolExpr TkDosPuntos cont TkElse cont TkEnd
                    |    TkIf boolExpr TkDosPuntos cont TkEnd'''
    pass  

def p_while(p):
    '''while        :    TkWhile boolExpr TkDosPuntos cont TkEnd'''
    pass  


# Build the parser
parser = yacc.yacc()
