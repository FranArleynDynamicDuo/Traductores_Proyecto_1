'''
Created on 22 de sept. de 2015

@author: francisco
'''

import ply.lex as lex

def tokenization(word):
    
    tokens = ('QUOTE', 'SIMB', 'NUM', 'LPAREN', 'RPAREN', 'NIL', 'TRUE', 'FALSE', 'TEXT')
    
    
    # Los tokens relevantes serán:
    
    #===========================================================================
    #  Cada una de las palabras claves utilizadas en la sintaxis de BOT, i.e. 
    # create, while, bool, if,etc. En este caso, los tokens deberán llamarse 
    # TkhPalabra Clavei, donde hPalabra Clavei es
    # la palabra clave a la que representa el token, con su primera letra en 
    # mayúscula. Por ejemplo, para la palabra clave create, su token 
    # sería TkCreate.
    #===========================================================================
    
    #===========================================================================
    #  Los identicadores de variables. A diferencia de las palabras claves, 
    # los identicadores corresponderan a un único token llamado TkIdent. 
    # Este token siempre tendrá asociado como atributo el identicador particular
    # reconocido. Por ejemplo, al leer contador, se dará como
    # salida TkIdent("contador").
    #===========================================================================
    
    #===========================================================================
    #  Los literales numéricos, los cuales serán secuencias no-vacías de 
    # dígitos decimales. De manera análoga a los identicadores, éstos serán
    # agrupados bajo el token TkNum. Este token tendrá
    # como atributo el número reconocido, por ejemplo TkNum(3000).
    #===========================================================================
    
    #===========================================================================
    #  Los literales booleanos, los cuales a diferencia de los literales 
    # numéricos, estarán representados
    # por dos tokens. Uno de ellos para true (TkTrue) y otro para false (TkFalse).
    #===========================================================================
    
    #===========================================================================
    #  Los literales para caracteres, los cuales estarán envueltos en comillas simples. De manera
    # análoga a los identicadores y los literales numéricos, éstos serán agrupados bajo el token
    # TkCaracter. Este token tendrá como atributo el caracter reconocido, por ejemplo TkCaracter('p').
    #===========================================================================
   



    #===============================================================================
    # Los espacios en blanco, tabuladores y saltos de línea deben ser ignorados. Así
    # mismo, los comentarios no deben ser reconocidos como tokens, sino ser 
    # ignorados igualmente. Cualquier otro caracter será
    # reportado como error. 
    #===============================================================================
    
    if (word == "Create"):
        return "TkCreate"
       
    #===============================================================================
    # Cada uno de los símbolos que denotan separadores en BOT, los cuales se 
    # presentan a continuación:
    #   
    # "," 􀀀 TkComa
    # "." 􀀀 TkPunto
    # ":" 􀀀 TkDosPuntos
    # "(" 􀀀 TkParAbre
    # ")" 􀀀 TkParCierra
    #===============================================================================

        
    elif(word == ","):
        return "TkComa"

    elif(word == "."):
        return "TkPunto"
    
    elif(word == ":"):
        return "TkDosPuntos"
    
    elif(word == "("):
        return "TkParAbre"
    
    elif(word == ")"):
        return "TkParCierra"
    
    
    #===============================================================================
    #  Cada uno de los símbolos que denotan a operadores aritméticos, booleanos, 
    # relacionales, o de otro tipo en BOT, los cuales se presentan a continuación:
    # "+" 􀀀 TkSuma
    # "-" 􀀀 TkResta
    # "*" 􀀀 TkMult
    # "/" 􀀀 TkDiv
    # "%" 􀀀 TkMod
    # "/\" 􀀀 TkConjuncion
    # "\/" 􀀀 TkDisyuncion
    # "" 􀀀 TkNegacion
    # "<" 􀀀 TkMenor
    # "<=" 􀀀 TkMenorIgual
    # ">" 􀀀 TkMayor
    # ">=" 􀀀 TkMayorIgual
    # "=" 􀀀 TkIgual
    #===============================================================================
    
    elif(word == "+"):
        return "TkSuma"

    elif(word == "."):
        return "TkResta"
    
    elif(word == "*"):
        return "TkMult"
    
    elif(word == "/"):
        return "TkDiv"
    
    elif(word == "%"):
        return "TkMod"
    
    # elif(word == "/\"):
    #    return "TkConjuncion"
    
    elif(word == "\/"):
        return "TkDisyuncion"
    
    elif(word == "~"):
        return "TkNegacion"
    
    elif(word == "<"):
        return "TkMenor"
    
    elif(word == "<="):
        return "TkMenorIgual"
    
    elif(word == ">"):
        return "TkMayor"
    
    elif(word == ">="):
        return "TkMayorIgual"
    
    elif(word == "="):
        return "TkIgual"
    
    else:
        pass
    
    pass