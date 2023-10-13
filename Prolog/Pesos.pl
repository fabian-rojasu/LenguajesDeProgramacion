% Conexiones con pesos
conectado(i, 2, 4).
conectado(2, 3, 2).
conectado(2, 8, 6).
conectado(8, 9, 3).
conectado(9, 3, 5).
conectado(3, 4, 1).
conectado(4, 10, 7).
conectado(10, 16, 4).
conectado(16, 22, 5).
conectado(22, 21, 2).
conectado(21, 15, 3).
conectado(15, 14, 2).
conectado(14, 13, 1).
conectado(13, 7, 2).
conectado(7, 1, 5).
conectado(14, 20, 6).
conectado(20, 26, 4).
conectado(22, 28, 3).
conectado(26, 27, 2).
conectado(27, 28, 1).
conectado(28, 29, 2).
conectado(29, 23, 3).
conectado(23, 17, 5).
conectado(17, 11, 2).
conectado(11, 5, 3).
conectado(1, 7, 2).
conectado(5, 6, 2).
conectado(28, 34, 2).
conectado(34, 35, 1).
conectado(35, 36, 1).
conectado(36, 30, 1).
conectado(30, 24, 2).
conectado(24, 18, 3).
conectado(18, 12, 2).
conectado(32, 31, 2).
conectado(31, 25, 3).
conectado(25, 19, 1).
conectado(34, 33, 1).
conectado(33, 32, 1).
conectado(32, f, 2).

% Predicado para encontrar la ruta más corta
ruta_mas_corta(Inicio, Fin, Ruta) :-
    dijkstra([[Inicio, 0, []]], Fin, Ruta).

% Implementación del algoritmo de Dijkstra
dijkstra([[Nodo, CostoAcumulado, Camino]|_], Nodo, [Nodo|Camino]) :-
    reverse([Nodo|Camino], Ruta),
    write('Ruta más corta: '), write(Ruta),
    nl,
    write('Costo total: '), write(CostoAcumulado),
    !. % Detener la búsqueda cuando se llega al nodo de destino.
dijkstra([[Nodo, CostoAcumulado, Camino]|Cola], NodoFinal, Ruta) :-
    findall([NodoAdyacente, NuevoCosto, [Nodo|Camino]],
            (conectado(Nodo, NodoAdyacente, Costo),
             \+ member(NodoAdyacente, [Nodo|Camino]),
             NuevoCosto is CostoAcumulado + Costo),
            NuevosCaminos),
    append(Cola, NuevosCaminos, NuevaCola),
    sort(2, @=<, NuevaCola, ColaOrdenada), % Ordenar la cola por costo acumulado.
    dijkstra(ColaOrdenada, NodoFinal, Ruta).
