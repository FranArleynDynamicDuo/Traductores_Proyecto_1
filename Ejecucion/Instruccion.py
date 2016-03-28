'''
Created on Feb 1, 2016

@author: francisco
'''


from abc import ABCMeta, abstractmethod
from AnalisisContexto.TablaDeSimbolos import TablaDeSimbolos
from AnalisisContexto.Simbolo import Simbolo
from copy import deepcopy
from re import compile
from re import match

from Ejecucion.Expresion import ExpresionAritmetica
from Ejecucion.Expresion import ExpresionRelacional
from Ejecucion.Expresion import ExpresionBooleana
from Ejecucion.Expresion import ExpresionParentizada

BotSymbolTable = TablaDeSimbolos(None);
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
    # Patrones necesarios para la comporacion
    charPattern = r"'(.)'|'(\\n)'|'(\\t)'|'\\''"
    numPattern = compile('([0-9]+)|(-[0-9]+)')
    
    # Caso 1: Es un entero
    if match(numPattern,stringElement):
        element = int(stringElement)
    # Caso 2: Es true
    elif stringElement == 'true':
        element = True
    # Caso 3: Es false
    elif stringElement == 'false':
        element = False
    # Caso 4: Es un caracter
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
    # Caso 5: Es un identificador o una lectura invalida
    else:
        simbolo = BotSymbolTable.buscarSimbolo(stringElement)
        # Caso 5.1: Es un identificador
        if (simbolo):
            if simbolo.activado == False:
                print('Bot no activado!')
                exit()
            element = simbolo.obtenerValor()
            if not element:
                print('Bot no inicializado!')
                exit()
        # Caso 5.2: Es una lectura invalida
        else:
            print('Lectura Invalida')
            exit()
    return element
        
class InstruccionClass(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self, params):
        pass
    
class Program(InstruccionClass):
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
                BotSymbolTable = TablaDeSimbolos(deepcopy(BotSymbolTable))
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
        if BotSymbolTable.obtenerNivelSuperior() != None:
            BotSymbolTable.obtenerNivelSuperior()
        
# Clase Crear el LexBot 
class CreateInstruccion(InstruccionClass):
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
        simbolo = Simbolo(self.identifier,self.botType,None)
        simbolo.behaviorTable = self.declarationSet
        # Agregamos el simbolo a la tabla
        BotSymbolTable.agregarATabla(self.identifier, simbolo)

# Clase Declaracion del bot
class BotBehavior(InstruccionClass):
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
        botResult = BotSymbolTable.buscarSimbolo("me")
        # Volvemos a la tabla de simbolos original
        BotSymbolTable = BotSymbolTable.obtenerNivelSuperior()
        return botResult
    
