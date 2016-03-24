'''
Created on Feb 1, 2016

@author: francisco
'''

from abc import ABCMeta, abstractmethod
from re import compile
from re import match


binary_symbol = {
                    "+"      : "Suma",
                    "-"      : "Resta",
                    "*"      : "Multiplicación",
                    "/"      : "Division",
                    "%"      : "Modulo",
                    ">"      : "Mayor",
                    ">="     : "Mayor o Igual",
                    "<"      : "Menor",
                    "<="     : "Menor o Igual",
                    "="      : "Igual",
                    ","      : "Coma",
                    "."      : "Punto",
                    ":"      : "Dos Puntos",
                    "("      : "Abre Parentesis",
                    ")"      : "Cierra Parentesis",
                    "/\\"    : "Conjuncion",
                    "\/"     : "Disyuncion",
                    "~"      : "Negacion"
                }  

# Funcion para controlar el espaciado
def spacing(espacio):
        i = 0
        while (i < 4):
            espacio += " " 
            i += 1
        return espacio
    
    
# Funcion para imprmir las Operaciones Binarias    
def operacionBinariaString(expresion1,operador,expresion2):
    espacio ="    "
    retorno =""
    operador = binary_symbol[operador]
    retorno += (espacio + espacio + espacio + " - operacion: " +  "'"+operador+"'")
    retorno += "\n"
    retorno += espacio + espacio + espacio + " - operando izquierdo: " +  str(expresion1)
    retorno += "\n"
    retorno += espacio + espacio + espacio + " - operando derecho: " +  str(expresion2)
    retorno += "\n"
    return retorno


# Funcion para imprmir las Operaciones Unarias
def operacionUnariaString(expresion1,operador):
    espacio ="    "
    retorno =""
    operador = binary_symbol[operador]
    retorno += (espacio + espacio + espacio + espacio + " - operacion: " +  "'"+operador+"'")
    retorno += "\n"
    retorno += espacio + espacio + espacio + espacio + " - operando: " +  str(expresion1)
    retorno += "\n"
    return retorno

# Funcion para imprmir las Expresiones Con Parentesis
def expresionParentesisString(expresion):
    espacio ="    "
    retorno =""
    retorno += (espacio + espacio + espacio +  "- parentesis izquierdo: " +  "'('")
    retorno += "\n"
    retorno += espacio + espacio + espacio + "- expresion: " +  str(expresion)
    retorno += "\n"
    retorno += espacio + espacio + espacio + "- parentesis derecho: " +  "')'"
    return retorno
    
# Expresiones Aritmetica
class ArithmethicExpression:
    '''
    classdocs
    '''
    def __init__(self, expresion1,operador=None,expresion2=None):
        '''
        Constructor
        '''
        self.expresion1 = expresion1
        self.operador = operador
        self.expresion2 = expresion2
        
    def __str__(self):
        espacio ="    "
        retorno = ""
        retorno += "\n"
        retorno += "\n"
        retorno += espacio + espacio + "- guardia: ArithmethicExpression"
        retorno += "\n"
        if( self.expresion1 != "(" ):
            if ( (self.operador != None) and (self.expresion2 != None) ):
                retorno += operacionBinariaString(self.expresion1,self.operador,self.expresion2)
            elif ( (self.operador == None) and (self.expresion2 == None) ):
                retorno += espacio + espacio + espacio + espacio + " - variable: " + self.expresion1
        return retorno    

    # Evaluar Resultado de evaluacion
    def evaluar(self,symbolTable):
        expresionUno = None
        expresionDos = None
        
        symbol1 = symbolTable.searchForSymbol(self.expresion1)
        symbol2 = symbolTable.searchForSymbol(self.expresion2)
        numPattern = compile('([0-9]+)|(-[0-9]+)')
        
        if match(numPattern,self.expresion1):
            expresionUno = int(self.expresion1)
        elif symbol1 != None:
            expresionUno= symbol1.value
        else:
            expresionUno = self.expresion1.evaluar(symbolTable)
        
        if match(numPattern,self.expresion2):
            expresionDos = int(self.expresion2)
        elif symbol2 != None:
            expresionDos= symbol2.value
        else:
            expresionDos = self.expresion2.evaluar(symbolTable)     
        
        
        if (self.operador == "+"):
            return (expresionUno + expresionDos)
        elif (self.operador == "-"):
            return (expresionUno - expresionDos)
        elif (self.operador == "*"):
            return (expresionUno * expresionDos)
        elif  (self.operador == "/"):
            return (expresionUno / expresionDos)
        elif  (self.operador == "%"):
            return (expresionUno % expresionDos)

        
