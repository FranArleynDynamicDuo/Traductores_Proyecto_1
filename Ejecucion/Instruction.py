'''
Created on Feb 1, 2016

@author: francisco
'''


from abc import ABCMeta, abstractmethod
from AnalisisContexto.SymbolTable import SymbolTable
from AnalisisContexto.Symbol import Symbol
from copy import deepcopy
from re import compile
from re import match

from Ejecucion.Expression import ArithmethicExpression
from Ejecucion.Expression import RelationalExpresion
from Ejecucion.Expression import BooleanExpression
from Ejecucion.Expression import ParentizedExpression

BotSymbolTable = SymbolTable(None);
posicionmatriz = dict()
currentBotHorPosicion = None
currentBotVerPosicion = None
currentBotValue = None

def getValueInPosicionmatriz(matriz,horPosicion,verPosicion):
    """
    Toma una matriz y unas coordenadas y obtiene el valor almacenado
    en esas coordenadas
    
    @type  matriz: Dict
    @param matriz: Matriz de recorrido de los bots
    @type  horPosicion: int
    @param horPosicion: posicion en el eje horizontal de la matriz
    @type  verPosicion: int
    @param verPosicion: posicion en el eje vertical de la matriz
    @rtype: Object
    @return: valor almacenado en la posicion deseada de la matriz
    """
    # Formamos el string de coordenadas
    stringPosicion = "(" + str(horPosicion) + "," + str(verPosicion) + ")"
    # Retornamos el valor
    return matriz.get(stringPosicion)
    
def setValueInPosicionmatriz(matriz,horPosicion,verPosicion,element):
    """
    Toma una matriz y unas coordenadas y guarda un valor en la celda
    apuntada por las coordenadas
    
    @type  matriz: Dict
    @param matriz: Matriz de recorrido de los bots
    @type  horPosicion: int
    @param horPosicion: posicion en el eje horizontal de la matriz
    @type  verPosicion: int
    @param verPosicion: posicion en el eje vertical de la matriz
    @type  element: Object
    @param element: Valor a ser almacenado
    @rtype: Dict
    @return: Matriz actualizada
    """
    # Formamos el string de coordenadas
    stringPosicion = "(" + str(horPosicion) + "," + str(verPosicion) + ")"
    # Guardamos el elemento en la matriz
    matriz.update({stringPosicion : element})
    # Retornamos la matriz actualizada
    return matriz

def obtainValueFromString(stringElement):
    """
    Toma un string y lo transforma en el tipo primitivo que corresponda
    Puede ser bool, str o int
    
    @type  stringElement: Str
    @param stringElement: Elemento a transformar
    @rtype: Object
    @return: Objeto primitivo
    """
    global BotSymbolTable
    charPattern = r"'(.)'|'(\\n)'|'(\\t)'|'\\''"
    numPattern = compile('([0-9]+)|(-[0-9]+)')
    
    if match(numPattern,stringElement):
        element = int(stringElement)
    elif stringElement == 'true':
        element = True
    elif stringElement == 'false':
        element = False
    elif match(charPattern,stringElement):
        element = ""
        if stringElement == "'\\n'":
            element = "\n"
        elif stringElement == "'\\t'":
            element = "\t"
        elif stringElement == "'\\''":
            element = "'"
        else:
            for i in range(1,len(stringElement) -1):
                element += stringElement[i]
    else:
        symbol = BotSymbolTable.searchForSymbol(stringElement)
        if (symbol):
            element = symbol.getValue()
        else:
            print('Lectura Invalida')
            exit()
    return element
        
class InstructionClass(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self, params):
        pass
    
class Program(InstructionClass):
    def __init__(self, executeSet, createSet=None):
        self.createSet = createSet
        self.executeSet = executeSet
    def __str__(self):
        retorno = ""
        retorno += "\n"
        retorno += "--------(Program)-------"
        retorno += "\n"
        retorno += "PROGRAM"
        retorno += "\n"
        if self.createSet != None:
            retorno += "CREATE"
            retorno += "\n"
            for create in self.createSet :
                retorno += str(create)
        retorno += "EXECUTE"
        retorno += "\n"
        for execute in self.executeSet :
            retorno += str(execute)
        retorno += "\n"
        return retorno
    def run(self):
        """
        Corrida de la instruccion
        """
        global BotSymbolTable
        global posicionmatriz
        # Revisamos si hay declaraciones de bots
        if self.createSet != None:
            # Revisamos si estamos en una tabla vacia
            if BotSymbolTable.emptyTable():
                pass
            # Si no es asi, bajamos a un nivel de tabla inferior
            else:
                BotSymbolTable = SymbolTable(deepcopy(BotSymbolTable))
            # Reiniciamos el iterador
            i = 0
            # Recorremos las declaraciones de los bots
            for i in  range(0,len(self.createSet)):
                (self.createSet[i]).run()
        # Reiniciamos el iterador
        i = 0
        # Recorremos las instrucciones del programa
        for i in  range(0,len(self.executeSet)):
            (self.executeSet[i]).run()
        # Si no estamos en la tabla tope subimos un nivel
        if BotSymbolTable.getUpperLevel() != None:
            BotSymbolTable.getUpperLevel()
        
