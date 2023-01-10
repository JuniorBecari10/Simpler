from enum import Enum

# inport custom files
from util import *

keywords = [
  "print",
  "printl",
  "input",
  "if",
  "exit",
  "goto"
]

types = [
  "num",
  "str"
]

class TokenType(Enum):
  #EOF = 0
  NEWLINE = 0
  
  IDENTIFIER = 1
  LIT_NUM = 2
  LIT_STR = 3
  
  KEYWORD = 4
  TYPE = 5
  
  PLUS = 6
  MINUS = 7
  TIMES = 8
  DIVIDE = 9
  
  LPAREN = 10
  RPAREN = 11
  
  ASSIGN = 12
  LABEL = 13
  
  EQUALS = 15
  DIFF = 16
  
  GREATER = 17
  GREATER_EQ = 18
  
  LESS = 19
  LESS_EQ = 20

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
    if l[i] == " " or l[i] == ":":
      i += 1
      continue
    
    # if the current character is a digit or a dot
    elif is_digit(l[i]) or l[i] == ".":
      start = i
      n = ""
      
      # While it's a digit or dot, continue looping
      while i < len(l) and (is_digit(l[i]) or l[i] == "."):
        n += l[i]
        i += 1
      
      # Convert to number and add to the tokens list
      try:
        num = float(n)
        
        tokens.append(Token(TokenType.LIT_NUM, num, start))
      except Exception:
        throw_error_noline(f"Invalid number literal: {n}")
    
    # if the current character is a letter
    elif is_letter(l[i]):
      start = i
      s = ""
      
      # While it's a letter continue looping
      while i < len(l) and is_letter(l[i]):
        s += l[i]
        i += 1
      
      # if it's a keyword
      if s in keywords:
        tokens.append(Token(TokenType.KEYWORD, s, start))
        i += 1
        continue
      
      # if it's a type
      if s in types:
        tokens.append(Token(TokenType.TYPE, s, start))
        i += 1
        continue
      
      # if it's a label
      if start > 0 and l[start - 1] == ":":
        tokens.append(Token(TokenType.LABEL, s, start - 1))
        i += 1
        continue
      
      # else, it's a identifier
      tokens.append(Token(TokenType.IDENTIFIER, s, start))
    
    # detect quotes
    elif l[i] == "\"":
      start = i
      s = ""
      
      i += 1
      
      # While there's not another quote, we're still inside them
      while i < len(l) and (l[i] != "\""):
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
      if i < len(l) and l[i + 1] == "=":
        tokens.append(Token(TokenType.EQUALS, l[i:i+2], i))
        i += 2
        continue
      
      tokens.append(Token(TokenType.ASSIGN, l[i], i))
      i += 1
    
    # Unknown; invalid
    else:
      throw_error(f"Invalid token: '{l}' at position {i + 1}", line_n + 1, "                " + (" " * i) + "^" + "\n" + ("We don't use '$' anymore to reference a variable.\n\nExample:\na = 10\nprint a" if l[i] == "$" else ""))
  
  # New line; equivalent to semicolon (;) in C.
  tokens.append(Token(TokenType.NEWLINE, "", len(l)))
  
  return tokens