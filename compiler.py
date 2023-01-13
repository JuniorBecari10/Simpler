from lexer import TokenType
from parser import ParseNode

# Verifications:
#
# Has any variables? -> Implementation of interface
# Has any inputs? -> Implementation of Scanner

def compile(nodes):
  has_var, has_input = verify(nodes)
  
  

def verify(nodes):
  for n in nodes:
    if n.type == ParseNode.VAR_DECL:
      has_var = True
    
    for t in n.tokens:
      if t.type == ParseNode.KEYWORD and t.cont == "input":
        has_input = True
 
 return has_var, has_input