# Clase Crear el LexBot 
class CreateInstruction(InstructionClass):
    def __init__(self, botType,identifier,declarationSet ):
        self.botType = botType
        self.identifier = identifier
        self.declarationSet = declarationSet    
    def __str__(self):
        espacio = ""
        retorno = ""
        retorno += "CREAR BOT"
        retorno += "\n"
        retorno += espacio + espacio + " - Tipo: " + str(self.botType);
        retorno += "\n"
        retorno += espacio + espacio + " - Nombre: " +  str(self.identifier);
        retorno += "\n"
        for declarion in self.declarationSet:
            if declarion != None:
                retorno += espacio + espacio + espacio + espacio +  str(declarion)
        retorno += "\n"
        return retorno
    def run(self):
        """
        Corrida de la instruccion
        """
        global BotSymbolTable
        global posicionmatriz
        # Creamos el simbolo
        symbol = Symbol(self.identifier,self.botType,None)
        symbol.behaviorTable = self.declarationSet
        # Agregamos el simbolo a la tabla
        BotSymbolTable.addToTable(self.identifier, symbol)

# Clase Declaracion del bot
class BotBehavior(InstructionClass):
    def __init__(self,condition,instructionSet ):
        self.condition = condition
        self.instructionSet = instructionSet
    def __str__(self):
        espacio = ""
        retorno = ""
        if (self.condition == "activation"):
            retorno +=espacio + "ACTIVACION"
        elif (self.condition == "deactivation"):
            retorno +=espacio + "DESACTIVACION"
        elif (self.condition == "default"):
            retorno +=espacio + "DEFAULT"
        retorno += "\n"
        for instruction in self.instructionSet:
            if instruction != None:
                retorno += espacio + espacio + espacio + espacio + str(instruction)
                retorno += "\n"
        return retorno
    def run(self):
        """
        Corrida de la instruccion
        """
        global BotSymbolTable
        global currentBotType
        global currentBotValue
        global currentBotHorPosicion
        global currentBotVerPosicion
        # Corremos las instrucciones
        for i in  range(0,len(self.instructionSet)):
            self.instructionSet[i].run()        
        # obtenemos el nuevo valor del bot
        botResult = BotSymbolTable.searchForSymbol("me")
        # Volvemos a la tabla de simbolos original
        BotSymbolTable = BotSymbolTable.getUpperLevel()
        return botResult
    
