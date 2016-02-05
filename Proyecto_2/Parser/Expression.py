'''
Created on Feb 1, 2016

@author: francisco
'''


from abc import ABCMeta, abstractmethod
    
class Expresion(metaclass=ABCMeta):
    '''
    classdocs
    '''

class ArithmethicExpression(Expresion):
    '''
    classdocs
    '''

    @abstractmethod
    def __init__(self, expresion1,operador=None,expresion2=None):
        '''
        Constructor
        '''
        self.expresion1 = expresion1
        self.expresion1 = operador
        self.expresion2 = expresion2
        
class RelationalExpresion(Expresion):
    '''
    classdocs
    '''

    @abstractmethod
    def __init__(self, expresion1,operador=None,expresion2=None):
        '''
        Constructor
        '''
        self.expresion1 = expresion1
        self.expresion1 = operador
        self.expresion2 = expresion2
        
class BooleanExpression(Expresion):
    '''
    classdocs
    '''

    @abstractmethod
    def __init__(self, expresion1,operador=None,expresion2=None):
        '''
        Constructor
        '''
        self.expresion1 = expresion1
        self.expresion1 = operador
        self.expresion2 = expresion2