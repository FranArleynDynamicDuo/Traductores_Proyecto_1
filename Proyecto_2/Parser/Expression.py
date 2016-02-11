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

def operacionBinariaString(expresion1,operador,expresion2):
    espacio =""
    retorno =""
    operador = binary_symbol[operador]
    retorno += (espacio + espacio + espacio + espacio + " - operacion: " +  "'"+operador+"'")
    retorno += "\n"
    retorno += espacio + espacio + espacio + espacio + " - operando izquierdo: " +  expresion1
    retorno += "\n"
    retorno += espacio + espacio + espacio + espacio + " - operando derecho: " +  expresion2
    retorno += "\n"
    return retorno

def operacionUnariaString(expresion1,operador):
    espacio =""
    retorno =""
    operador = binary_symbol[operador]
    retorno += (espacio + espacio + espacio + espacio + " - operacion: " +  "'"+operador+"'")
    retorno += "\n"
    retorno += espacio + espacio + espacio + espacio + " - operando: " +  expresion1
    retorno += "\n"
    return retorno

def expresionParentesisString(expresion):
    espacio =""
    retorno =""
    retorno += (espacio + espacio + espacio + espacio + " - operacion: " +  "'('")
    retorno += "\n"
    retorno += espacio + espacio + espacio + espacio + " - expresion: " +  expresion
    retorno += "\n"
    retorno += espacio + espacio + espacio + espacio + " - operando derecho: " +  "')'"
    retorno += "\n"
    return retorno

def spacing(espacio):
        i = 0
        while (i < 4):
            espacio += " " 
            i += 1
        return espacio
    
class Expresion(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self, params):
        pass


        
# Se Especifica el Bloque        
class ProgramExpression:
    
    def __init__(self,bloque):
        self.bloque = bloque
        #self.imprimir("")
        
    def imprimir(self,espacio):
        print("--------(Bloque)-------")
        print(espacio,"SECUENCIACION") #PREGUNTAR SI COLOCAR "EJECUTAR"


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
        #self.imprimir("")
        
    def __str__(self):
        espacio = ""
        retorno = ""
        retorno += "--------(ArithmethicExpression)-------"
        retorno += "\n"
        retorno += espacio + espacio + espacio + espacio + "- guardia: ArithmethicExpression"
        retorno += "\n"
        if( self.expresion1 != "(" ):
            if ( (self.operador != None) and (self.expresion2 != None) ):
                operador = binary_symbol[self.operador]
                retorno += operacionBinariaString(self.expresion1,operador,self.expresion2)
            elif ( (self.operador == None) and (self.expresion2 == None) ):
                retorno += espacio + espacio + espacio + espacio + " - variable: " + self.expresion1
                retorno += "\n"
        elif( self.expresion1 == "(" ):
            retorno += expresionParentesisString(self.expresion1)
        return retorno    
        
# Expresiones Relacionales
class RelationalExpresion:
    def __init__(self, expresion1,operador=None,expresion2=None):
        self.expresion1 = expresion1
        self.operador = operador
        self.expresion2 = expresion2
        #self.imprimir("")
        
    def __str__(self):
        espacio = ""
        retorno = ""
        retorno += "--------(RelationalExpresion)-------"
        retorno += "\n"
        retorno += espacio + espacio + espacio + espacio + "- guardia: RelationalExpresion"
        retorno += "\n"
        if( self.expresion1 != "(" ):
            if ( (self.operador != None) and (self.expresion2 != None) ):
                operador = binary_symbol[self.operador]
                retorno += operacionBinariaString(self.expresion1,operador,self.expresion2)
            elif ( (self.operador == None) and (self.expresion2 == None) ):
                retorno += espacio + espacio + espacio + espacio + " - variable: " + self.expresion1
                retorno += "\n"
                 
        elif( self.expresion1 == "(" ):
            retorno += expresionParentesisString(self.expresion1)
        return retorno   
          
# Expresiones Booleanas
class BooleanExpression:
    def __init__(self,expresion1,operador=None,expresion2=None):
        self.expresion1 = expresion1
        self.operador = operador
        self.expresion2 = expresion2
        #self.imprimir("")
 
    def __str__(self):
        espacio = ""
        retorno = ""
        retorno += "--------(BooleanExpression)-------"
        retorno += "\n"
        retorno += espacio + espacio + espacio + espacio + "- guardia: BooleanExpression"
        retorno += "\n"
        if( self.expresion1 != "(" ):
            if ( (self.operador != None) and (self.expresion2 != None) ):
                operador = binary_symbol[self.operador]
                retorno += operacionBinariaString(self.expresion1,operador,self.expresion2)
            elif ( (self.operador != None) and (self.expresion2 == None) ):
                operador = binary_symbol[self.operador]
                retorno += operacionUnariaString(self.expresion1,operador)
            elif ( (self.operador == None) and (self.expresion2 == None) ):
                retorno += espacio + espacio + espacio + espacio + " - variable: " + self.expresion1
                retorno += "\n"
                 
        elif( self.expresion1 == "(" ):
            retorno += expresionParentesisString(self.expresion1)
        return retorno 

