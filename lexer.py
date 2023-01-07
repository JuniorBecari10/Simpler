from enum import Enum

# inport custom files
import util

class TokenType(Enum):
  EOF = 0
  NEWLINE = 1
  
  IDENTIFIER = 2
  LITERAL_NUM = 3
  LITERAL_STR = 4
  
  KEYWORD = 5

class Token:
  def __init__(self, type, cont):
    self.type = type
    self.cont = cont

def lex(lines):
  tokens = []
  
  for l in lines:
    for i, c in enumerate(l):
      
  
  return tokens