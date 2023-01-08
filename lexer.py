from enum import Enum

# inport custom files
from util import *

keywords = [
  "print"
]

class TokenType(Enum):
  #EOF = 0
  #NEWLINE = 1
  
  IDENTIFIER = 0
  LIT_NUM = 1
  LIT_STR = 2
  
  KEYWORD = 3
  
  PLUS = 4
  MINUS = 5
  TIMES = 6
  DIVIDE = 7
  
  LPAREN = 8
  RPAREN = 9
  
  ASSIGN = 10

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
      
      if s in keywords:
        tokens.append(Token(TokenType.KEYWORD, s, start))
        i += 1
        continue
      
      tokens.append(Token(TokenType.IDENTIFIER, s, start))
    
    # detect quotes
    elif l[i] == "\"" or l[i] == "'":
      start = i
      s = ""
      
      i += 1
      
      while i < len(l) and (l[i] != "\"" and l[i] != "'"):
        s += l[i]
        i += 1
      
      i += 1
      
      tokens.append(Token(TokenType.LIT_STR, s, start))
    
    # Operators
    elif l[i] == "+":
      tokens.append(Token(TokenType.PLUS, l[i], i))
      i += 1
    elif l[i] == "-":
      tokens.append(Token(TokenType.MINUS, l[i], i))
      i += 1
    elif l[i] == "*":
      tokens.append(Token(TokenType.TIMES, l[i], i))
      i += 1
    elif l[i] == "/":
      tokens.append(Token(TokenType.DIVIDE, l[i], i))
      i += 1
    
    # Parenthesis
    elif l[i] == "(":
      tokens.append(Token(TokenType.LPAREN, l[i], i))
      i += 1
    elif l[i] == ")":
      tokens.append(Token(TokenType.RPAREN, l[i], i))
      i += 1
    
    # Assignment
    elif l[i] == "=":
      tokens.append(Token(TokenType.ASSIGN, l[i], i))
      i += 1
    
    # Unknown
    else:
      throw_error(f"Invalid token: '{l}' at position {i + 1}", line_n + 1, "                " + (" " * i) + "^" + "\n" + ("We don't use '$' anymore to reference a variable.\n\nExample:\na = 10\nprint a" if l[i] == "$" else ""))
  
  return tokens