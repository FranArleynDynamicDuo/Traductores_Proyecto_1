'''
Created on 23 de sept. de 2015

@author: francisco
'''

class Token(object):
    
    '''
    Clase base de los tokens con sus atributos basicos
    '''

    def __init__(self ,name,value,line_Number,column_Number):
        '''
        Constructor
        '''
        self.name = name
        self.value = value
        self.line_Number = line_Number
        self.column_Number = column_Number