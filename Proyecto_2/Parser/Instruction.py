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
    @abstractmethod
    def __init__(self, params):
        pass
    
class Program(InstructionClass):
    
    def __init__(self, executeSet,createSet=None ):
        self.createSet = createSet
        self.executeSet = executeSet
        
    def __str__(self):
        retorno = ""
        retorno += "--------(Program)-------"
        retorno += "\n"
        retorno += "PROGRAM"
        retorno += "\n"
        if self.createSet != None:
            for create in self.createSet :
                retorno += str(create)
        for execute in self.executeSet :
            retorno += str(execute)
        return retorno
        
        
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
            retorno += espacio + espacio + " - Nombre: " +  str(declarion);
            retorno += "\n"
        return retorno


# Clase Declaracion del bot
class BotDeclaration(InstructionClass):
    
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
            retorno +=espacio + espacio + espacio + espacio + str(instruction)
            retorno += "\n"
        return retorno
        
# Clase Intrucciones del boot
class BotInstruction(InstructionClass):

    def __init__(self, command,argument=None):
        self.command = command
        self.argument = argument
        #
        
    def imprimir(self,espacio):
        
        #if (self.argument != None):
        #    if (self.command == "store"):
        #        print(espacio,espacio," - instruccion: almacenamiento")
        #    elif (self.command == "collect"):
        #        print(espacio,espacio," - instruccion: coleccion")
        #    elif (self.command == "recieve"):
        #        print(espacio,espacio," - instruccion: lectura") 
        #    elif (self.command == "drop"):
        #        print(espacio,espacio," - instruccion: soltado")
                 
        #    print(espacio,espacio," - valor: ",self.argument)
        #elif (self.argument == None):
        #
        #    if (self.command == "send"):
        #        print(espacio,espacio," - instruccion: enviar")
        #    elif (self.command == "read"):
        #        print(espacio,espacio," - instruccion: leer")
        #    elif (self.command == "left"):
        #        print(espacio,espacio," - instruccion: movimiento hacia la izquierda")
        #    elif (self.command == "right"):
        #        print(espacio,espacio," - instruccion: movimiento hacia la derecha")
        #    elif (self.command == "up"):
        #        print(espacio,espacio," - instruccion: movimiento hacia arriba")
        #    elif (self.command == "down"):
        #        print(espacio,espacio," - instruccion: movimiento hacia abajo")
        pass

# Class ConditionalInstruction      
class ConditionalInstruction(InstructionClass):

    def __init__(self,ifCondition,ifInstructionSet,elseInstructionSet=None):
        self.ifCondition = ifCondition
        self.ifInstructionSet = ifInstructionSet
        self.elseInstructionSet = elseInstructionSet    
        #
        
    def imprimir(self,espacio):
        print("--------(ConditionalInstruction)-------")
        print(espacio,"CONDICIONAL")

        
# Class whileInstruction
class whileInstruction(InstructionClass):

    def __init__(self, condition,instructionSet):
        self.condition = condition
        self.instructionSet = instructionSet
        
        #
        
    def imprimir(self,espacio):
        print("--------(whileInstruction)-------")
        print(espacio,"ITERACION INDETERMINADA")
        
        
# Class ActivateInstruction (REVISAR COMO HACER EL FOR PENDIENTE EN DONDE)
class ActivateInstruction:
    
    def __init__(self,identList):
        self.identList = identList
        

    def __str__(self):
        retorno = ""
        retorno += "--------(ActivateInstruction)-------"
        retorno += "\n"
        retorno += "ACTIVACION"
        retorno += "\n"
        for nameBot in self.identList :
            print("","",""," - var: ", nameBot)
        return retorno
        
    def imprimir(self,espacio):
        print("--------(ActivateInstruction)-------")
        print(espacio,espacio,"ACTIVACION")

        for nameBot in self.identList :
            print(espacio,espacio,espacio," - var: ", nameBot)
        
        
# Class DeactivateInstruction (REVISAR COMO HACER EL FOR PENDIENTE EN DONDE)
class DeactivateInstruction:
    
    def __init__(self,identList):
        self.identList = identList
        
    def __str__(self):
        retorno = ""
        retorno += "--------(DeactivateInstruction)-------"
        retorno += "\n"
        retorno += "DESACTIVACION"
        retorno += "\n"
        for nameBot in self.identList :
            print("","",""," - var: ", nameBot)
        return retorno
            
    def imprimir(self,espacio):
        print("--------(DeactivateInstruction)-------")
        print(espacio,espacio,"DESACTIVACION")

        for nameBot in self.identList :
            print(espacio,espacio,espacio," - var: ", nameBot)
    
 
# Class AdvanceInstruction
class AdvanceInstruction:

    def __init__(self,identList):
        self.identList = identList
    
    def __str__(self):
        retorno = ""
        retorno += "--------(AdvanceInstruction)-------"
        retorno += "\n"
        retorno += "AVANCE"
        retorno += "\n"
        for nameBot in self.identList :
            print("","",""," - var: ", nameBot)
        return retorno
    
        
    def imprimir(self,espacio):
        
        print("--------(AdvanceInstruction)-------")
        print(espacio,espacio,"AVANCE")

        for nameBot in self.identList :
            print(espacio,espacio,espacio," - var: ", nameBot)
        
        