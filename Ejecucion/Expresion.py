'''
Created on Feb 1, 2016

@author: francisco
'''

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

def operacionBinariaString(expresion1,operador,expresion2):
    """
    Funcion para imprmir las Operaciones Binarias
    
    @type  expresion1: Expresion
    @param expresion1: expresion a imprimir
    @type  operador: Str
    @param operador: operador de la operacion en la expresion
    @type  expresion2: Expresion
    @param expresion2: expresion a imprimir
    """
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

def operacionUnariaString(expresion,operador):
    """
    Funcion para imprmir las Operaciones Unarias
    
    @type  expresion: Expresion
    @param expresion: expresion a imprimir
    @type  operador: Str
    @param operador: operador de la operacion en la expresion
    """
    espacio ="    "
    retorno =""
    operador = binary_symbol[operador]
    retorno += (espacio + espacio + espacio + espacio + " - operacion: " +  "'"+operador+"'")
    retorno += "\n"
    retorno += espacio + espacio + espacio + espacio + " - operando: " +  str(expresion)
    retorno += "\n"
    return retorno

def expresionParentesisString(expresion):
    """
    Funcion para imprmir las Operaciones parentizadas
    
    @type  expresion: Expresion
    @param expresion: expresion a imprimir
    """
    espacio ="    "
    retorno =""
    retorno += (espacio + espacio + espacio +  "- parentesis izquierdo: " +  "'('")
    retorno += "\n"
    retorno += espacio + espacio + espacio + "- expresion: " +  str(expresion)
    retorno += "\n"
    retorno += espacio + espacio + espacio + "- parentesis derecho: " +  "')'"
    return retorno
    
# Expresiones Aritmetica
class ExpresionAritmetica:
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
        retorno += espacio + espacio + "- guardia: ExpresionAritmetica"
        retorno += "\n"
        if( self.expresion1 != "(" ):
            if ( (self.operador != None) and (self.expresion2 != None) ):
                retorno += operacionBinariaString(self.expresion1,self.operador,self.expresion2)
            elif ( (self.operador == None) and (self.expresion2 == None) ):
                retorno += espacio + espacio + espacio + espacio + " - variable: " + self.expresion1
        return retorno    
    # Evaluar Resultado de evaluacion
    def evaluar(self,symbolTable):
        """
        Evalua la expresion y retorna el resultado
        
        @type  symbolTable: SymbolTable
        @param symbolTable: Tabla de simbolos actual
        @rtype:   int
        @return:  Resultado de la expresion
        """
        # Inicializamos las variables
        expresionUno = None
        expresionDos = None
        # Verificamos si las expresiones son simbolos
        symbol1 = symbolTable.searchForSymbol(self.expresion1)
        symbol2 = symbolTable.searchForSymbol(self.expresion2)
        # Patron para la comparacion de numeros
        numPattern = compile('([0-9]+)|(-[0-9]+)')
        # Primera expresion
        # Caso 1: es un tipo int
        if match(numPattern,self.expresion1):
            expresionUno = int(self.expresion1)
        # Caso 2: es un simbolo
        elif symbol1 != None:
            expresionUno= symbol1.value
        # Caso 3: es una expresion
        else:
            expresionUno = self.expresion1.evaluar(symbolTable)
        # Segunda expresion
        # Caso 1: es un tipo int
        if match(numPattern,self.expresion2):
            expresionDos = int(self.expresion2)
        # Caso 2: es un simbolo
        elif symbol2 != None:
            expresionDos= symbol2.value
        # Caso 3: es una expresion
        else:
            expresionDos = self.expresion2.evaluar(symbolTable)     
        # Dependiendo del operador realizamos la operacion
        # Caso 1: Suma
        if (self.operador == "+"):
            return (expresionUno + expresionDos)
        # Caso 2: Resta
        elif (self.operador == "-"):
            return (expresionUno - expresionDos)
        # Caso 3: Multiplicacion
        elif (self.operador == "*"):
            return (expresionUno * expresionDos)
        # Caso 4: Division
        elif  (self.operador == "/"):
            # Verificamos que no sea una division indefinida
            if expresionDos == 0:
                print("ERROR: Division entre 0, comportamiento indefinido")
            return (expresionUno / expresionDos)
        # Caso 5: Modulo
        elif  (self.operador == "%"):
            return (expresionUno % expresionDos)

        
