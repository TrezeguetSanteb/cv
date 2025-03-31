import soko
'''
algoritmo buscar_solucion(estado_inicial):
    visitados := un conjunto vacío de estados
    devolver backtrack(estado_inicial, visitados)

algoritmo backtrack(estado, visitados):
    agregar(visitados, estado)                            [1]
    si juego_ganado(estado):
        # ¡encontramos la solución!
        devolver Verdadero, []
    Para toda acción posible `a` desde el estado:
        nuevo_estado := mover(estado, a)
        si pertenece(visitados, nuevo_estado):            [2]
            continuar
        solución_encontrada, acciones := backtrack(nuevo_estado, visitados)
        si solución_encontrada:
            devolver Verdadero, concatenar([a], acciones)
    devolver Falso, ∅
'''
DIRECCIONES = [(1,0), (0,1), (0,-1), (-1,0)]

def crear_str(estado):
    nivel = [i.copy() for i in estado]
    for i in range(len(nivel)):
        nivel[i] = str(nivel[i])
    nivel = str(nivel)
    return nivel

def agregar(visitados, estado):
    visitados.add(crear_str(estado))

def concatenar(direccion, acciones):
    acciones.append(direccion)
    return acciones 

def buscar_solucion(estado):
    visitados = set()
    try:
        return backtrack(estado ,visitados)
    except RecursionError:
        return False
    
def backtrack(estado, visitados):
    agregar(visitados, estado)
    if soko.juego_ganado(estado):
        return True, []
    for direccion in DIRECCIONES:
        nuevo_estado = soko.mover(estado, direccion)
        if crear_str(nuevo_estado) in visitados:
            continue
        solucion_encontrada, acciones = backtrack(nuevo_estado, visitados)
        if solucion_encontrada:
            return True, concatenar(direccion, acciones)
    return False, None


