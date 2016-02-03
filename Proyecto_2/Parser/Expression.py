'''
Created on Feb 1, 2016

@author: francisco
'''


from abc import ABCMeta, abstractmethod
    
class Expresion(metaclass=ABCMeta):
    '''
    classdocs
    '''

    @abstractmethod
    def __init__(self, params):
        '''
        Constructor
        '''

class ArithmethicOperation(Expresion):
    '''
    classdocs
    '''

    @abstractmethod
    def __init__(self, params):
        '''
        Constructor
 
        '''
        
class RelationalOperation(Expresion):
    '''
    classdocs
    '''

    @abstractmethod
    def __init__(self, params):
        '''
        Constructor
 
        '''
        
class BooleanOperation(Expresion):
    '''
    classdocs
    '''

    @abstractmethod
    def __init__(self, params):
        '''
        Constructor
 
        '''