module ej

type GrafoConPesos = (string * (string * int) list) list

let grafoConPesos : GrafoConPesos = [
    ("i", [("a", 3); ("b", 6); ("c", 5)]);
    ("a", [("i", 1); ("c", 2); ("d", 3)]);
    ("b", [("i", 4); ("c", 5); ("d", 6)]);
    ("c", [("a", 2); ("b", 3); ("x", 1)]);
    ("d", [("a", 5); ("b", 6); ("f", 4)]);
    ("f", [("d", 7)]);
    ("x", [("c", 1)]);
]

let rec buscarCaminoMasCortoConPesos inicio fin grafo visitados =
    if inicio = fin then
        [fin]
    else
        let rec encontrarPeso nodo vecinos =
            match vecinos with
            | [] -> None
            | (vecino, peso) :: rest ->
                if vecino = nodo then Some peso
                else encontrarPeso nodo rest

        let vecinos =
            let rec obtenerVecinos nodo grafo =
                match grafo with
                | [] -> []
                | (n, v) :: rest ->
                    if n = nodo then v
                    else obtenerVecinos nodo rest
            obtenerVecinos inicio grafo
            |> List.filter (fun (vecino, _) -> not (List.exists (fun x -> x = vecino) visitados))
            |> List.sortBy (fun (_, peso) -> peso)
        
        let rec buscarDesdeVecinos vecinos =
            match vecinos with
            | [] -> []
            | (vecino, _) :: rest ->
                match encontrarPeso vecino grafo with
                | Some peso ->
                    let camino = buscarCaminoMasCortoConPesos vecino fin grafo (vecino :: visitados)
                    if List.isEmpty camino then
                        buscarDesdeVecinos rest
                    else
                        inicio :: camino
                | None -> buscarDesdeVecinos rest
        buscarDesdeVecinos vecinos

let encontrarCaminoMasCortoConPesos inicio fin grafo =
    buscarCaminoMasCortoConPesos inicio fin grafo []


