package main

import (
  "fmt"
)

type Var interface {}

func main() {
  var a Var
  fmt.Scanln(&a)
}