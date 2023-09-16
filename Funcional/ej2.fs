module ej2

type Coordenada = int * int
type GrafoLaberinto = (Coordenada * (Coordenada * int) list) list

let laberinto : GrafoLaberinto = [
    ((0, 0), [((0, 1), 1); ((1, 0), 1)]);  // Ejemplo: Casilla (0, 0) tiene vecinos (0, 1) y (1, 0)
    ((0, 1), [((0, 0), 1); ((0, 2), 1)]);
    ((0, 2), [((0, 1), 1); ((0, 3), 1)]);
    ((0, 3), [((0, 2), 1); ((1, 3), 1)]);
    ((1, 0), [((0, 0), 1); ((1, 1), 1)]);
    ((1, 1), [((1, 0), 1); ((1, 2), 1)]);
    ((1, 2), [((1, 1), 1); ((1, 3), 1)]);
    ((1, 3), [((0, 3), 1); ((1, 2), 1)]);
]

let rec dfs inicio destino grafo ruta visitados =
    if inicio = destino then
        ruta :: []  // Hemos encontrado una ruta válida
    else
        let vecinos =
            match List.tryFind (fun (nodo, _) -> nodo = inicio) grafo with
            | Some (_, vecinos) -> vecinos
            | None -> []

        let rutasPosibles =
            List.collect (fun (vecino, peso) ->
                if not (List.contains vecino visitados) then
                    dfs vecino destino grafo (vecino :: ruta) (vecino :: visitados)
                else
                    [])
                vecinos
        rutasPosibles

let encontrarRutas inicio destino grafo =
    dfs inicio destino grafo [inicio] [inicio]

let encontrarRutaMasCorta inicio destino grafo =
    let rutas = encontrarRutas inicio destino grafo
    match List.minBy List.length rutas with
    | [] -> None  // No se encontró ruta
    | ruta -> Some ruta


