from enum import Enum

from lexer import TokenType
from util import *

class NodeType(Enum):
  VAR_DECL = 0
  PRINT_STAT = 1

class ParseNode:
  def __init__(self, type, tokens):
    self.type = type
    self.tokens = tokens
  
  def __repr__(self):
    return "ParseNode(type: " + str(self.type) + ", tokens: " + str(self.tokens) + ")"

def parse(tokens, line_n):
  # variable declaration
  if len(tokens) >= 2 and tokens[0].type == TokenType.IDENTIFIER and tokens[1].type == TokenType.EQUALS:
    return ParseNode(NodeType.VAR_DECL, tokens)
  
  elif len(tokens) >= 1 and tokens[0].type == TokenType.KEYWORD and tokens[0].cont == "print":
    return ParseNode(NodeType.PRINT_STAT, tokens)
  
  # Unknown
  else:
    throw_error(f"Unknown statement.", line_n + 1)

# Grammar:
#
# VAR_DECL: <IDENTIFIER> = <...>
# PRINT_STAT: <KEYWORD: print> <...>