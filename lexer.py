from enum import Enum

# inport custom files
from util import *

class TokenType(Enum):
  #EOF = 0
  #NEWLINE = 1
  
  IDENTIFIER = 2
  LIT_NUM = 3
  LIT_STR = 4
  
  KEYWORD = 5

class Token:
  def __init__(self, type, cont, pos):
    self.type = type
    self.cont = cont
    self.pos = pos
  
  def __repr__(self):
    return "Token(type: " + str(self.type) + ", cont: " + str(self.cont) + ", pos: " + str(self.pos) + ")"

def lex(l, line_n):
  tokens = []
  
  i = 0
  while i < len(l):
    # ignore spaces
    if l[i] == " ":
      i += 1
      continue
    
    # if the current character is a char or a dot
    elif is_digit(l[i]) or l[i] == ".":
      start = i
      n = ""
      
      while i < len(l) and (is_digit(l[i]) or l[i] == "."):
        n += l[i]
        i += 1
      
      try:
        num = float(n)
        
        tokens.append(Token(TokenType.LIT_NUM, num, start))
      except Exception:
        throw_error_noline(f"Invalid number literal: {n}")
    
    # if the current character is a letter
    elif is_letter(l[i]):
      start = i
      s = ""
      
      while i < len(l) and is_letter(l[i]):
        s += l[i]
        i += 1
      
      tokens.append(Token(TokenType.IDENTIFIER, s, start))
    
    # Quotes
    elif l[i] == "\"" or l[i] == "'":
      start = i
      s = ""
      
      while i < len(l) and (l[i] != "\"" or l[i] != "'"):
        s += l[i]
        i += 1
      
      tokens.append(Token(TokenType.LIT_STR, s, start))
    # Unknown
    else:
      throw_error_noline(f"Invalid token: '{l[i]}' at position {i + 1} in line {line_n + 1}")
  i += 1
  
  return tokens