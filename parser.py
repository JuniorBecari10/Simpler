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

def parse(tokens, line_n, line):
  # variable declaration (must have 3 or more tokens (a = <value>))
  if len(tokens) >= 3 and tokens[0].type == TokenType.IDENTIFIER and tokens[1].type == TokenType.ASSIGN:
    return ParseNode(NodeType.VAR_DECL, tokens)
  
  elif len(tokens) >= 1 and tokens[0].type == TokenType.KEYWORD and tokens[0].cont == "print":
    return ParseNode(NodeType.PRINT_STAT, tokens)
  
  # Unknown
  else:
    throw_error(f"Unknown statement: '{line}'.", line_n + 1, ("This is not the correct way to declare a variable.\n\nExample:\na = 10\nb = 'Hello'" if any_has_type(tokens, TokenType.ASSIGN) else ("This is not the correct way to declare a print statement.\n\nExample:\nprint 'Hello World!'\nprintl 'Hello.'" if any_cont_contains(tokens, "pri") else "")))

# Grammar:
#
# VAR_DECL: <IDENTIFIER> = <...>
# PRINT_STAT: <KEYWORD: print> <...>