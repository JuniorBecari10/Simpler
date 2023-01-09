#include <iostream>
#include <string>

struct Var
{
  string s;
  float f;
  
  char type;
};

Var::Var operator = (Var &v)
{
  
}

int main()
{
  Var data;
  data = "Hello."
  
  std::cout << data << std::endl;
  
  return 0;
}