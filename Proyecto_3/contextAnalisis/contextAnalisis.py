'''
Created on Feb 1, 2016

@author: francisco
'''
from Proyecto_2.Parser.Expression import ArithmethicExpression
from Proyecto_2.Parser.Expression import RelationalExpresion
from Proyecto_2.Parser.Expression import BooleanExpression
from Proyecto_2.Parser.Expression import ParentizedExpression

from re import compile
from re import match

'''--------------------------------- CONSTANTES --------------------------------'''

''' Patrones de comparacion '''

boolPattern = compile('true|false')
numPattern = compile('([0-9]+)|(-[0-9]+)')
idenPattern = compile(r'[a-zA-Z][a-zA-Z0-9_]*')

''' Tipos de Simbolos '''

intTipo = "int"
boolTipo = "bool"
charTipo = "char"
tokenMe = "me"

''' Mensajes De Error '''

notInt = " no es tipo 'int'"
notIntChar = " no es tipo 'int' ni 'char'"
notIntBool = "no es tipo 'int' ni 'bool'"

''' Informacion Linea/Columna '''

lineInfo = " (L:"
columnInfo = ",C:"
closeInfo = ")"

''' Mensajes De Error '''

errorMe = "Uso de la palabra reservada 'me' fuera de un comportamiento "
errorConflictoTipos = "Conflicto De Tipos --> "
errorSimNoDeclarado = "Simbolo No Declarado --> "
errorDesconocido = "Error desconocido"


