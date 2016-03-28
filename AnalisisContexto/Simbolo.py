'''
Created on Mar 23, 2016

@author: francisco
'''

class Simbolo():
    def __init__(self,identifier,symbolType,value):
        self.identifier = identifier
        self.symbolType = symbolType
        self.value = value
        self.tablaDeComportamientos = []
        self.activado = False
        self.horPosicion = 0
        self.verPosicion = 0
    def __str__(self):
        retorno = self.symbolType + " " + self.identifier + " : "
        if self.value is None:
            retorno += "None"
        else:
            retorno += str(self.value) + " "
        retorno += " | "
        retorno += ("Active: " + str(self.activado) +
                   " | (" + str(self.horPosicion) + " : " + str(self.verPosicion) + ")")
        retorno += "\n"
        return retorno 
    def obtenerIdentificador(self):
        return self.identifier
    def obtenerTipo(self):
        return self.symbolType
    def obtenerValor(self):
        return self.value
    def setIdentifier(self,identifier):
        self.identifier = identifier
        return self
    def setType(self,symbolType):
        self.symbolType = symbolType
        return self
    def setValue(self,value):
        global sintBotSymbolTable
        valueType = type(value)
        if (self.obtenerTipo() == "char" and valueType is str):
            self.value = value
        elif (self.obtenerTipo() == "int" and valueType is int):
            self.value = value
        elif (self.obtenerTipo() == "bool" and valueType is bool):
            self.value = value
        elif (self.value is None and value is None):
            pass
        # ERROR Conflicto de tipos
        else:
            print("ERROR: Conflicto De Tipos al tratar de asignarle '" + str(value) + "' a '" + self.getIdentifier() + "' \n")
            exit()
        return self
    
    def crearSimboloDeValor(self,value):
        resultType = type(value)
        if resultType is bool:
            symbolType = "bool"
        elif resultType is int:
            symbolType = "int"
        elif resultType is str :
            symbolType = "char"
        simbolo = Simbolo(self.identifier,symbolType,value)
        return simbolo 