# Expresiones Relacionales
class RelationalExpresion:
    def __init__(self, expresion1,operador=None,expresion2=None):
        self.expresion1 = expresion1
        self.operador = operador
        self.expresion2 = expresion2
        #self.imprimir("")
        
    def __str__(self):
        espacio ="    "
        retorno = ""
        retorno += "\n"
        retorno += "\n"
        retorno += espacio + espacio + "- guardia: RelationalExpresion"
        retorno += "\n"
        if( self.expresion1 != "(" ):
            if ( (self.operador != None) and (self.expresion2 != None) ):
                retorno += operacionBinariaString(self.expresion1,self.operador,self.expresion2)
            elif ( (self.operador == None) and (self.expresion2 == None) ):
                retorno += espacio + espacio + espacio + espacio + " - variable: " + self.expresion1
        retorno += "\n"
        return retorno   
    
    # Evaluar Resultado de evaluacion
    def evaluar(self,symbolTable):
        
        numPattern = compile('([0-9]+)|(-[0-9]+)')
        
        expresionUno = None
        expresionDos = None
        
        symbol1 = symbolTable.searchForSymbol(self.expresion1)
        symbol2 = symbolTable.searchForSymbol(self.expresion2)

        if self.operador == '/=' or self.operador == '=':
            # Expresion 1
            if self.expresion1 == "true":
                expresionUno = True
            elif self.expresion1 == "false":
                expresionUno = False
            elif match(numPattern,self.expresion1):
                expresionUno = int(self.expresion1)
            elif symbol1 != None:
                expresionUno= symbol1.value
            else:
                expresionUno = self.expresion1.evaluar(symbolTable)
            
            # Expresion 2    
            if self.expresion2 == "true":
                expresionDos = True
            elif self.expresion2 == "false":
                expresionDos = False
            elif match(numPattern,self.expresion2):
                expresionDos = int(self.expresion2)
            elif symbol2 != None:
                expresionDos= symbol2.value
            else:
                expresionDos = self.expresion2.evaluar(symbolTable)                
                
        elif (self.operador == '>' or self.operador == '>=' or self.operador == '<' 
              or self.operador == '<='):
            
            # Expresion 1
            if match(numPattern,self.expresion1):
                expresionUno = int(self.expresion1)
            elif symbol1 != None:
                expresionUno= symbol1.value
            else:
                expresionUno = self.expresion1.evaluar(symbolTable)
            
            # Expresion 2    
            if match(numPattern,self.expresion2):
                expresionDos = int(self.expresion2)
            elif symbol2 != None:
                expresionDos= symbol2.value
            else:
                expresionDos = self.expresion2.evaluar(symbolTable)  

        # Efectuo la operacion
        if (self.operador == "/="):
            return (expresionUno != expresionDos)
        elif (self.operador == "="):
            return (expresionUno == expresionDos)
        elif (self.operador == ">"):
            return (expresionUno > expresionDos)
        elif (self.operador == ">="):
            return (expresionUno >= expresionDos)
        elif (self.operador == "<"):
            return (expresionUno < expresionDos)
        elif (self.operador == "<="):
            return (expresionUno <= expresionDos)




          
# Expresiones Booleanas
class BooleanExpression:
    def __init__(self,expresion1,operador=None,expresion2=None):
        self.expresion1 = expresion1
        self.operador = operador
        self.expresion2 = expresion2
        #self.imprimir("")
 
    def __str__(self):
        espacio ="    "
        retorno = ""
        retorno += "\n"
        retorno += "\n"
        retorno += espacio + espacio + "- guardia: BooleanExpression"
        retorno += "\n"
        if( self.expresion1 != "(" ):
            if ( (self.operador != None) and (self.expresion2 != None) ):
                retorno += operacionBinariaString(self.expresion1,self.operador,self.expresion2)
            elif ( (self.operador != None) and (self.expresion2 == None) ):
                retorno += operacionUnariaString(self.expresion1,self.operador)
            elif ( (self.operador == None) and (self.expresion2 == None) ):
                retorno += espacio + espacio + espacio + espacio + " - variable: " + self.expresion1
        retorno += "\n"
        return retorno
    
    # Evaluar Resultado de evaluacion
    def evaluar(self,symbolTable):
        expresionUno = None
        expresionDos = None
        
        symbol = symbolTable.searchForSymbol(expresionUno)
        
        if type(self.expresion1) is str:
            if self.expresion1 == "true":
                expresionUno = True
            elif self.expresion1 == "false":
                expresionUno = False
            elif symbol != None:
                expresionUno= symbol.value
        else:
            expresionUno = self.expresion1.evaluar(symbolTable)
        
        if type(self.expresion2) is str:
            if self.expresion2 == "true":
                expresionDos = True
            elif self.expresion2 == "false":
                expresionDos = False
            elif symbol != None:
                expresionDos= symbol.value
        else:
            expresionUno = self.expresion1.evaluar(symbolTable)  
        
        if (self.operador == "/\\"):
            return (expresionUno and expresionDos)
        elif (self.operador == "\/"):
            return (expresionUno or expresionDos)

# Expresiones con Parentizacion
class ParentizedExpression:
    def __init__(self,abre,expresion,cierra):
        self.cierra = cierra
        self.expresion = expresion
        self.cierra = cierra
        #self.imprimir("")
 
    def __str__(self):
        espacio = "    "
        retorno = ""
        retorno += "\n"
        retorno += "\n"
        retorno += espacio + espacio + "--- Open ParentizedExpression ---"
        retorno += "\n"
        retorno += expresionParentesisString(self.expresion)
        retorno += "\n"
        retorno += espacio + espacio + "--- Close ParentizedExpression ---"
        retorno += "\n"
        return retorno 
    
    # Evaluar Resultado de evaluacion
    def evaluar(self,symbolTable):
        return self.expresion.evaluar(symbolTable)