class BotInstruction(InstructionClass):
    def __init__(self, command,argument=None):
        self.command = command
        self.argument = argument
    def __str__(self):
        espacio = ""
        retorno = ""
        if (self.argument != None):
            if (self.command == "store"):
                retorno +=espacio + espacio + espacio + espacio + " - instruccion: almacenamiento"
            elif (self.command == "collect"):
                retorno +=espacio + espacio + espacio+ espacio+ " - instruccion: coleccion"
            elif (self.command == "recieve"):
                retorno +=espacio + espacio+ espacio+ espacio + " - instruccion: lectura"
            elif (self.command == "drop"):
                retorno +=espacio + espacio + espacio+ espacio + " - instruccion: soltado"  
            retorno += "\n"
            retorno +=espacio + espacio + " - valor: "  + str(self.argument)
        elif (self.argument == None):
            if (self.command == "send"):
                retorno +=espacio + espacio+ espacio+ espacio + " - instruccion: enviar"
            elif (self.command == "read"):
                retorno +=espacio + espacio+ espacio+ espacio + " - instruccion: leer"
            elif (self.command == "left"):
                retorno +=espacio + espacio+ espacio+ espacio + " - instruccion: movimiento hacia la izquierda"
            elif (self.command == "right"):
                retorno +=espacio + espacio+ espacio+ espacio + " - instruccion: movimiento hacia la derecha"
            elif (self.command == "up"):
                retorno +=espacio + espacio+ espacio+ espacio + " - instruccion: movimiento hacia arriba"
            elif (self.command == "down"):
                retorno +=espacio + espacio + " - instruccion: movimiento hacia abajo"
        retorno += "\n"
        return retorno 
    def run(self):
        """
        Corrida de la instruccion
        """
        global BotSymbolTable
        global posicionmatriz
        # STORE
        if self.command == 'store':
            # Caso 1: El argumento es una expresion
            if (type(self.argument) is ArithmethicExpression or 
                  type(self.argument) is BooleanExpression or
                  type(self.argument) is RelationalExpresion or
                  type(self.argument) is ParentizedExpression):
                result = self.argument.evaluar(BotSymbolTable)
            # Caso 2: El argumento es un string de un tipo primitivo
            else:
                result = obtainValueFromString(self.argument)
            # Actualizamos el valor del bot
            BotSymbolTable.updateSymbolValue("me",result)
        # COLLECT
        elif self.command == 'collect':
            # Buscamos los datos actuales del bot
            symbol = BotSymbolTable.searchForSymbol("me")
            # Obtenemos el valor de la posicion actual de la matriz
            result = getValueInPosicionmatriz(posicionmatriz,symbol.horPosicion,symbol.verPosicion)
            # Si no recibimos argumento lo guardamos en el bot
            if self.argument is None:
                BotSymbolTable.updateSymbolValue("me",result)
            else:
                # Buscamos a ver si la variable ya fue declarada anteriormente
                upperlevel = BotSymbolTable.getUpperLevel()
                symbol = upperlevel.searchForSymbol(self.argument)
                # Si no encontramos la variable seguimos
                if not (symbol):
                    symbol = BotSymbolTable.searchForSymbol(self.argument)
                    if symbol != None:
                        BotSymbolTable.updateSymbolValue(symbol.getIdentifier(),result)
                    # Variable no declarada, debe agregarse
                    else:
                        symbol = Symbol(self.argument,None,None)
                        symbol = symbol.createSymbolFromValue(result)
                        BotSymbolTable.addToTable(symbol.getIdentifier(),symbol)
                # Variable declarada en otro nivel, ERROR
                else:
                    print("ERROR: Variable Declarada anteriormente en un alcance anterior\n")
                    exit()
        # DROP
        elif self.command == 'drop':
            # Buscamos los datos actuales del bot
            symbol = BotSymbolTable.searchForSymbol("me")
            # Caso 1: El argumento es una expresion
            if (type(self.argument) is ArithmethicExpression or 
                  type(self.argument) is BooleanExpression or
                  type(self.argument) is RelationalExpresion or
                  type(self.argument) is ParentizedExpression):
                resultado = self.argument.evaluar(BotSymbolTable)
            # Caso 2: El argumento es un string de un tipo primitivo
            else:
                resultado = obtainValueFromString(self.argument)
            # Guardamos el valor en la matriz
            posicionmatriz = setValueInPosicionmatriz(posicionmatriz,symbol.horPosicion,symbol.verPosicion,resultado)
        # SEND            
        elif self.command == 'send':
            # Buscamos los datos actuales del bot
            symbol = BotSymbolTable.searchForSymbol("me")
            # Obtenemos el valor del bot
            value = symbol.getValue()
            # Si es un string lo imprimimos
            if type(value) is str:
                print(value,end="")
            # Si no es un string lo transformamos en string antes de imprimirlo
            else:
                print(str(symbol.getValue()),end="")
        # READ            
        elif self.command == 'read':
            # Buscamos los datos actuales del bot
            symbol = BotSymbolTable.searchForSymbol("me")
            # Obtenemos la entrada del usuario
            stringElement = input("Value To Read " + "(" + symbol.getType()  + " type): ")
            # Convertimos esa entrada en un tipo primitivo
            element = obtainValueFromString(stringElement)
            # Caso 1: Se guardara en el bot
            if self.argument is None:
                pass
            # Caso 2: Se guardara en una variable
            else:
                symbol = BotSymbolTable.searchForSymbol(self.argument)
            # Actualizamos el valor del bot     
            BotSymbolTable.updateSymbolValue(symbol.getIdentifier(),element)
        # LEFT            
        elif self.command == 'left':
            # Buscamos los datos actuales del bot
            symbol = BotSymbolTable.searchForSymbol("me")
            # Caso 1: Se movera 1 paso
            if self.argument is None:
                BotSymbolTable.updateSymbolHorPosicion("me",symbol.horPosicion - 1)
            # Caso 2: Se moveran varios pasos
            else:
                BotSymbolTable.updateSymbolHorPosicion("me",symbol.horPosicion - self.argument.evaluar(BotSymbolTable))
        # RIGHT            
        elif self.command == 'right':
            # Buscamos los datos actuales del bot
            symbol = BotSymbolTable.searchForSymbol("me")
            # Caso 1: Se movera 1 paso
            if self.argument is None:
                BotSymbolTable.updateSymbolHorPosicion("me",symbol.horPosicion + 1)
            # Caso 2: Se moveran varios pasos
            else:
                BotSymbolTable.updateSymbolHorPosicion("me",symbol.horPosicion + self.argument.evaluar(BotSymbolTable))
        # UP
        elif self.command == 'up':
            # Buscamos los datos actuales del bot
            symbol = BotSymbolTable.searchForSymbol("me")
            # Caso 1: Se movera 1 paso
            if self.argument is None:
                BotSymbolTable.updateSymbolVerPosicion("me",symbol.verPosicion + 1)
            # Caso 2: Se moveran varios pasos
            else:
                BotSymbolTable.updateSymbolVerPosicion("me",symbol.verPosicion + self.argument.evaluar(BotSymbolTable))
        # DOWN
        elif self.command == 'down':
            # Buscamos los datos actuales del bot
            symbol = BotSymbolTable.searchForSymbol("me")
            # Caso 1: Se movera 1 paso
            if self.argument is None:
                BotSymbolTable.updateSymbolVerPosicion("me",symbol.verPosicion - 1)
            # Caso 2: Se moveran varios pasos
            else:
                BotSymbolTable.updateSymbolVerPosicion("me",symbol.verPosicion - self.argument.evaluar(BotSymbolTable))