class BotInstruccion(InstruccionClass):
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
            if (type(self.argument) is ExpresionAritmetica or 
                  type(self.argument) is ExpresionBooleana or
                  type(self.argument) is ExpresionRelacional or
                  type(self.argument) is ExpresionParentizada):
                result = self.argument.evaluar(BotSymbolTable)
            # Caso 2: El argumento es un string de un tipo primitivo
            else:
                result = obtainValueFromString(self.argument)
            # Actualizamos el valor del bot
            BotSymbolTable.actualizarValorDeSimbolo("me",result)
        # COLLECT
        elif self.command == 'collect':
            # Buscamos los datos actuales del bot
            simbolo = BotSymbolTable.buscarSimbolo("me")
            # Obtenemos el valor de la posicion actual de la matriz
            result = getValueInPosicionmatriz(posicionmatriz,simbolo.horPosicion,simbolo.verPosicion)
            # Si no recibimos argumento lo guardamos en el bot
            if self.argument is None:
                BotSymbolTable.actualizarValorDeSimbolo("me",result)
            else:
                # Buscamos a ver si la variable ya fue declarada anteriormente
                upperlevel = BotSymbolTable.obtenerNivelSuperior()
                simbolo = upperlevel.buscarSimbolo(self.argument)
                # Si no encontramos la variable seguimos
                if not (simbolo):
                    simbolo = BotSymbolTable.buscarSimbolo(self.argument)
                    if simbolo != None:
                        BotSymbolTable.actualizarValorDeSimbolo(simbolo.obtenerIdentificador(),result)
                    # Variable no declarada, debe agregarse
                    else:
                        simbolo = Simbolo(self.argument,None,None)
                        simbolo = simbolo.crearSimboloDeValor(result)
                        simbolo.activado = True
                        BotSymbolTable.agregarATabla(simbolo.obtenerIdentificador(),simbolo)
                # Variable declarada en otro nivel, ERROR
                else:
                    print("ERROR: Variable Declarada anteriormente en un alcance anterior\n")
                    exit()
        # DROP
        elif self.command == 'drop':
            # Buscamos los datos actuales del bot
            simbolo = BotSymbolTable.buscarSimbolo("me")
            # Caso 1: El argumento es una expresion
            if (type(self.argument) is ExpresionAritmetica or 
                  type(self.argument) is ExpresionBooleana or
                  type(self.argument) is ExpresionRelacional or
                  type(self.argument) is ExpresionParentizada):
                resultado = self.argument.evaluar(BotSymbolTable)
            # Caso 2: El argumento es un string de un tipo primitivo
            else:
                resultado = obtainValueFromString(self.argument)
            # Guardamos el valor en la matriz
            posicionmatriz = setValueInPosicionmatriz(posicionmatriz,simbolo.horPosicion,simbolo.verPosicion,resultado)
        # SEND            
        elif self.command == 'send':
            # Buscamos los datos actuales del bot
            simbolo = BotSymbolTable.buscarSimbolo("me")
            # Obtenemos el valor del bot
            value = simbolo.obtenerValor()
            # Si es un string lo imprimimos
            if type(value) is str:
                print(value,end="")
            # Si no es un string lo transformamos en string antes de imprimirlo
            else:
                print(str(simbolo.obtenerValor()),end="")
        # READ            
        elif self.command == 'read':
            # Buscamos los datos actuales del bot
            simbolo = BotSymbolTable.buscarSimbolo("me")
            # Obtenemos la entrada del usuario
            stringElement = input("Value To Read " + "(" + simbolo.obtenerTipo()  + " type): ")
            # Convertimos esa entrada en un tipo primitivo
            element = obtainValueFromString(stringElement)
            # Caso 1: Se guardara en el bot
            if self.argument is None:
                pass
            # Caso 2: Se guardara en una variable
            else:
                # Buscamos si la variable existe
                simbolo = BotSymbolTable.buscarSimbolo(self.argument)
                # Se encontro la variable
                if simbolo != None:
                    pass
                # Variable no declarada, debe agregarse
                else:
                    simbolo = Simbolo(self.argument,None,None)
                    simbolo = simbolo.crearSimboloDeValor(element)
                    simbolo.activado = True
                    BotSymbolTable.agregarATabla(simbolo.obtenerIdentificador(),simbolo)
                
            # Actualizamos el valor del bot     
            BotSymbolTable.actualizarValorDeSimbolo(simbolo.obtenerIdentificador(),element)
        # LEFT            
        elif self.command == 'left':
            # Buscamos los datos actuales del bot
            simbolo = BotSymbolTable.buscarSimbolo("me")
            # Caso 1: Se movera 1 paso
            if self.argument is None:
                BotSymbolTable.actualizarPosicionHorSimbolo("me",simbolo.horPosicion - 1)
            # Caso 2: Se moveran varios pasos
            else:
                BotSymbolTable.actualizarPosicionHorSimbolo("me",simbolo.horPosicion - self.argument.evaluar(BotSymbolTable))
        # RIGHT            
        elif self.command == 'right':
            # Buscamos los datos actuales del bot
            simbolo = BotSymbolTable.buscarSimbolo("me")
            # Caso 1: Se movera 1 paso
            if self.argument is None:
                BotSymbolTable.actualizarPosicionHorSimbolo("me",simbolo.horPosicion + 1)
            # Caso 2: Se moveran varios pasos
            else:
                BotSymbolTable.actualizarPosicionHorSimbolo("me",simbolo.horPosicion + self.argument.evaluar(BotSymbolTable))
        # UP
        elif self.command == 'up':
            # Buscamos los datos actuales del bot
            simbolo = BotSymbolTable.buscarSimbolo("me")
            # Caso 1: Se movera 1 paso
            if self.argument is None:
                BotSymbolTable.actualizarPosicionVerSimbolo("me",simbolo.verPosicion + 1)
            # Caso 2: Se moveran varios pasos
            else:
                BotSymbolTable.actualizarPosicionVerSimbolo("me",simbolo.verPosicion + self.argument.evaluar(BotSymbolTable))
        # DOWN
        elif self.command == 'down':
            # Buscamos los datos actuales del bot
            simbolo = BotSymbolTable.buscarSimbolo("me")
            # Caso 1: Se movera 1 paso
            if self.argument is None:
                BotSymbolTable.actualizarPosicionVerSimbolo("me",simbolo.verPosicion - 1)
            # Caso 2: Se moveran varios pasos
            else:
                BotSymbolTable.actualizarPosicionVerSimbolo("me",simbolo.verPosicion - self.argument.evaluar(BotSymbolTable))