# Expresiones Relacionales
class ExpresionRelacional:
    def __init__(self, expresion1,operador=None,expresion2=None):
        self.expresion1 = expresion1
        self.operador = operador
        self.expresion2 = expresion2
    def __str__(self):
        espacio ="    "
        retorno = ""
        retorno += "\n"
        retorno += "\n"
        retorno += espacio + espacio + "- guardia: ExpresionRelacional"
        retorno += "\n"
        if( self.expresion1 != "(" ):
            if ( (self.operador != None) and (self.expresion2 != None) ):
                retorno += operacionBinariaString(self.expresion1,self.operador,self.expresion2)
            elif ( (self.operador == None) and (self.expresion2 == None) ):
                retorno += espacio + espacio + espacio + espacio + " - variable: " + self.expresion1
        retorno += "\n"
        return retorno   
    def evaluar(self,symbolTable):
        """
        Evalua la expresion y retorna el resultado
        
        @type  symbolTable: SymbolTable
        @param symbolTable: Tabla de simbolos actual
        @rtype:   bool
        @return:  Resultado de la expresion
        """        
        # Inicializamos las variables
        expresionUno = None
        expresionDos = None
        # Patron para la comparacion de numeros
        numPattern = compile('([0-9]+)|(-[0-9]+)')
        # Verificamos si las expresiones son simbolos
        symbol1 = symbolTable.searchForSymbol(self.expresion1)
        symbol2 = symbolTable.searchForSymbol(self.expresion2)
        # Dependiendo del operador entradas validas distintas
        # Caso 1: Igualdad y Desigualdad
        if self.operador == '/=' or self.operador == '=':
            # Primera expresion
            # Caso 1: es true
            if self.expresion1 == "true":
                expresionUno = True
            # Caso 2: es false
            elif self.expresion1 == "false":
                expresionUno = False
            # Caso 3: es un int
            elif match(numPattern,self.expresion1):
                expresionUno = int(self.expresion1)
            # Caso 4: es un simbolo
            elif symbol1 != None:
                expresionUno= symbol1.value
            # Caso 5: es una expresion
            else:
                expresionUno = self.expresion1.evaluar(symbolTable)
            # Segunda expresion
            # Caso 1: es true
            if self.expresion2 == "true":
                expresionDos = True
            # Caso 2: es false
            elif self.expresion2 == "false":
                expresionDos = False
            # Caso 3: es un int
            elif match(numPattern,self.expresion2):
                expresionDos = int(self.expresion2)
            # Caso 4: es un simbolo
            elif symbol2 != None:
                expresionDos= symbol2.value
            # Caso 5: es una expresion
            else:
                expresionDos = self.expresion2.evaluar(symbolTable)                
        # Caso 1: Mayor, Mayor o igual, Menor, Menor o Igual 
        elif (self.operador == '>' or self.operador == '>=' or self.operador == '<' 
              or self.operador == '<='):
            # Primera expresion
            # Caso 1: es un int
            if match(numPattern,self.expresion1):
                expresionUno = int(self.expresion1)
            # Caso 2: es un simbolo
            elif symbol1 != None:
                expresionUno= symbol1.value
            # Caso 3: es una expresion
            else:
                expresionUno = self.expresion1.evaluar(symbolTable)
            # Segunda expresion
            # Caso 1: es un int
            if match(numPattern,self.expresion2):
                expresionDos = int(self.expresion2)
            # Caso 2: es un simbolo
            elif symbol2 != None:
                expresionDos= symbol2.value
            # Caso 3: es una expresion
            else:
                expresionDos = self.expresion2.evaluar(symbolTable)  
        # Dependiendo del operador realizamos la operacion
        # Caso 1: Igualdad
        if (self.operador == "/="):
            return (expresionUno != expresionDos)
        # Caso 2: Desigualdad
        elif (self.operador == "="):
            return (expresionUno == expresionDos)
        # Caso 3: Mayor
        elif (self.operador == ">"):
            return (expresionUno > expresionDos)
        # Caso 4: Mayor o Igual
        elif (self.operador == ">="):
            return (expresionUno >= expresionDos)
        # Caso 5: Menor
        elif (self.operador == "<"):
            return (expresionUno < expresionDos)
        # Caso 6: Menor o Igual
        elif (self.operador == "<="):
            return (expresionUno <= expresionDos)

