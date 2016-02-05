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
