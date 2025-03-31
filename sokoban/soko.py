def crear_grilla(desc):
    '''Devuelve una lista de listas con desc.'''
    grilla = desc.copy()
    for i in range(len(desc)):
        grilla[i] = list(grilla[i])
    return grilla

def dimensiones(grilla):
    '''Devuelve una tupla con la cantidad de columnas y filas de la grilla.'''
    return len(grilla[0]), len(grilla)

def hay_pared(grilla, c, f):
    '''Devuelve True si hay una pared en la columna y fila (c, f).'''  
    return grilla[f][c] == '#'

def hay_objetivo(grilla, c, f):
    '''Devuelve True si hay un objetivo en la columna y fila (c, f).'''
    return grilla[f][c] == '.' or grilla[f][c] == '+' or grilla[f][c] == '*'
        

def hay_caja(grilla, c, f):
    '''Devuelve True si hay una caja en la columna y fila (c, f).'''
    return grilla[f][c] == '$' or grilla[f][c] == '*'
        

def hay_jugador(grilla, c, f):
    '''Devuelve True si el jugador está en la columna y fila (c, f).'''
    return grilla[f][c] == '@' or grilla[f][c] == '+'

def juego_ganado(grilla):
    '''Devuelve True si el juego está ganado.'''
    for f in grilla:
        for c in f:
            if c == '$' or c == '.':
                return False 
    return True

def posicion_jugador(grilla):
    for f in range(len(grilla)):
        for c in range(len(grilla[f])):
            if hay_jugador(grilla,c,f):
                return (c,f)    

def pisar_objetivo(grilla,c,f,x,y):   
    grilla[f][c] = ' '
    grilla[f+y][c+x] = '+'   
    
def mover(grilla, direccion):
    '''Mueve el jugador en la dirección indicada.'''
    grilla_movimiento = [i.copy() for i in grilla]        
    c,f = posicion_jugador(grilla) 
    x,y = direccion
    if not hay_caja(grilla,c+x,f+y) and not hay_pared(grilla,c+x,f+y):
        grilla_movimiento[f+y][c+x],grilla_movimiento[f][c] = '@',' '
        if grilla[f+y][c+x] == '.':
            pisar_objetivo(grilla_movimiento,c,f,x,y)
        if grilla[f][c] == '+':
            grilla_movimiento[f][c] = '.'
    elif hay_caja(grilla,c+x,f+y) and hay_objetivo(grilla,c+2*x,f+2*y):
        if grilla[f][c] == '+':
            if not hay_caja(grilla,c+x*2,f+y*2):
                grilla_movimiento[f+2*y][c+2*x] = '*'
                grilla_movimiento[f+y][c+x] = '@'
                grilla_movimiento[f][c] = '.'
                if hay_objetivo(grilla,c+x,f+y):
                    grilla_movimiento[f+y][c+x] = '+'
        else:
            if grilla[f+2*y][c+2*x] == '*':
                return grilla_movimiento
            grilla_movimiento[f+y][c+x],grilla_movimiento[f][c] = '@',' '
            if grilla[f+y][c+x] == '*':
                grilla_movimiento[f+y][c+x] = '+'
            grilla_movimiento[f+2*y][c+2*x] = '*'
    elif hay_caja(grilla,c+x,f+y) and hay_objetivo(grilla,c+x,f+y) and not hay_pared(grilla,c+x*2,f+y*2):
        if not hay_caja(grilla,c+x*2,f+y*2):
            grilla_movimiento[f+y][c+x],grilla_movimiento[f][c] = '+',' '
            grilla_movimiento[f+y*2][c+x*2] = '$'
        if grilla[f][c] == '+':
            grilla_movimiento[f+2*y][c+2*x] = '$'
            grilla_movimiento[f+y][c+x] = '+'
            grilla_movimiento[f][c] = '.'
    elif hay_caja(grilla,c+x,f+y) and not hay_pared(grilla,c+2*x,f+2*y) and not hay_caja(grilla,c+2*x,f+2*y):
        if grilla[f][c] == '+':
            grilla_movimiento[f+2*y][c+2*x] = '$'
            grilla_movimiento[f+y][c+x] = '@'
            grilla_movimiento[f][c] = '.'
        else:
            grilla_movimiento[f+y][c+x],grilla_movimiento[f][c] = '@',' '
            grilla_movimiento[f+y*2][c+x*2] = '$'


    return grilla_movimiento

