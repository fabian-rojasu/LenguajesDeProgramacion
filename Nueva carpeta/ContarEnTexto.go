package main

import (
	"bufio"
	_ "bufio"
	"fmt"
	_ "fmt"
	"strings"
	_ "strings"
)

func contar(texto string) {

	cantPalabras := strings.Fields(texto)

	scanner := bufio.NewScanner(strings.NewReader(texto))
	lineas := 0
	for scanner.Scan() {
		lineas++
	}

	fmt.Print("Numero de palabras: ", len(cantPalabras))
	fmt.Print("Numero de caracteres: ", len(texto))
	fmt.Print("Numero de lineas: ", lineas)
}

func main() {
	texto := `Este es un ejemplo, para
contar los caracteres, palabras y lineas
de un texto cualquiera`

	contar(texto)

}
