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
    def __init__(self, params):
        '''
        Constructor
 
        '''
        
class LoopInstruction(Instruction):
    '''
    classdocs
    '''

    @abstractmethod
    def __init__(self, params):
        '''
        Constructor
 
        '''