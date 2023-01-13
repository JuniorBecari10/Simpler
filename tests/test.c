#include <stdio.h>

typedef enum
{
  NUM,
  STR,
  ARR
}
VarType;

typedef struct
{
  void *value;
  VarType type;
}
Var;

void print(Var v);

int main()
{
  /*
  a = 10
  print "a is " a
  */
  
  float av = 10;
  
  Var a;
  a.value = &av;
  a.type = NUM;
  
  printf("a is ");
  print(a);
  
  return 0;
}

void print(Var v)
{
  switch (v.type)
  {
    case NUM:
      printf("%f", (float *) v.value);
      break;
    
    case STR:
      printf("%s", (char *) v.value);
      break;
  }
}