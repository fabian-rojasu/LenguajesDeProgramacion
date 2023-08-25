package main

import (
	"fmt"
)

type Calzado struct {
	Modelo string
	Precio float64
	Talla  int
}

type InventarioItem struct {
	Zapato Calzado
	Stock  int
}

func (item *InventarioItem) Vender(cantidad int) bool {
	if cantidad <= item.Stock {
		item.Stock -= cantidad
		return true
	}
	return false
}

func main() {
	inventario := []InventarioItem{
		{Zapato: Calzado{"Nike", 50000, 42}, Stock: 10},
		{Zapato: Calzado{"Adidas", 60000, 38}, Stock: 5},
		// Puedes agregar más elementos al inventario aquí
	}

	// Realizar ventas
	realizarVenta(&inventario, "Nike", 42, 3)
	realizarVenta(&inventario, "Adidas", 38, 2)
	realizarVenta(&inventario, "Reebok", 40, 1) // Zapato no disponible

	// Imprimir inventario después de ventas
	fmt.Println("Inventario después de las ventas:")
	for _, item := range inventario {
		fmt.Printf("Modelo: %s, Talla: %d, Precio: %.2f, Stock: %d\n", item.Zapato.Modelo, item.Zapato.Talla, item.Zapato.Precio, item.Stock)
	}
}

func realizarVenta(inventario *[]InventarioItem, modelo string, talla int, cantidad int) {
	for i, item := range *inventario {
		if item.Zapato.Modelo == modelo && item.Zapato.Talla == talla {
			if item.Vender(cantidad) {
				fmt.Printf("Venta exitosa: Se vendieron %d pares de %s talla %d.\n", cantidad, modelo, talla)
			} else {
				fmt.Printf("Venta fallida: No hay suficiente stock de %s talla %d.\n", modelo, talla)
			}
			(*inventario)[i] = item // Actualizar el inventario
			return
		}
	}
	fmt.Printf("Venta fallida: No se encontró el zapato %s talla %d en el inventario.\n", modelo, talla)
}
