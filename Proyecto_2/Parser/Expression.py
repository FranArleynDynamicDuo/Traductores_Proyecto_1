'''
Created on Feb 1, 2016

@author: francisco
'''

from abc import ABCMeta, abstractmethod

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