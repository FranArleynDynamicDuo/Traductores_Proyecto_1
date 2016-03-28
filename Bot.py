'''
Created on 23 de sept. de 2015

@author: francisco
'''

if __name__ == '__main__':
    pass

##################### Imports ##################################################

import sys

from AnalisisLexicografico.Lexer.Lexer import botLexer
from AnalisisLexicografico.Lexer.Lexer import column_token
from AnalisisLexicografico.Lexer.Token import Token
from AnalisisSintactico.Parser.parser import BotParser
from AnalisisContexto.TablaDeSimbolos import TablaDeSimbolos
from re import compile
from re import match

##################### Funciones ################################################
# Calculo de columna en la que se encuentra el numero de columna
def find_column(data,token):
    last_cr = data.rfind('\n',0,token.lexpos)
    if last_cr < 0:
        last_cr = 0
    column = (token.lexpos - last_cr) + 1
    return column

##################### Codigo Principal #########################################

# Verificamos que nuestro archivo es de extension .bot
botPattern = compile(r'([a-zA-Z][a-zA-Z0-9_]*)\.bot')
if not (match(botPattern, sys.argv[1])):
    print("Este no es un archivo .bot")
    exit()

# Abrimos el archivo y lo leemos
bot_Script = open(sys.argv[1],'r')

data = bot_Script.read()


# Pasamos nuestra informacion al lexer
botLexer.input(data)

# Creamos una lista para almacenar los tokens
token_List = []

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


# Pasamos nuestra informacion al lexer
botLexer.input(data)
bot_Script.close()

if botLexer.error_Found == True:
    print("Errores en el lexer")
    exit()

# Abrimos el archivo y lo leemos
bot_Script = open(sys.argv[1],'r')

data = bot_Script.read()
# 
# # DEBUG
# result = BotParser.parse(data,debug=1)
# 
parseTree = BotParser.parse(data)

runBotSymbolTable = TablaDeSimbolos(None)

parseTree.run()

print("")

# NO estamos claros si hay que usarlo
# print(result) 
