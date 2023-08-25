package main

import (
	"fmt"
	_ "fmt"
)

func imprimirFigura(cantidadAsteriscos int) {
	if cantidadAsteriscos%2 == 0 {
		fmt.Println("La cantidad de asteriscos debe ser impar.")
		return
	}

	for i := 0; i < cantidadAsteriscos; i += 2 {
		espacios := (cantidadAsteriscos - i) / 2

		// Imprimir espacios iniciales
		for j := 0; j < espacios; j++ {
			fmt.Print("  ")
		}

		// Imprimir asteriscos
		for j := 0; j <= i; j++ {
			fmt.Print("* ")
		}

		fmt.Println()
	}

	for i := cantidadAsteriscos - 2; i > 0; i -= 2 {
		espacios := (cantidadAsteriscos - i) / 2

		// Imprimir espacios iniciales
		for j := 0; j < espacios; j++ {
			fmt.Print("  ")
		}

		// Imprimir asteriscos
		for j := 0; j < i; j++ {
			fmt.Print("* ")
		}

		fmt.Println()
	}
}
func main() {

	imprimirFigura(5)
}
