#include <stdio.h>
#include <stdbool.h>

typedef struct
{
  char *value;
  bool is_num;
}
Var;

void print(Var v, ...)
{
  va_list s;
  va_start(s, v);
  
  
  
}

int main()
{
  /*
    Input:
    
    a = 10
    print "Hello World" a
  */
  
  Var a;
  a.value = "10";
  a.is_num = true;
  
  
  
  return 0;
}