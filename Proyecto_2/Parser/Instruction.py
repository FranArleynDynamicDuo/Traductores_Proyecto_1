'''
Created on Feb 1, 2016

@author: francisco
'''


from abc import ABCMeta, abstractmethod
    
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
    def __init__(self, createSet=None,executeSet ):
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
        '''
        Constructor
 
        '''
        self.blockType = blockType
        self.instructionSet = instructionSet
        
class CreateInstruction(InstructionClass):
    '''
    classdocs
    '''

    @abstractmethod
    def __init__(self, botType,identifier,declarationSet ):
        '''
        Constructor
 
        '''
        self.botType = botType
        self.identifier = identifier
        self.declarationSet = declarationSet    

class BotDeclaration(InstructionClass):
    '''
    classdocs
    '''

    @abstractmethod
    def __init__(self, condition,instructionSet ):
        '''
        Constructor
 
        '''
        self.condition = condition
        self.instructionSet = instructionSet
        
class BotDecInstruction(InstructionClass):
    '''
    classdocs
    '''

    @abstractmethod
    def __init__(self, commands,argument,instructionSet):
        '''
        Constructor
 
        '''
        self.commands = commands
        self.argument = argument
        self.instructionSet = instructionSet
        
class ConditionalInstruction(InstructionClass):
    '''
    classdocs
    '''

    @abstractmethod
    def __init__(self,ifCondition=True,ifInstructionSet,elseInstructionSet=None):
        '''
        Constructor
 
        '''
        self.ifCondition = ifCondition
        self.ifInstructionSet = ifInstructionSet
        self.elseInstructionSet = elseInstructionSet        
        
class whileInstruction(InstructionClass):
    '''
    classdocs
    '''

    @abstractmethod
    def __init__(self, condition,instructionSet):
        '''
        Constructor
 
        '''
        self.condition = condition
        self.instructionSet = instructionSet

class ActivateInstruction(InstructionClass):
    '''
    classdocs
    '''

    @abstractmethod
    def __init__(self, identList):
        '''
        Constructor
 
        '''
        self.identList = identList

class DeactivateInstruction(InstructionClass):
    '''
    classdocs
    '''

    @abstractmethod
    def __init__(self, identList):
        '''
        Constructor
 
        '''
        self.identList = identList
    
 
class AdvanceInstruction(InstructionClass):
    '''
    classdocs
    '''

    @abstractmethod
    def __init__(self, identList):
        '''
        Constructor
 
        '''
        self.identList = identList

class BotInstruction(InstructionClass):
    '''
    classdocs
    '''

    @abstractmethod
    def __init__(self, command,argument=None):
        '''
        Constructor
 
        '''
        self.identList = command
        self.identList = argument