# Class ConditionalInstruction      
class ConditionalInstruction(InstructionClass):
    def __init__(self,ifCondition,ifInstructionSet,elseInstructionSet=None):
        self.ifCondition = ifCondition
        self.ifInstructionSet = ifInstructionSet
        self.elseInstructionSet = elseInstructionSet    
    def __str__(self):
        retorno = ""
        retorno += "\n"
        retorno += "--------(ConditionalInstruction)-------"
        retorno += "\n"
        retorno += "    CONDICIONAL"
        retorno += str(self.ifCondition)
        # Recorremos las instrucciones del if
        for instruction in self.ifInstructionSet :
            retorno += str(instruction)
        # Si hay else, recorremos las instrucciones del else
        if self.elseInstructionSet != None:
            for instruction in self.elseInstructionSet :
                retorno += str(instruction)
        return retorno
    def run(self):
        """
        Corrida de la instruccion
        """
        # Caso 1: Se cumple la condicion del if
        if (self.ifCondition.evaluar(BotSymbolTable)):
            # recorremos y corremos las instrucciones
            for i in  range(0,self.ifInstructionSet.len):
                self.ifInstructionSet[i].run()
        # Caso 2: Si hay condicion de else y no se cumplio el if
        elif (self.elseInstructionSet):
            # recorremos y corremos las instrucciones
            for i in  range(0,self.elseInstructionSet.len):
                self.elseInstructionSet[i].run()
        
# Class whileInstruction
class whileInstruction(InstructionClass):

    def __init__(self,condition,instructionSet):
        self.condition = condition
        self.instructionSet = instructionSet
    def __str__(self):
        retorno = ""
        retorno += "\n"
        retorno += "--------(whileInstruction)-------"
        retorno += "\n"
        retorno += "    ITERACION INDETERMINADA"
        retorno += "\n"
        retorno += str(self.condition)
        for instruction in self.instructionSet :
            retorno += str(instruction)
        return retorno
    def run(self):
        """
        Corrida de la instruccion
        """
        # Mientras se cumpla la condicion iteramos
        while (self.condition.evaluar(BotSymbolTable)):
            # Recorremos y corremos las instrucciones
            for i in  range(0,len(self.instructionSet)):
                self.instructionSet[i].run()
        