# Class ConditionalInstruccion      
class ConditionalInstruccion(InstruccionClass):
    def __init__(self,ifCondition,ifInstruccionSet,elseInstruccionSet=None):
        self.ifCondition = ifCondition
        self.ifInstruccionSet = ifInstruccionSet
        self.elseInstruccionSet = elseInstruccionSet    
    def __str__(self):
        retorno = ""
        retorno += "\n"
        retorno += "--------(ConditionalInstruccion)-------"
        retorno += "\n"
        retorno += "    CONDICIONAL"
        retorno += str(self.ifCondition)
        # Recorremos las instrucciones del if
        for instruction in self.ifInstruccionSet :
            retorno += str(instruction)
        # Si hay else, recorremos las instrucciones del else
        if self.elseInstruccionSet != None:
            for instruction in self.elseInstruccionSet :
                retorno += str(instruction)
        return retorno
    def run(self):
        """
        Corrida de la instruccion
        """
        # Caso 1: Se cumple la condicion del if
        if (self.ifCondition.evaluar(BotSymbolTable)):
            # recorremos y corremos las instrucciones
            for i in  range(0,self.ifInstruccionSet.len):
                self.ifInstruccionSet[i].run()
        # Caso 2: Si hay condicion de else y no se cumplio el if
        elif (self.elseInstruccionSet):
            # recorremos y corremos las instrucciones
            for i in  range(0,self.elseInstruccionSet.len):
                self.elseInstruccionSet[i].run()
        
# Class whileInstruccion
class whileInstruccion(InstruccionClass):

    def __init__(self,condition,instructionSet):
        self.condition = condition
        self.instructionSet = instructionSet
    def __str__(self):
        retorno = ""
        retorno += "\n"
        retorno += "--------(whileInstruccion)-------"
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
        
