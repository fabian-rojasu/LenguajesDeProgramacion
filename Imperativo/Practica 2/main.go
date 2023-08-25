package main

import (
	"fmt"
	"sort"
)

type producto struct {
	nombre   string
	cantidad int
	precio   int
}
type listaProductos []producto

var lProductos listaProductos
var listProdMin listaProductos

const existenciaMinima int = 10 //la existencia mínima es el número mínimo debajo de el cual se deben tomar eventuales desiciones

func (l *listaProductos) agregarProducto(productos ...producto) {
	for _, p := range productos {
		pr, err := l.buscarProducto(p.nombre)
		if err != -1 {
			pr.cantidad = pr.cantidad + p.cantidad
			if pr.precio != p.precio {
				pr.precio = p.precio
			}
		} else {
			*l = append(*l, producto{nombre: p.nombre, cantidad: p.cantidad, precio: p.precio})
		}
	}
}

func (l *listaProductos) buscarProducto(nombre string) (*producto, int) {
	var err = -1
	var p *producto = nil
	for i := 0; i < len(*l); i++ {
		if (*l)[i].nombre == nombre {
			p = &((*l)[i])
			err = 0
		}
	}
	return p, err
}

func (l *listaProductos) venderProducto(nombre string, cant int) {
	var prod, err = l.buscarProducto(nombre)
	if err != -1 {

		prod.cantidad = prod.cantidad - cant
		if prod.cantidad >= 0 {
			l.eliminar(nombre)
		}
	}
}

func (l *listaProductos) eliminar(prod string) {
	for i, p := range *l {
		if p.nombre == prod {
			*l = append((*l)[:i], (*l)[i+1:]...)
			break
		}
	}
}

//haga una función para a partir del nombre del producto, se pueda modificar el precio del mismo Pero utilizando la función buscarProducto MODIFICADA PREVIAMENTE

func llenarDatos() {
	lProductos.agregarProducto(producto{nombre: "arroz", cantidad: 15, precio: 2500},
		producto{nombre: "frijoles", cantidad: 8, precio: 1200},
		producto{nombre: "café", cantidad: 3, precio: 4500},
		producto{nombre: "frijoles", cantidad: 8, precio: 100},
		producto{nombre: "papas", cantidad: 2, precio: 100},
		producto{nombre: "Pizza", cantidad: 1, precio: 100})

}
func (l *listaProductos) listarProductosMínimos() listaProductos {
	for _, p := range *l {
		if p.cantidad < existenciaMinima {
			listProdMin = append(listProdMin, p)
		}
	}
	return listProdMin
}

func (l *listaProductos) aumentarDeMin(listaMinimos listaProductos) listaProductos {
	for i := 0; i < len(listaMinimos); i++ {
		listaMinimos[i].cantidad = existenciaMinima
	}
	return listaMinimos
}

func (l *listaProductos) ordenarPorEdad(listaMinimos listaProductos) {
	sort.Slice(listaMinimos, func(i, j int) bool {
		return listaMinimos[i].cantidad < listaMinimos[j].cantidad
	})
}

func main() {
	llenarDatos()
	fmt.Println("Productos originales")
	fmt.Println(lProductos)
	//A)
	fmt.Println("Productos minimos")
	lProductos.listarProductosMínimos()
	fmt.Println(listProdMin)

	fmt.Println("Despues de aumentar")
	lProductos.aumentarDeMin(listProdMin)
	fmt.Println(listProdMin)

	//B)
	fmt.Println("Lista ordenada")
	lProductos.ordenarPorEdad(listProdMin)
	fmt.Println(listProdMin)
}
