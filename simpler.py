import sys

# import different parts
from os.path import exists

from util import *

import lexer
import parser

version = "Alpha v0.1"

#langs = ["go", "c", "cpp"]

# ---

# The main function. The program starts here.
def main():
  # Verify the CLI args
  if len(sys.argv) < 2 or len(sys.argv) > 4:
    print("Usage: simpler [run] [-v | --version] <file>")
    sys.exit(1)
  
  if sys.argv[1].lower() == "-v" or sys.argv[1].lower() == "--version":
    print(f"Simpler {version}")
    print("Made by Antonio Carlos (JuniorBecari10).")
    sys.exit(0)
  
  file = sys.argv[1]
  
  if sys.argv[1].lower() == "run" and not exists(sys.argv[1]):
    if len(sys.argv) == 2:
      print("Usage: simpler [run] [-v | --version] <file>")
      sys.exit(1)
    
    file = sys.argv[2]
  
  # Run the program
  try:
    # Open the source file
    with open(file, "r") as f:
      # Read all the file and split into lines
      lines = f.read().splitlines()
    
    # Declare tokens
    tokens = []
    
    # Run the Lexer, line by line
    for i, l in enumerate(lines):
      if len(l) == 0:
        continue
      
      t = lexer.lex(l, i)
      tokens.append(t)
    
    for t in tokens:
      for tt in t:
        print(tt)
    
    print()
    
    nodes = []
    
    # Run the Parser, line by line
    for i, t in enumerate(tokens):
      n = parser.parse(t, i, lines[i])
      nodes.append(n)
    
    for n in nodes:
      print(n)
    
    # Compile the code.
    
    
    
  except FileNotFoundError:
    throw_error_noline(f"The source file '{sys.argv[1]}' doesn't exist.", "Verify if you typed the source file's name correctly.")

# --

if __name__ == "__main__":
  main()