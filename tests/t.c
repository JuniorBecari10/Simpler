#include <stdio.h>

typedef struct
{
  char *s;
  float f;
  char type;
}
Var;

void print(Var *v)
{
  if (v->type == 's')
    printf("%s dd", v->s);
  else
    printf("%d aaaa", v->f);
}

int main()
{
  /*
    Input:
    
    a = 10
    print "Hello World" a
  */
  
  Var *a;
  a->f = 10;
  a->s = "hello";
  a->type = 's';
  
  print(a);
  printf("\n");
  
  return 0;
}