sumlist([], 0).
sumlist([Head|Tail], Sum) :-
    sumlist(Tail, TailSum),
    Sum is Head + TailSum.

subconj([], _).
subconj([H|T], S) :-
    member(H, S),
    subconj(T, S).


aplanar([], []).
aplanar([Head|Tail], FlatList) :-
    is_list(Head),            
    aplanar(Head, FlatHead),  
    aplanar(Tail, FlatTail),  
    append(FlatHead, FlatTail, FlatList).
aplanar([Head|Tail], [Head|FlatTail]) :-
    \+ is_list(Head),        
    aplanar(Tail, FlatTail).

partir([], _, [], []).
partir([Head|Tail], Umbral, [Head|Menores], Mayores) :-
    Head =< Umbral,
    partir(Tail, Umbral, Menores, Mayores).
partir([Head|Tail], Umbral, Menores, [Head|Mayores]) :-
    Head > Umbral,
    partir(Tail, Umbral, Menores, Mayores).

sub_cadenas(Subcadena, ListaCadenas, Filtradas) :-
    incluir_cadenas_con_subcadena(Subcadena, ListaCadenas, Filtradas).


sub_cadenas(Subcadena, ListaCadenas, Filtradas) :-
    incluir_cadenas_con_subcadena(Subcadena, ListaCadenas, Filtradas).

incluir_cadenas_con_subcadena(_, [], []).
incluir_cadenas_con_subcadena(Subcadena, [Cadena|Resto], [Cadena|FiltradasResto]) :-
    sub_atom(Cadena, _, _, _, Subcadena),
    incluir_cadenas_con_subcadena(Subcadena, Resto, FiltradasResto).
incluir_cadenas_con_subcadena(Subcadena, [_|Resto], FiltradasResto) :-
    incluir_cadenas_con_subcadena(Subcadena, Resto, FiltradasResto).

