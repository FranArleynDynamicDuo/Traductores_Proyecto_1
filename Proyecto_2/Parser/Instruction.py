'''
Created on Feb 1, 2016

@author: francisco
'''


from abc import ABCMeta, abstractmethod
    
class Instruction(metaclass=ABCMeta):
    '''
    classdocs
    '''

    @abstractmethod
    def __init__(self, params):
        '''
        Constructor
        '''
class Program(Instruction):
    '''
    classdocs
    '''

    @abstractmethod
    def __init__(self, instructionSet ):
        '''
        Constructor
 
        '''
        self.instructionSet = instructionSet
        
class CodeBlock(Instruction):
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
        
class CreateInstruction(Instruction):
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

class BotDeclaration(Instruction):
    '''
    classdocs
    '''

    @abstractmethod
    def __init__(self, condition,identifier,instructionSet ):
        '''
        Constructor
 
        '''
        self.condition = condition
        self.instructionSet = instructionSet
        
class BotDecInstruction(Instruction):
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
        
class ConditionalInstruction(Instruction):
    '''
    classdocs
    '''

    @abstractmethod
    def __init__(self, conditionalInstructiontype,condition,instructionSet ):
        '''
        Constructor
 
        '''
        self.conditionalInstructiontype = conditionalInstructiontype
        self.condition = condition
        self.instructionSet = instructionSet
        
class whileInstruction(Instruction):
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

class ActivateInstruction(Instruction):
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
        
class ExecuteInstruction(Instruction):
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


