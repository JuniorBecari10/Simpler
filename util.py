import sys

def is_digit(c):
  return c >= "0" and c <= "9"

def is_letter(c):
  return (c >= "A" and c <= "Z") or (c >= "a" and c <= "z")

# Function used to throw errors
def throw_error(message, line_number, suggestion):
  line_number = str(line_number)
  
  print("--- ERROR --- ")
  print("On line " + line_number + "\n")
  print(message)
  print()
  print(suggestion)
  
  sys.exit(1)

# Function to throw error without specifing the line
def throw_error_noline(message, suggestion):
  print("--- ERROR ---")
  print(message)
  print()
  print(suggestion)
  
  sys.exit(1)

def any_has_type(tokens, type):
  for t in tokens:
    if t.type == type:
      return True
  
  return False

def any_cont_contains(tokens, cont):
  for t in tokens:
    if t.cont.__contains__(cont):
      return True
  
  return False