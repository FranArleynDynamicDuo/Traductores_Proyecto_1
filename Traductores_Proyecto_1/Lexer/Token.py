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
        self.type = type
        self.value = value
        self.line_Number = line_Number
        self.column_Number = column_Number
        
class Token_One_Atribute(Token):
    '''
    SubClase de token, que corresponde a los tokens que tienen 1 datos adicional
    asociado como en el caso de los identificadores o los TkNum(x)
    '''
    def __init__(self ,type,value,line_Number,column_Number,extra_Atribute):
        '''
        Constructor
        '''
        self.name = type
        self.value = value
        self.line_Number = line_Number
        self.column_Number = column_Number
        self.extra_Atribute = extra_Atribute
        