'''
Created on Feb 1, 2016

@author: francisco
'''
from Proyecto_2.Parser.Expression import ArithmethicExpression
from Proyecto_2.Parser.Expression import RelationalExpresion
from Proyecto_2.Parser.Expression import BooleanExpression
from Proyecto_2.Parser.Expression import ParentizedExpression

import re

# Clase de tabla de simbolos
class SymbolTable():
    
    def __init__(self,upperLevel ):
        self.table = dict()
        self.upperLevel = upperLevel
        
    def __str__(self):
        retorno = ""
        if self.upperLevel is None:
            retorno += "Tabla De Simbolos\n"
            retorno += "    Nivel Superior\n"
            for key in self.table:
                retorno += "        " + key + " ==> " + str(self.getElement(key))
            retorno += "\n"
            return retorno
        
        else:
            retorno += str(self.upperLevel)
            retorno += "    Siguiente Nivel\n"
            if (self.emptyTable()):
                retorno += "        Nivel Vacio!\n"
            else:
                for key in self.table:
                    retorno += "        " + key + " ==> " + str(self.getElement(key))
            retorno += "\n"
            return retorno
    
    ''' Funciones simples de primer nivel '''
    
    def addToTable(self,key,element):
        self.table.update({key: element})
        return self
    
    def emptyTable(self):
        if (self.table):
            return False
        else:
            return True
    
    def getElement(self,key):
        return self.table.get(key)
    
    def getUpperLevel(self):
        return self.upperLevel

    def getTable(self):
        return self.table
    
    ''' Funciones Complejas Recursivas '''
    
    def searchForSymbol(self,identifier):
        """
        Busca un elemento en los distintos niveles de la tabla de simbolos y 
        retorna su valor
        
        Si el valor no se encuentra, retorna None
        
        @type  identifier: String
        @param identifier: Nombre del simbolo a buscar
        @rtype:   Object
        @return:  El valor del simbolo encontrado
        """
   
        # Buscamos el simbolo
        elementValue = self.getElement(identifier)
        # Caso 1: Se encuentra, se devuelve el valor del simbolo
        if (elementValue is not None):
            return elementValue
        # Caso 2: No se encuentra, se busca en la tabla de nivel superior
        else:
            # Caso 2.1: Estamos en el ultima nivel, el elemento no existe en la tabla
            # asi que retornamos None
            if self.getTableFather() is None:
                return None;
            # Caso 2.2: No estamos en el ultimo nivel, buscamos en el nivel superior
            else:
                return self.getUpperLevel().searchForSymbol(identifier) 

class Symbol():
    
    def __init__(self,identifier,symbolType,value):
        self.identifier = identifier
        self.symbolType = symbolType
        self.value = value

    def __str__(self):
        if self.value is None:
            self.value = "None"
        retorno = self.symbolType + " " + self.identifier + " : " + self.value
        retorno += "\n"
        return retorno 
    
    def getIdentifier(self):
        return self.identifier
    
    def getType(self):
        return self.symbolType
    
    def getValue(self):
        return self.value
    
    def setIdentifier(self,identifier):
        self.identifier = identifier
        return self
 
    def setType(self,symbolType):
        self.symbolType = symbolType
        return self
    
    def setValue(self,value):
        self.value = value
        return self


# Metodo que lee el arbol de parseo y obtiene las variables declaradas y las coloca en un diccionario
def executeAnalisis(parseTree):

    pass

# Metodo que lee el arbol de parseo y obtiene las variables declaradas y las coloca en un diccionario
def expressionAnalisis(variableTable,expression):

        # Creamos la tabla vacia
        valid = False
        expressionType = type(expression)
        
        if expressionType is ArithmethicExpression:
            numPattern = re.compile('([0-9]+)|(-[0-9]+)')
        elif expressionType is RelationalExpresion:
            numPattern = re.compile('([0-9]+)|(-[0-9]+)')
        elif expressionType is BooleanExpression:
            boolPattern = re.compile('(true)|(false)')
        elif expressionType is ParentizedExpression:
            pass
        else:
            pass
        
#         pattern = re.compile("^([A-Z][0-9]+)*$")
#         pattern.match(string)
        
        return valid  

        