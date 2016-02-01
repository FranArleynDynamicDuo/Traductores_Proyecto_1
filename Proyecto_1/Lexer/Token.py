'''
Created on 23 de sept. de 2015

@author: francisco
'''

class Token(object):
    
    '''
    Clase base de los tokens con sus atributos basicos
    '''

    def __init__(self ,type,value,line_Number,column_Number):
        '''
        Constructor
        '''
        self.type = type                     # Tipo de token
        self.value = value                   # Valor de la palabra que se leyo
        self.line_Number = line_Number       # Numero de linea
        self.column_Number = column_Number   # Numero de columna