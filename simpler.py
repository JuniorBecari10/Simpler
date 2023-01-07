import sys

# import different parts
from util import *
import lexer
import parser

version = "Alpha v0.1"

# Source: StackOverflow (Modified)
# A custom iterator that allows the modification of its count (for goto statements)
class Iterator:
  def __init__(self, start, end):
    self.end = end
    self.position = start
  
  def __next__(self):
    if self.position >= self.end:
      raise StopIteration
    else:
      self.position += 1
      return self.position - 1
  
  def __iter__(self):
    return self
  
  def set_pos(self, n=1):
    self.position = n

# ---

# The main function. The program starts here.
def main():
  # Verify the CLI args
  if len(sys.argv) != 2:
    print("Usage: simpler <file> | [-v | --version]")
    sys.exit(1)
  
  if sys.argv[1] == "-v" or sys.argv[1] == "--version":
    print(f"Simpler {version}")
    print("Made by Antonio Carlos (JuniorBecari10).")
    print()
    print("\"The simplest compiled language ever made\".")
    sys.exit(0)
  
  # Run the program
  try:
    # Open the source file
    with open(sys.argv[1], "r") as f:
      # Read all the file and split into lines
      lines = f.read().splitlines()
      
      # Declare tokens
      tokens = []
      
      # Run the Lexer, line by line
      for i, l in enumerate(lines):
        t = lexer.lex(l, i)
        tokens.append(t)
      
      for t in tokens:
        for tt in t:
          print(tt)
     
      print()
      
      nodes = []
      
      # Run the Parser, line by line
      for i, t in enumerate(tokens):
        n = parser.parse(t, i)
        nodes.append(n)
      
      for n in nodes:
        print(n)
     
  except FileNotFoundError:
    throw_error_noline(f"The source file '{sys.argv[1]}' doesn't exist.")

# --

if __name__ == "__main__":
  main()