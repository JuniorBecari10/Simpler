package main

import (
  "fmt"
  "bufio"
  "os"
)

type Var interface {}

/*
Input:

a = 10
print "a is " a
*/

func main() {
  scanner := bufio.NewScanner(os.Stdin)
  
  var a Var = 10
  
  fmt.Printf("a is %v\n", a)
  
  // ---
  
  /*
  Input:
  
  b = input
  print b
  */
  
  scanner.Scan()
  var b Var = scanner.Text()
  
  fmt.Printf("%v\n", b)
}