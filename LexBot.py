'''
Created on 23 de sept. de 2015

@author: francisco
'''

if __name__ == '__main__':
    pass

##################### Imports ##################################################

import sys

from Proyecto_1.Lexer.Lexer import botLexer
from Proyecto_1.Lexer.Lexer import column_token
from Proyecto_1.Lexer.Token import Token
from Proyecto_2.Parser.parser import BotParser


##################### Funciones ################################################
# Calculo de columna en la que se encuentra el numero de columna
def find_column(data,token):
    last_cr = data.rfind('\n',0,token.lexpos)
    if last_cr < 0:
        last_cr = 0
    column = (token.lexpos - last_cr) + 1
    return column

##################### Codigo Principal #########################################

# Abrimos el archivo y lo leemos
bot_Script = open(sys.argv[1],'r')

data = bot_Script.read()


# Pasamos nuestra informacion al lexer
botLexer.input(data)

# Creamos una lista para almacenar los tokens
token_List = []

# Inicializamos nuestro iterador
i = 0

# Print por detalles esteticos
print(" ")

# Creamos los objetos token necesarios
while True:
    
    # Tomamos el siguiente token
    tok = botLexer.token()
    
    # Verificamos que no llegamos el final del conjunto de tokens
    if not tok: 
        break
    
    # Agregamos a la lista un token nuevo
    token_List.append(Token(tok.type,tok.value,
                            tok.lineno,column_token(data,tok)))

# Reiniciamos el iterador
i = 0

if botLexer.error_Found == False:

    # 2DO CICLO: Si no se encuentran errores, se imprimen las tokens correctas
    while i < len(token_List):
        
        # Si el token requiere mostrar un dato adicional utilizamos un formato
        if token_List[i].type == 'TkNum' or token_List[i].type == 'TkIdent':
            
            print ('%s("%s") %s %s' % (token_List[i].type,token_List[i].value,
                                       token_List[i].line_Number,token_List[i].column_Number),end=" ")
            
        # En caso de no necesitarlo, usamos un formato con 3 parametros
        else:
        
            print ('%s %s %s' % (token_List[i].type,token_List[i].line_Number,
                   token_List[i].column_Number),end=" ")
        
        # Aumentamos el iterador
        i += 1


print("\n")
# Pasamos nuestra informacion al lexer
botLexer.input(data)
bot_Script.close()

# Abrimos el archivo y lo leemos
bot_Script = open(sys.argv[1],'r')

data = bot_Script.read()

# DEBUG
result = BotParser.parse(data,debug=1)

# # Pasamos nuestra informacion al lexer
# result = BotParser.parse(data)

# NO estamos claros si hay que usarlo
print(result) 

result.