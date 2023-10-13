persona('Fabian', 'Rojas', [1,0,1,0,1,0,1,0,1,0]).
persona('Ana', 'Perez', [0,1,0,1,0,1,0,1,0,1]).
persona('Carlos', 'Gomez', [1,1,0,0,1,1,0,0,1,1]).
persona('Maria', 'Lopez', [0,0,1,1,0,0,1,1,0,0]).

porcentaje_coincidencia([], [], 0). % Si ambas listas están vacías, el porcentaje es 0%.
porcentaje_coincidencia([H1|T1], [H2|T2], Porcentaje) :-
    porcentaje_coincidencia(T1, T2, PorcentajeRestante),
    (H1 = H2 -> Porcentaje is PorcentajeRestante + 10; Porcentaje is PorcentajeRestante).

mejor_coincidencia(Lista, Persona, PorcentajeCoincidencia) :-
    persona(Persona, _, ListaPersona),
    porcentaje_coincidencia(Lista, ListaPersona, PorcentajeCoincidencia).

coincidencia_mas_cercana(Lista, MejorPersona, PorcentajeCoincidencia) :-
    findall((Persona, Porcentaje), mejor_coincidencia(Lista, Persona, Porcentaje), Coincidencias),
    sort(2, @>, Coincidencias, CoincidenciasOrdenadas), % Ordenar en orden descendente por porcentaje
    CoincidenciasOrdenadas = [(MejorPersona, PorcentajeCoincidencia) | _].
