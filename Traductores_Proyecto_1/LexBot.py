'''
Created on 23 de sept. de 2015

@author: francisco
'''

if __name__ == '__main__':
    pass

import sys
import ply.lex as lex
import Lexer.Lexer

lexer = lex.lex()
inFile = sys.argv[1]

# Test it out
data = '''

3 + 4 * 10
  
  + -20 *2
      -
          cosa
'''



# Give the lexer some input
lexer.input(data)

# Tokenize
while True:
    tok = lexer.token()
    if not tok: 
        break      # No more input
    print(tok)