# Class ActivateInstruction (REVISAR COMO HACER EL FOR PENDIENTE EN DONDE)
class ActivateInstruction:
    
    def __init__(self,identList):
        self.identList = identList
        

    def __str__(self):
        espacio = "  "
        retorno = ""
        retorno += "\n"
        retorno += "--------(ActivateInstruction)-------"
        retorno += "\n"
        retorno += "    ACTIVACION"
        retorno += "\n"
        for nameBot in self.identList :
            retorno += espacio + espacio + " - var: " + str(nameBot)
            retorno += "\n"
        return retorno
 
    def run(self):
        """
        Corrida de la instruccion
        """
        global BotSymbolTable
        global currentBotType
        global currentBotValue
        global currentBotHorPosicion
        global currentBotVerPosicion
        
        j = 0
        # Por cada bot
        for j in range(0,len(self.identList)):
            
            symbol = BotSymbolTable.searchForSymbol(self.identList[j])
            
            currentBotType = symbol.getType()
            currentBotValue = symbol.getValue()
            currentBotHorPosicion = symbol.horPosicion
            currentBotVerPosicion = symbol.verPosicion
            
            
            BotSymbolTable = SymbolTable(deepcopy(BotSymbolTable))
        
            symbolMe = Symbol("me",currentBotType,currentBotValue)
            
            symbolMe.horPosicion = currentBotHorPosicion
            symbolMe.verPosicion = currentBotVerPosicion
            
            BotSymbolTable = BotSymbolTable.addToTable(symbolMe.getIdentifier(),symbolMe)
            
            # Si el bot esta desactivado procedemos
            if symbol.activated == False:
                # Buscamos el comportamiento correspondiente
                for behavior in symbol.behaviorTable:
                    if behavior.condition == 'activation':
                        result = behavior.run()
                        # Si la operacion devuelve un resultado actualizamos el valor del bot
                        if result != None:
                            BotSymbolTable.updateSymbolValue(self.identList[j],result.value)
                            BotSymbolTable.updateSymbolHorPosicion(self.identList[j],result.horPosicion)
                            BotSymbolTable.updateSymbolVerPosicion(self.identList[j],result.verPosicion)
                        break
                BotSymbolTable.updateSymbolStatus(self.identList[j],True)        
            # El Bot ya estaba activo, ERROR
            else:
                print("ERROR: " +self.identList[j]+ " ya se encontraba activo")
                exit()

        
# Class DeactivateInstruction (REVISAR COMO HACER EL FOR PENDIENTE EN DONDE)
class DeactivateInstruction:
    def __init__(self,identList):
        self.identList = identList
    def __str__(self):
        espacio = "  "
        retorno = ""
        retorno += "\n"
        retorno += "--------(DeactivateInstruction)-------"
        retorno += "\n"
        retorno += "    DESACTIVACION"
        retorno += "\n"
        for nameBot in self.identList :
            retorno += espacio + espacio + " - var: " + str(nameBot)
            retorno += "\n"
        return retorno
    def run(self):
        """
        Corrida de la instruccion
        """
        global BotSymbolTable
        global currentBotType
        global currentBotValue
        global currentBotHorPosicion
        global currentBotVerPosicion
        # Por cada bot
        for j in range(0,len(self.identList)):
            
            
            symbol = BotSymbolTable.searchForSymbol(self.identList[j])
            
            currentBotType = symbol.getType()
            currentBotValue = symbol.getValue()
            currentBotHorPosicion = symbol.horPosicion
            currentBotVerPosicion = symbol.verPosicion
            
            BotSymbolTable = SymbolTable(deepcopy(BotSymbolTable))
        
            symbolMe = Symbol("me",currentBotType,currentBotValue)
            
            symbolMe.horPosicion = currentBotHorPosicion
            symbolMe.verPosicion = currentBotVerPosicion
            
            BotSymbolTable = BotSymbolTable.addToTable(symbolMe.getIdentifier(),symbolMe) 
            
            # Buscamos el simbolo correspondiente al bot
            symbol = BotSymbolTable.searchForSymbol(self.identList[j])
            currentBotType = symbol.getType()
            currentBotHorPosicion = symbol.horPosicion
            currentBotVerPosicion = symbol.verPosicion
            currentBotValue = symbol.getValue()
            # Si el bot esta desactivado procedemos
            if symbol.activated == True:
                # Buscamos el comportamiento correspondiente
                for behavior in symbol.behaviorTable:
                    if behavior.condition == 'deactivation':
                        result = behavior.run()
                        # Si la operacion devuelve un resultado actualizamos el valor del bot
                        if result != None:
                            BotSymbolTable.updateSymbolValue(self.identList[j],result.value)
                            BotSymbolTable.updateSymbolHorPosicion(self.identList[j],result.horPosicion)
                            BotSymbolTable.updateSymbolVerPosicion(self.identList[j],result.verPosicion)
                        break
                BotSymbolTable.updateSymbolStatus(self.identList[j],False)
            # El Bot ya estaba activo, ERROR
            else:
                print("ERROR: " +self.identList[j]+ " no se encontraba activo")
                exit()

