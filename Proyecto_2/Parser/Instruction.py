'''
Created on Feb 1, 2016

@author: francisco
'''


from abc import ABCMeta, abstractmethod
    
def spacing(espacio):
        i = 0
        while (i < 4):
            espacio += " " 
            i += 1
        return espacio
        
class InstructionClass(metaclass=ABCMeta):
    '''
    classdocs
    '''

    @abstractmethod
    def __init__(self, params):
        '''
        Constructor
        '''
class Program(InstructionClass):
    '''
    classdocs
    '''

    @abstractmethod
    def __init__(self, executeSet,createSet=None ):
        '''
        Constructor
 
        '''
        self.createSet = createSet
        self.executeSet = executeSet
        
class CodeBlock(InstructionClass):
    '''
    classdocs
    '''

    @abstractmethod
    def __init__(self, blockType,instructionSet ):
        self.blockType = blockType
        self.instructionSet = instructionSet
        
# Clase Crear el LexBot 
class CreateInstruction(InstructionClass):
    @abstractmethod
    def __init__(self, botType,identifier,declarationSet ):
        self.botType = botType
        self.identifier = identifier
        self.declarationSet = declarationSet    
        self.imprimir("")
        
    def imprimir(self,espacio):
        print(espacio, "CREAR BOT")
        print(espacio,espacio," - Tipo: ", self.botType)
        print(espacio,espacio," - Nombre: ", self.identifier)


# Clase Declaracion del bot
class BotDeclaration(InstructionClass):
    
    @abstractmethod
    def __init__(self,condition,instructionSet ):
        self.condition = condition
        self.instructionSet = instructionSet
        self.imprimir("")
        
    def imprimir(self,espacio):
        if (self.condition == "activation"):
            print(espacio,"ACTIVACION")
        elif (self.condition == "deactivation"):
            print(espacio,"DESACTIVACION")
        elif (self.condition == "default"):
            print(espacio,"DEFAULT")
        
        
# Clase Intrucciones del boot
class BotInstruction(InstructionClass):

    @abstractmethod
    def __init__(self, command,argument=None):
        self.command = command
        self.argument = argument
        self.imprimir("")
        
    def imprimir(self,espacio):
        
        if (self.argument == None):
            if (self.command == "store"):
                print(espacio,espacio," - instruccion: almacenamiento")
            elif (self.command == "collect"):
                print(espacio,espacio," - instruccion: coleccion")
            elif (self.command == "recieve"):
                print(espacio,espacio," - instruccion: lectura") 
            elif (self.command == "drop"):
                print(espacio,espacio," - instruccion: soltado")
                 
            print(espacio,espacio," - valor: ",self.argument)


        elif (self.argument == None):
        
            if (self.command == "send"):
                print(espacio,espacio," - instruccion: enviar")
            elif (self.command == "read"):
                print(espacio,espacio," - instruccion: leer")
            elif (self.command == "left"):
                print(espacio,espacio," - instruccion: movimiento hacia la izquierda")
            elif (self.command == "right"):
                print(espacio,espacio," - instruccion: movimiento hacia la derecha")
            elif (self.command == "up"):
                print(espacio,espacio," - instruccion: movimiento hacia arriba")
            elif (self.command == "down"):
                print(espacio,espacio," - instruccion: movimiento hacia abajo")
  

# Class ConditionalInstruction      
class ConditionalInstruction(InstructionClass):

    @abstractmethod
    def __init__(self,ifCondition,ifInstructionSet,elseInstructionSet=None):
        self.ifCondition = ifCondition
        self.ifInstructionSet = ifInstructionSet
        self.elseInstructionSet = elseInstructionSet    
        self.imprimir("")
        
    def imprimir(self,espacio):
        print(espacio,"CONDICIONAL")
        
        
# Class whileInstruction
class whileInstruction(InstructionClass):

    @abstractmethod
    def __init__(self, condition,instructionSet):
        self.condition = condition
        self.instructionSet = instructionSet
        
        self.imprimir("")
        
    def imprimir(self,espacio):
        print(espacio,"ITERACION INDETERMINADA")
        
        
# Class ActivateInstruction (REVISAR COMO HACER EL FOR PENDIENTE EN DONDE)
class ActivateInstruction:
    
    def __init__(self,identList):
        self.identList = identList
        self.imprimir("")
        
    def imprimir(self,espacio):
        print(espacio,espacio,"ACTIVACION")

        for nameBot in self.identList :
            print(espacio,espacio,espacio," - var: ", nameBot)
        
        
# Class DeactivateInstruction (REVISAR COMO HACER EL FOR PENDIENTE EN DONDE)
class DeactivateInstruction:
    
    def __init__(self,identList):
        self.identList = identList
        self.imprimir("")
        
    def imprimir(self,espacio):
        print(espacio,espacio,"DESACTIVACION")

        for nameBot in self.identList :
            print(espacio,espacio,espacio," - var: ", nameBot)
    
 
# Class AdvanceInstruction
class AdvanceInstruction:

    def __init__(self,identList):
        self.identList = identList
        self.imprimir("")
        
    def imprimir(self,espacio):
        print(espacio,espacio,"AVANCE")

        for nameBot in self.identList :
            print(espacio,espacio,espacio," - var: ", nameBot)
        
