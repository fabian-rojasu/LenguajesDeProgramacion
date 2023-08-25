package main

import (
	"fmt"
)

func rotateSequence(arr *[]interface{}, rotationAmount int, direction int) {
	length := len(*arr)

	if direction == 0 { // Izquierda
		rotationAmount = rotationAmount % length
		temp := append((*arr)[:0:0], (*arr)[rotationAmount:]...)
		*arr = append(temp, (*arr)[:rotationAmount]...)
	} else if direction == 1 { // Derecha
		rotationAmount = length - (rotationAmount % length)
		temp := append((*arr)[:0:0], (*arr)[rotationAmount:]...)
		*arr = append(temp, (*arr)[:rotationAmount]...)
	}
}

func main() {
	secuenciaOriginal := []interface{}{"a", "b", "c", "d", "e", "f", "g", "h"}

	rotaciones := []struct {
		cantidadRotaciones int
		direccion          int
	}{
		{3, 0}, // Rotación a la izquierda
		{2, 1}, // Rotación a la derecha
		{5, 0}, // Rotación a la izquierda
	}

	fmt.Println("Secuencia Original =", secuenciaOriginal)

	for _, r := range rotaciones {
		secuenciaCopia := make([]interface{}, len(secuenciaOriginal))
		copy(secuenciaCopia, secuenciaOriginal)

		rotateSequence(&secuenciaCopia, r.cantidadRotaciones, r.direccion)
		direccionStr := "izq"
		if r.direccion == 1 {
			direccionStr = "der"
		}

		fmt.Printf("Cantidad de rotaciones = %d, Dirección = %s\n", r.cantidadRotaciones, direccionStr)
		fmt.Println("Secuencia final rotada =", secuenciaCopia)
		fmt.Println()
	}
}