# Class AdvanceInstruction
class AdvanceInstruction:
    def __init__(self,identList):
        self.identList = identList
    def __str__(self):
        espacio = "    "
        retorno = ""
        retorno += "\n"
        retorno += "--------(AdvanceInstruction)-------"
        retorno += "\n"
        retorno += "    AVANCE"
        retorno += "\n"
        for nameBot in self.identList :
            retorno += espacio + espacio + " - var: " + str(nameBot)
            retorno += "\n"
        return retorno
    def run(self):
        """
        Corrida de la instruccion
        """
        global BotSymbolTable
        global currentBotType
        global currentBotValue
        global currentBotHorPosicion
        global currentBotVerPosicion
        
        # Por cada bot
        for j in range(0,len(self.identList)):
            
            symbol = BotSymbolTable.searchForSymbol(self.identList[j])
            
            currentBotType = symbol.getType()
            currentBotValue = symbol.getValue()
            currentBotHorPosicion = symbol.horPosicion
            currentBotVerPosicion = symbol.verPosicion
            
            BotSymbolTable = SymbolTable(deepcopy(BotSymbolTable))
        
            symbolMe = Symbol("me",currentBotType,currentBotValue)
            
            symbolMe.horPosicion = currentBotHorPosicion
            symbolMe.verPosicion = currentBotVerPosicion
            
            BotSymbolTable = BotSymbolTable.addToTable(symbolMe.getIdentifier(),symbolMe)
            
            defaultEnabled = True
            defaultPosicion = None
            # Buscamos el simbolo correspondiente al bot
            symbol = BotSymbolTable.searchForSymbol(self.identList[j])
            currentBotType = symbol.getType()
            currentBotHorPosicion = symbol.horPosicion
            currentBotVerPosicion = symbol.verPosicion
            currentBotValue = symbol.getValue()
            # Si el bot esta activado procedemos
            if symbol.activated == True:
                # Buscamos comportamientos personalizados
                for i in range(0,len(symbol.behaviorTable)):
                    # Buscamos los comportamientos con expresiones
                    if (type(symbol.behaviorTable[i].condition) is ParentizedExpression or
                        type(symbol.behaviorTable[i].condition) is BooleanExpression or
                        type(symbol.behaviorTable[i].condition) is RelationalExpresion):
                        # Si ya se ha encontrado default entonces hay un ERROR
                        if defaultPosicion != None:
                            print("ERROR: Default definido antes que comportamiento con expresion")
                            exit()
                        # Buscamos el primero que se cumpla
                        if symbol.behaviorTable[i].condition.evaluar(BotSymbolTable) == True:
                            result = symbol.behaviorTable[i].run()
                            # Si la operacion devuelve un resultado actualizamos el valor del bot
                            if result != None:
                                BotSymbolTable.updateSymbolValue(self.identList[j],result.value)
                                BotSymbolTable.updateSymbolHorPosicion(self.identList[j],result.horPosicion)
                                BotSymbolTable.updateSymbolVerPosicion(self.identList[j],result.verPosicion)
                            defaultEnabled = False
                            break
                    elif symbol.behaviorTable[i].condition == 'default':
                        defaultPosicion = i
                    
                if defaultEnabled: 
                    # Buscamos el comportamiento default
                    for behavior in symbol.behaviorTable:
                        if behavior.condition == 'default':
                            result = behavior.run()
                            # Si la operacion devuelve un resultado actualizamos el valor del bot
                            if result != None:
                                BotSymbolTable.updateSymbolValue(self.identList[j],result.value)
                                BotSymbolTable.updateSymbolHorPosicion(self.identList[j],result.horPosicion)
                                BotSymbolTable.updateSymbolVerPosicion(self.identList[j],result.verPosicion)
                            break
            # El Bot no estaba activo, ERROR
            else:
                print("ERROR: " +self.identList[j]+ " no se encontraba activo")
                exit()  