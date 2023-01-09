import sys

# Verify if the specified char is a digit (i.e.: a number)
def is_digit(c):
  return c >= "0" and c <= "9"

# Verify if the specified char is a letter
def is_letter(c):
  return (c >= "A" and c <= "Z") or (c >= "a" and c <= "z")

# Function used to throw errors, with a suggestion on how to fix them
def throw_error(message, line_number, suggestion):
  line_number = str(line_number)
  
  print("--- ERROR --- ")
  print("On line " + line_number + "\n")
  print(message)
  print()
  print(suggestion)
  
  sys.exit(1)

# Function to throw error without specifing the line, with a suggestion on how to fix them
def throw_error_noline(message, suggestion):
  print("--- ERROR ---")
  print(message)
  print()
  print(suggestion)
  
  sys.exit(1)

# Verify if any of the tokens specified has a specified type
def any_has_type(tokens, type):
  for t in tokens:
    if t.type == type:
      return True
  
  return False

# Verify if any cont of the tokens specified contains the specified cont
def any_cont_contains(tokens, cont):
  for t in tokens:
    if t.cont.__contains__(cont):
      return True
  
  return False