# Class ActivateInstruccion (REVISAR COMO HACER EL FOR PENDIENTE EN DONDE)
class ActivateInstruccion:
    def __init__(self,identList):
        self.identList = identList
    def __str__(self):
        espacio = "  "
        retorno = ""
        retorno += "\n"
        retorno += "--------(ActivateInstruccion)-------"
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
            # Buscamos los datos actuales del bot
            simbolo = BotSymbolTable.buscarSimbolo(self.identList[j])
            # Guardamos sus datos en variables globales
            currentBotType = simbolo.obtenerTipo()
            currentBotValue = simbolo.obtenerValor()
            currentBotHorPosicion = simbolo.horPosicion
            currentBotVerPosicion = simbolo.verPosicion
            # Creamos un nuevo nivel de tabla de simbolos
            BotSymbolTable = TablaDeSimbolos(deepcopy(BotSymbolTable))
            # Creamos un simbolo Me con los datos del bot actual
            symbolMe = Simbolo("me",currentBotType,currentBotValue)
            symbolMe.horPosicion = currentBotHorPosicion
            symbolMe.verPosicion = currentBotVerPosicion
            symbolMe.activado = True
            # Agregamos el simbolo a la tabla
            BotSymbolTable = BotSymbolTable.agregarATabla(symbolMe.obtenerIdentificador(),symbolMe)
            # Si el bot esta desactivado procedemos
            if simbolo.activado == False:
                # Marcamos el bot como activado
                BotSymbolTable.updateSymbolStatus(self.identList[j],True)
                # Buscamos el comportamiento correspondiente
                for behavior in simbolo.behaviorTable:
                    if behavior.condition == 'activation':
                        # Corremos las instrucciones del comportamiento
                        result = behavior.run()
                        # Si la operacion devuelve un resultado actualizamos el valor del bot
                        if result != None:
                            BotSymbolTable.actualizarValorDeSimbolo(self.identList[j],result.obtenerValor())
                            BotSymbolTable.actualizarPosicionHorSimbolo(self.identList[j],result.horPosicion)
                            BotSymbolTable.actualizarPosicionVerSimbolo(self.identList[j],result.verPosicion)
                        break
            # El Bot ya estaba activo, ERROR
            else:
                print("ERROR: " +self.identList[j]+ " ya se encontraba activo")
                exit()
        
# Class DeactivateInstruccion (REVISAR COMO HACER EL FOR PENDIENTE EN DONDE)
class DeactivateInstruccion:
    def __init__(self,identList):
        self.identList = identList
    def __str__(self):
        espacio = "  "
        retorno = ""
        retorno += "\n"
        retorno += "--------(DeactivateInstruccion)-------"
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
            # Buscamos los datos actuales del bot
            simbolo = BotSymbolTable.buscarSimbolo(self.identList[j])
            # Guardamos sus datos en variables globales
            currentBotType = simbolo.obtenerTipo()
            currentBotValue = simbolo.obtenerValor()
            currentBotHorPosicion = simbolo.horPosicion
            currentBotVerPosicion = simbolo.verPosicion
            # Creamos un nuevo nivel de tabla de simbolos
            BotSymbolTable = TablaDeSimbolos(deepcopy(BotSymbolTable))
            # Creamos un simbolo Me con los datos del bot actual
            symbolMe = Simbolo("me",currentBotType,currentBotValue)
            symbolMe.horPosicion = currentBotHorPosicion
            symbolMe.verPosicion = currentBotVerPosicion
            symbolMe.activado = False
            # Agregamos el simbolo a la tabla
            BotSymbolTable = BotSymbolTable.agregarATabla(symbolMe.obtenerIdentificador(),symbolMe)
            # Si el bot esta desactivado procedemos
            if simbolo.activado == True:
                # El Bot ya estaba activo, ERROR    
                BotSymbolTable.updateSymbolStatus(self.identList[j],False)
                # Buscamos el comportamiento correspondiente
                for behavior in simbolo.behaviorTable:
                    if behavior.condition == 'deactivation':
                        result = behavior.run()
                        # Si la operacion devuelve un resultado actualizamos el valor del bot
                        if result != None:
                            BotSymbolTable.actualizarValorDeSimbolo(self.identList[j],result.obtenerValor())
                            BotSymbolTable.actualizarPosicionHorSimbolo(self.identList[j],result.horPosicion)
                            BotSymbolTable.actualizarPosicionVerSimbolo(self.identList[j],result.verPosicion)
                        break

            else:
                print("ERROR: " +self.identList[j]+ " no se encontraba activo")
                exit()