class SymbolTable():
    def __init__(self, upperLevel):
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
        retorna el simbolo
        
        Si el valor no se encuentra, retorna None
        
        @type  identifier: String
        @param identifier: Nombre del simbolo a buscar
        @rtype:   Object
        @return:  El valor del simbolo encontrado
        """
   
        # Buscamos el simbolo
        element = self.getElement(identifier)
        # Caso 1: Se encuentra, se devuelve el valor del simbolo
        if (element is not None):
            return element
        # Caso 2: No se encuentra, se busca en la tabla de nivel superior
        else:
            # Caso 2.1: Estamos en el ultima nivel, el elemento no existe en la tabla
            # asi que retornamos None
            if self.getUpperLevel() is None:
                return None;
            # Caso 2.2: No estamos en el ultimo nivel, buscamos en el nivel superior
            else:
                return self.getUpperLevel().searchForSymbol(identifier)
            
    def updateSymbol(self,identifier,value):
        """
        Busca un elemento en los distintos niveles de la tabla de simbolos y 
        retorna el simbolo
        
        Si el valor no se encuentra, retorna None
        
        @type  identifier: String
        @param identifier: Nombre del simbolo a buscar
        @rtype:   Object
        @return:  El valor del simbolo encontrado
        """
   
        # Buscamos el simbolo
        element = self.getElement(identifier)
        # Caso 1: Se encuentra, se devuelve el valor del simbolo
        if (element is not None):
            element.value = value
            self.table.update({identifier: element})
            return True
        # Caso 2: No se encuentra, se busca en la tabla de nivel superior
        else:
            # Caso 2.1: Estamos en el ultima nivel, el elemento no existe en la tabla
            # asi que retornamos None
            if self.getUpperLevel() is None:
                return False;
            # Caso 2.2: No estamos en el ultimo nivel, buscamos en el nivel superior
            else:
                return self.getUpperLevel().updateSymbol(identifier,value)


class Symbol():
    
    def __init__(self,identifier,symbolType,value):
        self.identifier = identifier
        self.symbolType = symbolType
        self.value = value
        self.behaviorTable = []

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
def validateArit(variableTable,expression,line,column):
    """
    Busca errores estaticos en una expresion aritmetica
    
    @type  variableTable: SymbolTable
    @param variableTable: Tabla de simbolos actual
    @type  expression: ArithmethicExpression
    @param expression: expresion a analizar
    @type  line: int
    @param line: numero de linea de la expresion
    @type  column: int
    @param column: numero de columna de la expresion
    @rtype:   booleano
    @return:  Indicacion si hubo error o no
    """
    
    if type(expression) is ParentizedExpression:
        
        return expressionAnalisis(variableTable,expression.expresion)    
    
    # Verificamos la primera expresion
    if (type(expression) is ArithmethicExpression):
        valid = True
    elif match(numPattern,expression):
        valid = True
    elif expression == tokenMe:
        print(errorMe + expression + lineInfo
              + str(line) + columnInfo + str(column) + closeInfo)
        return False
    elif variableTable.searchForSymbol(expression):
        symbol = variableTable.searchForSymbol(expression)
        if symbol.symbolType == intTipo:
            valid = True
        elif symbol.symbolType == charTipo or symbol.symbolType == boolTipo:
            print(errorConflictoTipos + expression + notInt + lineInfo
                  + str(line) + columnInfo + str(column) + closeInfo)
            return False                
    elif not variableTable.searchForSymbol(expression):
            print(errorSimNoDeclarado + expression + lineInfo
                  + str(line) + columnInfo + str(column) + closeInfo)
            return False
    else:
        print(errorDesconocido)
        return False
    return valid

# Metodo que lee el arbol de parseo y obtiene las variables declaradas y las coloca en un diccionario
def validateBool(variableTable,expression,line,column):
    """
    Busca errores estaticos en una expresion Booleana
    
    @type  variableTable: SymbolTable
    @param variableTable: Tabla de simbolos actual
    @type  expression: BooleanExpression
    @param expression: expresion a analizar
    @type  line: int
    @param line: numero de linea de la expresion
    @type  column: int
    @param column: numero de columna de la expresion
    @rtype:   booleano
    @return:  Indicacion si hubo error o no
    """
    
    # Caso 3.1: Es una expresion Booleana
    if (type(expression) is BooleanExpression):
        valid = True
    # Caso 3.2: Es una expresion Booleana
    elif (type(expression) is RelationalExpresion):
        valid = True
    # Caso 3.3: Es una literal booleano (true o false)
    elif match(boolPattern,expression):
        valid = True
    elif expression == tokenMe:
        print(errorMe + expression + lineInfo
              + str(line) + columnInfo + str(column) + closeInfo)
        return False
    # Caso 3.4: Es un identificador
    elif variableTable.searchForSymbol(expression):
        symbol = variableTable.searchForSymbol(expression)
        if symbol.symbolType == boolTipo:
            valid = True
        elif symbol.symbolType == charTipo or symbol.symbolType == intTipo:
            print(errorConflictoTipos + expression + notIntChar + lineInfo
                  + str(line) + columnInfo + str(column) + closeInfo)
            return False    
    elif not variableTable.searchForSymbol(expression):
            print(errorSimNoDeclarado + expression + lineInfo
                  + str(line) + columnInfo + str(column) + closeInfo)
    else:
        print(errorDesconocido)
        return False
    return valid

# Metodo que lee el arbol de parseo y obtiene las variables declaradas y las coloca en un diccionario
def validateRel(variableTable,expression,line,column):
    """
    Busca errores estaticos en una expresion Relacional
    
    @type  variableTable: SymbolTable
    @param variableTable: Tabla de simbolos actual
    @type  expression: RelationalExpresion
    @param expression: expresion a analizar
    @type  line: int
    @param line: numero de linea de la expresion
    @type  column: int
    @param column: numero de columna de la expresion
    @rtype:   booleano
    @return:  Indicacion si hubo error o no
    """
    
    if type(expression) is ParentizedExpression:
        
        return expressionAnalisis(variableTable,expression.expresion,line,column)
    
    if expression.operador == "=" or expression.operador == "/=":
        # Caso 3.1: Es una expresion Aritmetica
        if (type(expression) is ArithmethicExpression):
            valid = True        
        # Caso 3.2: Es una expresion Booleana
        elif (type(expression) is BooleanExpression):
            valid = True
        # Caso 3.3: Es una expresion Relacional
        elif (type(expression) is RelationalExpresion):
            valid = True
        # Caso 3.4: Es una literal aritmetico (numeros)
        elif match(numPattern,expression):
            valid = True
        # Caso 3.5: Es una literal booleano (true o false)
        elif match(boolPattern,expression):
            valid = True
        elif expression == tokenMe:
            print(errorMe + expression + lineInfo
                  + str(line) + columnInfo + str(column) + closeInfo)
            return False
        # Caso 3.6: Es un identificador
        elif variableTable.searchForSymbol(expression):
            symbol = variableTable.searchForSymbol(expression)
            if symbol.symbolType == boolTipo or symbol.symbolType == intTipo:
                valid = True
            elif symbol.symbolType == charTipo:
                print(errorConflictoTipos + expression + notIntBool + lineInfo
                  + str(line) + columnInfo + str(column) + closeInfo)
                return False
        elif not variableTable.searchForSymbol(expression):
            print(errorSimNoDeclarado + expression + lineInfo
                  + str(line) + columnInfo + str(column) + closeInfo)
        else:
            print(errorDesconocido)
            return False
            
    elif (expression.operador == "<" or expression.operador == "<=" or 
        expression.operador == ">" or expression.operador == ">="):
        
        # Caso 3.1: Es una expresion Aritmetica
        if (type(expression.expresion1) is ArithmethicExpression):
            valid = True
        # Caso 3.4: Es una literal aritmetico (numeros)
        elif match(numPattern,expression):
            valid = True
        elif expression == tokenMe:
            print(errorMe 
                  + expression + lineInfo
                  + str(line) + columnInfo + str(column) + closeInfo)
            return False
        # Caso 3.6: Es un identificador
        elif variableTable.searchForSymbol(expression):
            symbol = variableTable.searchForSymbol(expression)
            if symbol.symbolType == intTipo:
                valid = True
            elif symbol.symbolType == charTipo or symbol.symbolType == boolTipo:
                print(errorConflictoTipos + expression + notInt + lineInfo
                  + str(line) + columnInfo + str(column) + closeInfo)
                return False
        elif not variableTable.searchForSymbol(expression):
            print(errorSimNoDeclarado + expression + lineInfo
                  + str(line) + columnInfo + str(column) + closeInfo)
        else:
            print(errorDesconocido)
            return False
    
    return valid

# Metodo que lee el arbol de parseo y obtiene las variables declaradas y las coloca en un diccionario
def expressionAnalisis(variableTable,expression,line,column):
    """
    Orquesta la busqueda de errores en una expresion
    
    @type  variableTable: SymbolTable
    @param variableTable: Tabla de simbolos actual
    @type  expression: Expression
    @param expression: expresion a analizar
    @type  line: int
    @param line: numero de linea de la expresion
    @type  column: int
    @param column: numero de columna de la expresion
    @rtype:   booleano
    @return:  Indicacion si hubo error o no
    """
    # Creamos la tabla vacia
    expressionType = type(expression)

    # Caso 1: Expresion Aritmetica
    if expressionType is ArithmethicExpression:
        
        # Verificamos la primera expresion
        valid1 = validateArit(variableTable,expression.expresion1,line,column)
        
        if (valid1):
        
            # Verificamos la Segunda expresion
            valid2 = validateArit(variableTable,expression.expresion2,line,column)
        
        else:
            return False    
    
    # Caso 2: Expresion Relacional    
    elif expressionType is RelationalExpresion:
        
        # Verificamos la primera expresion
        valid1 = validateRel(variableTable,expression.expresion1,line,column)
        
        # Si la primera expresion es valida podemos continuar
        if (valid1):            
            
            # Verificamos la Segunda expresion
            valid2 = validateRel(variableTable,expression.expresion2,line,column)  
            
            expreType1 = type(expression.expresion1)
            expreType2 = type(expression.expresion2)
            symbol1 = variableTable.searchForSymbol(expression.expresion1)
            symbol2 = variableTable.searchForSymbol(expression.expresion2)
            
            # La expresion relacional cuando usa los operadores de igualdad y desigualdad,
            # tiene muchas combinaciones de tipos, asi que descartamos la expresion si
            # es una expresion invalida
            if valid2 and (expression.operador == "=" or expression.operador == "/="):
                
                # Una expresion aritmetica no puede ser igualada a otro tipo de expresion
                if ((expreType1 is ArithmethicExpression or expreType2 is ArithmethicExpression)
                      and (expreType1 is not ArithmethicExpression or 
                      expreType2 is not ArithmethicExpression)):
                    print()
                    return False
                
                # Una expresion aritmetica solo puede ser igualada a una variable si esta es
                # de tipo entero
                elif ((expreType1 is ArithmethicExpression and symbol2.getType() != intTipo)
                    or
                    (expreType1 is BooleanExpression and symbol2.getType() == intTipo)
                    or
                    (expreType1 is RelationalExpresion and symbol2.getType() == intTipo)):
                    print()
                    return False
                
                # Una expresion aritmetica solo puede ser igualada a una variable si esta es
                # de tipo entero 
                elif ((expreType2 is ArithmethicExpression and symbol1.getType() != intTipo)
                    or
                    (expreType2 is BooleanExpression and symbol1.getType() == intTipo)
                    or
                    (expreType2 is RelationalExpresion and symbol1.getType() == intTipo)):
                    print()
                    return False
            
        # Si la primera expresion es invalida, ya la expresion entera es invalida     
        else:
            return False   

    # Caso 3: Expresion Booleana
    elif expressionType is BooleanExpression:
        
        # Verificamos la primera expresion
        valid1 = validateBool(variableTable,expression.expresion1,line,column)

        if (valid1):
       
            # Verificamos la Segunda expresion
            valid2 = validateBool(variableTable,expression.expresion2,line,column)  

        else:
            return False   

    elif expressionType is ParentizedExpression:
        
        return expressionAnalisis(variableTable,expression.expresion,line,column)
   
    return valid1 and valid2 

        