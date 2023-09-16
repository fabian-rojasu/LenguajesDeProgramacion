open ej
open ej2

let desplazar (direccion:string) (n:int) (lista:int list) =
    let length = List.length lista
    match direccion with
    | "izq" ->
        if n >= length then List.replicate length 0
        else
            let primeraParte = List.skip n lista
            let segundaParte = List.replicate n 0
            primeraParte @ segundaParte
    | "der" ->
        if n >= length then List.replicate length 0
        else
            let primeraParte = List.replicate n 0
            let segundaParte = List.take (length - n) lista
            primeraParte @ segundaParte
    | _ -> failwith "Dirección no válida"
    
    
let sub_cadenas (lista: string list) (patron: string) =
    lista |> List.filter (fun cadena -> cadena.Contains(patron))

  
let n_esimo n lista =
    let indices = List.mapi (fun i _ -> if i = n then Some i else None) lista
    let resultado = List.choose id indices
    match resultado with
    | [x] -> Some (List.nth lista x)
    | _ -> None


let rec vecinos nodo grafo =
    match grafo with
    | [] -> []
    | (head, neighbors) :: rest ->
        if head = nodo then neighbors
        else vecinos nodo rest
        
let miembro elem lista =
    List.exists (fun x -> x = elem) lista

// Función para extender una ruta
let extender ruta grafo = 
    List.filter
        (fun x -> x <> [])
        (List.map  (fun x -> if (miembro x ruta) then [] else x::ruta) (vecinos (List.head ruta) grafo)) 

let rec prof2 ini fin grafo =
    let rec prof_aux fin ruta grafo =
        if List.isEmpty ruta then []
        elif (List.head (List.head ruta)) = fin then
            List.rev (List.head ruta) //:: prof_aux fin ((extender (List.head ruta) grafo) @ (List.tail ruta)) grafo       
        else
            prof_aux fin ((List.tail ruta) @ (extender (List.head ruta) grafo)  ) grafo
    prof_aux fin [[ini]] grafo



    
[<EntryPoint>]
let main argv =
    printfn "**********Ejercicio 1********"
    let lista1 = [1; 2; 3; 4; 5]
    let resultado1 = desplazar "izq" 2 lista1
    let resultado2 = desplazar "der" 2 lista1
    let resultado3 = desplazar "izq" 6 lista1
    printfn "%A" resultado1
    printfn "%A" resultado2
    printfn "%A" resultado3
    
    printfn "**********Ejercicio 2********"
    let lista = ["la casa"; "el perro"; "pintando la cerca"]
    let subcadena = "la"
    let resultado = sub_cadenas lista subcadena

    printfn "Resultado: %A" resultado
    
    
    printfn "**********Ejercicio 3********"
    let resultado1 = n_esimo 2 [1; 2; 3; 4; 5]
    let resultado2 = n_esimo 3 [1; 2; 3; 4; 5]
    let resultado3 = n_esimo 6 [1; 2; 3; 4; 5]

    match resultado1 with
    | Some valor -> printfn "Resultado 1: %d" valor
    | None -> printfn "Resultado 1: No existe"

    match resultado2 with
    | Some valor -> printfn "Resultado 2: %d" valor
    | None -> printfn "Resultado 2: No existe"

    match resultado3 with
    | Some valor -> printfn "Resultado 3: %d" valor
    | None -> printfn "Resultado 3: No existe"
    
    
    printfn "**********Ejercicio 4********"
    let resultado = encontrarCaminoMasCortoConPesos "i" "f" grafoConPesos
    printfn "Camino más corto con pesos: %A" resultado
    
    
    printfn "**********Ejercicio 5********"
    
    let inicio = (0, 0)
    let destino = (1, 3)

    match encontrarRutaMasCorta inicio destino laberinto with
    | Some ruta ->
        printfn "Ruta más corta para resolver el laberinto:"
        ruta |> List.iter (fun (x, y) -> printfn "(%d, %d)" x y)
    | None ->
        printfn "No se encontró una ruta para resolver el laberinto."

    0 // Código de salida