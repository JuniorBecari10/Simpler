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
  if len(tokens) >= 2 and tokens[0].type == TokenType.IDENTIFIER and tokens[1].type == TokenType.EQUALS:
    return ParseNode(NodeType.VAR_DECL, tokens)


# Grammar:
#
# VAR_DECL: <IDENTIFIER> = <...>
# PRINT_STAT: <KEYWORD: print> <...>