# Expresiones Booleanas
class ExpresionBooleana:
    def __init__(self,expresion1,operador=None,expresion2=None):
        self.expresion1 = expresion1
        self.operador = operador
        self.expresion2 = expresion2
    def __str__(self):
        espacio ="    "
        retorno = ""
        retorno += "\n"
        retorno += "\n"
        retorno += espacio + espacio + "- guardia: ExpresionBooleana"
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
    def evaluar(self,symbolTable):
        """
        Evalua la expresion y retorna el resultado
        
        @type  symbolTable: SymbolTable
        @param symbolTable: Tabla de simbolos actual
        @rtype:   bool
        @return:  Resultado de la expresion
        """  
        # Inicializamos las variables
        expresionUno = None
        expresionDos = None
        # Verificamos si las expresiones son simbolos
        symbol1 = symbolTable.searchForSymbol(self.expresion1)
        symbol2 = symbolTable.searchForSymbol(self.expresion2)
        # Caso 1: es un tipo string
        if type(self.expresion1) is str:
            # Caso 1.1: Es true
            if self.expresion1 == "true":
                expresionUno = True
            # Caso 1.2: Es false
            elif self.expresion1 == "false":
                expresionUno = False
            # Caso 1.3: Es un simbolo
            elif symbol1 != None:
                expresionUno= symbol1.value
        # Caso 2: Es una expresion
        else:
            expresionUno = self.expresion1.evaluar(symbolTable)
        # Caso 1: es un tipo string
        if type(self.expresion2) is str:
            # Caso 1.1: Es true
            if self.expresion2 == "true":
                expresionDos = True
            # Caso 1.2: Es false
            elif self.expresion2 == "false":
                expresionDos = False
            # Caso 1.3: Es un simbolo
            elif symbol2 != None:
                expresionDos= symbol2.value
        # Caso 2: Es una expresion
        else:
            expresionUno = self.expresion1.evaluar(symbolTable)  
        # Es una conjuncion
        if (self.operador == "/\\"):
            return (expresionUno and expresionDos)
        # Es una disjuncion
        elif (self.operador == "\/"):
            return (expresionUno or expresionDos)

# Expresiones con Parentizacion
class ParentizedExpresion:
    def __init__(self,abre,expresion,cierra):
        self.cierra = cierra
        self.expresion = expresion
        self.cierra = cierra
    def __str__(self):
        espacio = "    "
        retorno = ""
        retorno += "\n"
        retorno += "\n"
        retorno += espacio + espacio + "--- Open ParentizedExpresion ---"
        retorno += "\n"
        retorno += expresionParentesisString(self.expresion)
        retorno += "\n"
        retorno += espacio + espacio + "--- Close ParentizedExpresion ---"
        retorno += "\n"
        return retorno 
    def evaluar(self,symbolTable):
        """
        Evalua la expresion y retorna el resultado
        
        @type  symbolTable: SymbolTable
        @param symbolTable: Tabla de simbolos actual
        @rtype:   bool o int
        @return:  Resultado de la expresion
        """  
        return self.expresion.evaluar(symbolTable)
