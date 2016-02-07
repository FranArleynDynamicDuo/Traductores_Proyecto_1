'''
Created on Feb 1, 2016

@author: francisco
'''
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
                    "/"      : "Conjuncion",
                    "\/"     : "Disyuncion",
                    "~"      : "Negacion"
                }  

def spacing(espacio):
        i = 0
        while (i < 4):
            espacio += " " 
            i += 1
        return espacio
    
class Expresion(metaclass=ABCMeta):
    '''
    classdocs
    '''

# Inicio del Programa
class Program:
    
    def __init__(self,bloque = None):
        self.bloque = bloque
        
        # Imprime el programa
        self.imprimir("")
        
    def imprimir(self,espacio):
        print(espacio,"SECUENCIACION")
        
        
        
# Class Execute
class Execute:
    
    def __init__(self,action,identList):
        self.action = action
        self.identList = identList
        
        # Imprime el programa
        self.imprimir("")
        
    def imprimir(self,espacio):
        if (self.action == "activate"):
            print(espacio,espacio,"ACTIVACION")
            print(espacio,espacio,espacio," - var: ", self.identList)
        elif (self.action == "deactivate"):
            print(espacio,espacio,"DESACTIVACION")
            print(espacio,espacio,espacio," - var: ", self.identList)
    
# Expresiones Aritmetica
class ArithmethicExpression:
    '''
    classdocs
    '''

    @abstractmethod
    def __init__(self, expresion1,operador=None,expresion2=None):
        '''
        Constructor
        '''
        self.expresion1 = expresion1
        self.operador = operador
        self.expresion2 = expresion2
        self.imprimir("")
        
    def imprimir(self,espacio):
        print(espacio,"CONDICIONAL")
        print(espacio,espacio,"- guardia: ArithmethicExpression")
        
        if (self.operador != None):
            operador = binary_symbol[self.operador]
            print(espacio,espacio,espacio," - operacion: ", "'"+operador+"'")
            print(espacio,espacio,espacio," - operador izquierdo: ", self.expresion1)
            print(espacio,espacio,espacio," - operador derecho: ", self.expresion2)
        elif (self.operador == None):
            print(espacio,espacio,espacio," - operador izquierdo: ", self.expresion1)
        
# Expresiones Relacionales
class RelationalExpresion:
    '''
    classdocs
    '''
    @abstractmethod
    def __init__(self, expresion1,operador=None,expresion2=None):
        '''
        Constructor
        '''
        self.expresion1 = expresion1
        self.operador = operador
        self.expresion2 = expresion2
        self.imprimir("")
        
    def imprimir(self,espacio):
        print(espacio,"CONDICIONAL")
        print(espacio,espacio,"- guardia: RelationalExpresion")
        
        if (self.operador != None):
            operador = binary_symbol[self.operador]
            print(espacio,espacio,espacio," - operacion: ", "'"+operador+"'")
            print(espacio,espacio,espacio," - operador izquierdo: ", self.expresion1)
            print(espacio,espacio,espacio," - operador derecho: ", self.expresion2)
        elif (self.operador == None):
            print(espacio,espacio,espacio," - variable: ", self.expresion)
        
# Expresiones Booleanas
class BooleanExpression:
    '''
    classdocs
    '''
    def __init__(self,expresion1,operador=None,expresion2=None):
        '''
        Constructor
        '''
        self.expresion1 = expresion1
        self.operador = operador
        self.expresion2 = expresion2
        self.imprimir("")
        
    def imprimir(self,espacio):
        print(espacio,"CONDICIONAL")
        print(espacio,espacio,"- guardia: BooleanExpression")
        
        if ( (self.operador != None) and (self.expresion2 != None) ):
            operador = binary_symbol[self.operador]
            print(espacio,espacio,espacio," - operacion: ", "'"+operador+"'")
            print(espacio,espacio,espacio," - operador izquierdo: ", self.expresion1)
            print(espacio,espacio,espacio," - operador derecho: ", self.expresion2)
        elif ( (self.operador != None) and (self.expresion2 == None) ):
            operador = binary_symbol[self.expresion1]
            print(espacio,espacio,espacio," - operador: ", "'"+operador+"'")
            print(espacio,espacio,espacio," - variable: ", self.operador)
        elif ( (self.operador == None) and (self.expresion2 == None) ):
            print(espacio,espacio,espacio," - variable: ", self.expresion1)

from abc import ABCMeta, abstractmethod
    
class Expresion(metaclass=ABCMeta):
    '''
    classdocs
    '''

class ArithmethicExpression(Expresion):
    '''
    classdocs
    '''

    @abstractmethod
    def __init__(self, expresion1,operador=None,expresion2=None):
        '''
        Constructor
        '''
        self.expresion1 = expresion1
        self.expresion1 = operador
        self.expresion2 = expresion2
        
class RelationalExpresion(Expresion):
    '''
    classdocs
    '''

    @abstractmethod
    def __init__(self, expresion1,operador=None,expresion2=None):
        '''
        Constructor
        '''
        self.expresion1 = expresion1
        self.expresion1 = operador
        self.expresion2 = expresion2
        
class BooleanExpression(Expresion):
    '''
    classdocs
    '''

    @abstractmethod
    def __init__(self, expresion1,operador=None,expresion2=None):
        '''
        Constructor
        '''
        self.expresion1 = expresion1
        self.expresion1 = operador
        self.expresion2 = expresion2
