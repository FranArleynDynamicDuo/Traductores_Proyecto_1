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
        
#     def imprimir(self,espacio):
#         print("--------(ArithmethicExpression)-------")
#         print(espacio,espacio,espacio,espacio,"- guardia: ArithmethicExpression")
#         
#         if( self.expresion1 != "(" ):
#             if (self.operador != None):
#                 operador = binary_symbol[self.operador]
#                 print(espacio,espacio,espacio,espacio," - operacion: ", "'"+operador+"'")
#                 print(espacio,espacio,espacio,espacio," - operador izquierdo: ", self.expresion1)
#                 print(espacio,espacio,espacio,espacio," - operador derecho: ", self.expresion2)
#             elif (self.operador == None):
#                 print(espacio,espacio,espacio,espacio," - operador izquierdo: ", self.expresion1)
#         
#         elif( self.expresion1 == "(" ):
#             operador = binary_symbol[self.expresion1]
#             print(espacio,espacio,espacio,espacio," - operador: ", "'"+operador+"'")
#             print(espacio,espacio,espacio,espacio," - operador central: ", self.expresion1)
#             operador = binary_symbol[self.expresion2]
#             print(espacio,espacio,espacio,espacio," - operador: ", "'"+operador+"'")
#             
        
# Expresiones Relacionales
class RelationalExpresion:
    def __init__(self, expresion1,operador=None,expresion2=None):
        self.expresion1 = expresion1
        self.operador = operador
        self.expresion2 = expresion2
        #self.imprimir("")
        
#     def imprimir(self,espacio):
#         print("--------(RelationalExpresion)-------")
#         print(espacio,espacio,espacio,espacio,"- guardia: RelationalExpresion")
#         
#         if( self.expresion1 != "(" ):
#             if (self.operador != None):
#                 operador = binary_symbol[self.operador]
#                 print(espacio,espacio,espacio,espacio," - operacion: ", "'"+operador+"'")
#                 print(espacio,espacio,espacio,espacio," - operador izquierdo: ", self.expresion1)
#                 print(espacio,espacio,espacio,espacio," - operador derecho: ", self.expresion2)
#             elif (self.operador == None):
#                 print(espacio,espacio,espacio,espacio," - variable: ", self.expresion1)
#                 
#         elif( self.expresion1 == "(" ):
#             operador = binary_symbol[self.expresion1]
#             print(espacio,espacio,espacio,espacio," - operador: ", "'"+operador+"'")
#             print(espacio,espacio,espacio,espacio," - operador central: ", self.operador)
#             operador = binary_symbol[self.expresion2]
#             print(espacio,espacio,espacio,espacio," - operador: ", "'"+operador+"'")
#             
        
# Expresiones Booleanas
class BooleanExpression:
    def __init__(self,expresion1,operador=None,expresion2=None):
        self.expresion1 = expresion1
        self.operador = operador
        self.expresion2 = expresion2
        #self.imprimir("")
        
#     def imprimir(self,espacio):
#         print("--------(BooleanExpression)-------")
#         print(espacio,espacio,espacio,espacio,"- guardia: BooleanExpression")
#         
#         if( self.expresion1 != "(" ):
#             if ( (self.operador != None) and (self.expresion2 != None) ):
#                 operador = binary_symbol[self.operador]
#                 print(espacio,espacio,espacio,espacio," - operacion: ", "'"+operador+"'")
#                 print(espacio,espacio,espacio,espacio," - operador izquierdo: ", self.expresion1)
#                 print(espacio,espacio,espacio,espacio," - operador derecho: ", self.expresion2)
#             elif ( (self.operador != None) and (self.expresion2 == None) ):
#                 operador = binary_symbol[self.expresion1]
#                 print(espacio,espacio,espacio,espacio," - operador: ", "'"+operador+"'")
#                 print(espacio,espacio,espacio,espacio," - variable: ", self.operador)
#             elif ( (self.operador == None) and (self.expresion2 == None) ):
#                 print(espacio,espacio,espacio,espacio," - variable: ", self.expresion1)
#                 
#         elif( self.expresion1 == "(" ):
#             operador = binary_symbol[self.expresion1]
#             print(espacio,espacio,espacio,espacio," - operador: ", "'"+operador+"'")
#             print(espacio,espacio,espacio,espacio," - operador central: ", self.operador)
#             operador = binary_symbol[self.expresion2]
#             print(espacio,espacio,espacio,espacio," - operador: ", "'"+operador+"'")
