package main

import (
        "fmt"
)

func main(){
	var n int
	fmt.Println("Ingrese el numero de la variable n")
    fmt.Scan(&n)
    c := 0
    for j := 1; j < n; j= j+1 { 
    	if (n%j) == 0 {
    		c = c + j
    	}
    }
    if c == n {
    	fmt.Println("n es un numero perfecto")
    }else {
    	fmt.Println("n no es un numero perfecto")
    }
}