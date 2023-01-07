import sys

def is_digit(c):
  return c >= "0" and c <= "9"

def is_letter(c):
  return (c >= "A" and c <= "Z") or (c >= "a" and c <= "z")

# Function used to throw errors
def throw_error(message, line_number):
  line_number = str(line_number)
  
  print("-----")
  print("ERROR")
  print("On line " + line_number + "\n")
  print(message)
  print("-----")
  
  sys.exit(1)

# Function to throw error without specifing the line
def throw_error_noline(message):
  print("-----")
  print("ERROR\n")
  print(message)
  print("-----")
  
  sys.exit(1)