# Class AdvanceInstruccion
class AdvanceInstruccion:
    def __init__(self,identList):
        self.identList = identList
    def __str__(self):
        espacio = "    "
        retorno = ""
        retorno += "\n"
        retorno += "--------(AdvanceInstruccion)-------"
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
            # Buscamos los datos actuales del bot
            simbolo = BotSymbolTable.buscarSimbolo(self.identList[j])
            # Guardamos sus datos en variables globales
            currentBotType = simbolo.obtenerTipo()
            currentBotValue = simbolo.obtenerValor()
            currentBotHorPosicion = simbolo.horPosicion
            currentBotVerPosicion = simbolo.verPosicion
            # Creamos un nuevo nivel de tabla de simbolos
            BotSymbolTable = TablaDeSimbolos(deepcopy(BotSymbolTable))
            # Creamos un simbolo Me con los datos del bot actual
            symbolMe = Simbolo("me",currentBotType,currentBotValue)
            symbolMe.horPosicion = currentBotHorPosicion
            symbolMe.verPosicion = currentBotVerPosicion
            symbolMe.activado = simbolo.activado
            # Agregamos el simbolo a la tabla
            BotSymbolTable = BotSymbolTable.agregarATabla(symbolMe.obtenerIdentificador(),symbolMe)
            # Inicializamos las variables referentes al comportamiento default
            defaultEnabled = True
            defaultPosicion = None
            # Si el bot esta activado procedemos
            if simbolo.activado == True:
                # Buscamos comportamientos personalizados
                for i in range(0,len(simbolo.behaviorTable)):
                    # Buscamos los comportamientos con expresiones
                    if (type(simbolo.behaviorTable[i].condition) is ExpresionParentizada or
                        type(simbolo.behaviorTable[i].condition) is ExpresionBooleana or
                        type(simbolo.behaviorTable[i].condition) is ExpresionRelacional):
                        # Si ya se ha encontrado default entonces hay un ERROR
                        if defaultPosicion != None:
                            print("ERROR: Default definido antes que comportamiento con expresion")
                            exit()
                        # Buscamos el primero que se cumpla
                        if simbolo.behaviorTable[i].condition.evaluar(BotSymbolTable) == True:
                            result = simbolo.behaviorTable[i].run()
                            # Si la operacion devuelve un resultado actualizamos el valor del bot
                            if result != None:
                                BotSymbolTable.actualizarValorDeSimbolo(self.identList[j],result.obtenerValor())
                                BotSymbolTable.actualizarPosicionHorSimbolo(self.identList[j],result.horPosicion)
                                BotSymbolTable.actualizarPosicionVerSimbolo(self.identList[j],result.verPosicion)
                            defaultEnabled = False
                            break
                    # Si encontramos el comportamiento default anotamos su posicion para compararla con la
                    # de los demas comportamientos
                    elif simbolo.behaviorTable[i].condition == 'default':
                        defaultPosicion = i
                # Si no se encontro ninguna condicion que se cumpla, utilizamos el comportamiento default
                if defaultEnabled: 
                    # Buscamos el comportamiento default
                    for behavior in simbolo.behaviorTable:
                        if behavior.condition == 'default':
                            result = behavior.run()
                            # Si la operacion devuelve un resultado actualizamos el valor del bot
                            if result != None:
                                BotSymbolTable.actualizarValorDeSimbolo(self.identList[j],result.obtenerValor())
                                BotSymbolTable.actualizarPosicionHorSimbolo(self.identList[j],result.horPosicion)
                                BotSymbolTable.actualizarPosicionVerSimbolo(self.identList[j],result.verPosicion)
                            break
            # El Bot no estaba activo, ERROR
            else:
                print("ERROR: " +self.identList[j]+ " no se encontraba activo")
                exit()  