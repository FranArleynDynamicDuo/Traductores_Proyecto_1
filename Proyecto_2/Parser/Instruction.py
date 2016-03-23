'''
Created on Feb 1, 2016

@author: francisco
'''


from abc import ABCMeta, abstractmethod
from Proyecto_3.contextAnalisis.contextAnalisis import SymbolTable
from Proyecto_3.contextAnalisis.contextAnalisis import Symbol
from copy import deepcopy
from re import compile
from re import match

from Proyecto_2.Parser.Expression import ArithmethicExpression
from Proyecto_2.Parser.Expression import RelationalExpresion
from Proyecto_2.Parser.Expression import BooleanExpression
from Proyecto_2.Parser.Expression import ParentizedExpression

BotSymbolTable = SymbolTable(None);
posicionMatrix = dict()
currentBotHorPosicion = None
currentBotVerPosicion = None
currentBotValue = None

def spacing(espacio):
    i = 0
    while (i < 4):
        espacio += " " 
        i += 1
    return espacio

def getValueInPosicionMatrix(matrix,horPosicion,verPosicion):
    stringPosicion = "(" + str(horPosicion) + "," + str(verPosicion) + ")"
    return matrix.get(stringPosicion)
    
def setValueInPosicionMatrix(matrix,horPosicion,verPosicion,element):
    stringPosicion = "(" + str(horPosicion) + "," + str(verPosicion) + ")"
    matrix.update({stringPosicion : element})
    return matrix

def obtainValueFromString(stringElement):
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
    
    # Corrida de la instruccion
    def run(self):
        global BotSymbolTable
        global posicionMatrix
        posicionMatrix = dict()
        
        
        # Revisamos si hay declaraciones de bots
        if self.createSet != None:
            # Revisamos si estamos en una tabla vacia
            if BotSymbolTable.emptyTable():
                pass
            # Si no es asi, bajamos a un nivel de tabla inferior
            else:
                BotSymbolTable = SymbolTable(deepcopy(BotSymbolTable))
            
            i = 0
               
            for i in  range(0,len(self.createSet)):
                (self.createSet[i]).run()
        
        i = 0
          
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

    # Corrida de la instruccion
    def run(self):
        global BotSymbolTable
        global posicionMatrix
        
        symbol = Symbol(self.identifier,self.botType,None)
        symbol.behaviorTable = self.declarationSet
        
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
 
    # Corrida de la instruccion
    def run(self):
        
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
        return botResult.getValue()

# Clase Intrucciones del boot
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
        global BotSymbolTable
        global posicionMatrix
        
        if self.command == 'store':
            
            # Caso 1: El argumento es una expresion
            if (type(self.argument) is ArithmethicExpression or 
                  type(self.argument) is BooleanExpression or
                  type(self.argument) is RelationalExpresion or
                  type(self.argument) is ParentizedExpression):
                result = self.argument.evaluar(BotSymbolTable)
            else:
                result = obtainValueFromString(self.argument)
            
            BotSymbolTable.updateSymbolValue("me",result)
                

        elif self.command == 'collect':
            
            symbol = BotSymbolTable.searchForSymbol("me")
            result = getValueInPosicionMatrix(posicionMatrix,symbol.horPosicion,symbol.verPosicion)
            
            if self.argument is None:
                
                BotSymbolTable.updateSymbolValue("me",result)

            else:
                upperlevel = BotSymbolTable.getUpperLevel()
                symbol = upperlevel.searchForSymbol(self.argument)
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

        elif self.command == 'drop':
            symbol = BotSymbolTable.searchForSymbol("me")
            
            # Caso 1: El argumento es una expresion
            if (type(self.argument) is ArithmethicExpression or 
                  type(self.argument) is BooleanExpression or
                  type(self.argument) is RelationalExpresion or
                  type(self.argument) is ParentizedExpression):
                resultado = self.argument.evaluar(BotSymbolTable)
            else:
                resultado = obtainValueFromString(self.argument)
            
            posicionMatrix = setValueInPosicionMatrix(posicionMatrix,symbol.horPosicion,symbol.verPosicion,resultado)
            
        elif self.command == 'send':

            symbol = BotSymbolTable.searchForSymbol("me")
            value = symbol.getValue()
            if type(value) is str:
                print(value,end="")
            else:
                print(str(symbol.getValue()),end="")
            
        elif self.command == 'read':
            
            symbol = BotSymbolTable.searchForSymbol("me")
            
            stringElement = input("Value To Read " + "(" + symbol.getType()  + " type): ")
            
            element = obtainValueFromString(stringElement)
            
            if self.argument is None:
                pass
            else:
                symbol = BotSymbolTable.searchForSymbol(self.argument)
                
            BotSymbolTable.updateSymbolValue(symbol.getIdentifier(),element)
            
        elif self.command == 'left':
            
            symbol = BotSymbolTable.searchForSymbol("me")
            
            if self.argument is None:
                BotSymbolTable.updateSymbolHorPosicion("me",symbol.horPosicion - 1)
            else:
                BotSymbolTable.updateSymbolHorPosicion("me",symbol.horPosicion - self.argument.evaluar(BotSymbolTable))
            
        elif self.command == 'right':

            symbol = BotSymbolTable.searchForSymbol("me")
            
            if self.argument is None:
                BotSymbolTable.updateSymbolHorPosicion("me",symbol.horPosicion + 1)
            else:
                BotSymbolTable.updateSymbolHorPosicion("me",symbol.horPosicion + self.argument.evaluar(BotSymbolTable))
            

        elif self.command == 'up':

            symbol = BotSymbolTable.searchForSymbol("me")
            
            if self.argument is None:
                BotSymbolTable.updateSymbolVerPosicion("me",symbol.verPosicion + 1)
            else:
                BotSymbolTable.updateSymbolVerPosicion("me",symbol.verPosicion + self.argument.evaluar(BotSymbolTable))
            

        elif self.command == 'down':
            
            symbol = BotSymbolTable.searchForSymbol("me")
            
            if self.argument is None:
                BotSymbolTable.updateSymbolVerPosicion("me",symbol.verPosicion + 1)
            else:
                BotSymbolTable.updateSymbolVerPosicion("me",symbol.verPosicion + self.argument.evaluar(BotSymbolTable))

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
        for instruction in self.ifInstructionSet :
            retorno += str(instruction)
        
        if self.elseInstructionSet != None:
            for instruction in self.elseInstructionSet :
                retorno += str(instruction)
        return retorno

    # Corrida de la instruccion
    def run(self):
        if (self.ifCondition.evaluar(BotSymbolTable)):
            for i in  range(0,self.ifInstructionSet.len):
                self.ifInstructionSet[i].run()
        elif (self.elseInstructionSet):
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

    # Corrida de la instruccion
    def run(self):
        while (self.condition.evaluar(BotSymbolTable)):
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
 
    # Corrida de la instruccion
    def run(self):
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
                            BotSymbolTable.updateSymbolValue(self.identList[j],result)
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

    # Corrida de la instruccion
    def run(self):
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
                            BotSymbolTable.updateSymbolValue(self.identList[j],result)
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
        
    # Corrida de la instruccion
    def run(self):
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
                                BotSymbolTable.updateSymbolValue(self.identList[j],result)
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
                                BotSymbolTable.updateSymbolValue(self.identList[j],result)
                            break
            # El Bot no estaba activo, ERROR
            else:
                print("ERROR: " +self.identList[j]+ " no se encontraba activo")
                exit()  