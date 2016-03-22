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
        pass
        
        
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
        pass

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
            if instruction != None:
                retorno +=espacio + espacio + espacio + espacio + str(instruction)
                retorno += "\n"
        return retorno
 
    # Corrida de la instruccion
    def run(self):
        pass 

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

    # Corrida de la instruccion
    def run(self):
        pass

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
        if (self.ifCondition.evaluar()):
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
        while (self.condition.evaluar()):
            for i in  range(0,self.instructionSet.len):
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
        pass 
        
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
        pass
 
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
        pass       