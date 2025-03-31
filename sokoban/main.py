import soko
import gamelib
from pila import Pila
from backtracking import buscar_solucion

def niveles(ruta_entrada):
    niveles = {}
    i = 1
    with open(ruta_entrada) as entrada:
        next(entrada)
        for linea in entrada:
            if linea == '\n':
                i += 1
                next(entrada)
                continue
            linea = linea.rstrip()
            niveles[i] = niveles.get(i,[])
            niveles[i].append(linea)
    return niveles

def arreglar_niveles(nivel):
    max = 0
    n = 0
    for f in nivel:
        if len(f) > max:
            max = len(f)
    for i in nivel:
        if len(i) != max:
            n = max - len(i)
            i += [' ']*n
    return nivel

def teclas(ruta_entrada):
    teclas = {}
    with open(ruta_entrada) as entrada:
        for linea in entrada:
            if linea == '\n':
                linea = next(entrada)
            linea = linea.rstrip()
            key, value = linea.split(' = ')
            teclas[key] = value
        return teclas 

def actualizar_juego(nivel, tecla, instrucciones, deshacer, rehacer):
    movimientos = []
    if instrucciones[tecla] == 'NORTE':
        nivel = soko.mover(nivel,(0,-1))
    elif instrucciones[tecla] == 'SUR':
        nivel = soko.mover(nivel,(0,1))
    elif instrucciones[tecla] == 'ESTE':
        nivel = soko.mover(nivel,(1,0))
    elif instrucciones[tecla] == 'OESTE':
        nivel = soko.mover(nivel,(-1,0))
    elif instrucciones[tecla] == 'DESHACER':
        if not deshacer.esta_vacia():
            rehacer.apilar(nivel)
            nivel = deshacer.desapilar()
    elif instrucciones[tecla] == 'REHACER':
        if not rehacer.esta_vacia():
            deshacer.apilar(nivel)
            nivel = rehacer.desapilar()
    elif instrucciones[tecla] == 'BUSCAR':
        bool, movimientos = buscar_solucion(nivel)
    return nivel, movimientos

def juego_mostrar(nivel):      
    c_jug,f_jug = soko.posicion_jugador(nivel)
    x,y = soko.dimensiones(nivel)
    gamelib.resize(x*63, y*63)
    for f in range(y):
        for c in range(x):
            gamelib.draw_image('img/ground.gif', c*64, f*64)
            if soko.hay_pared(nivel, c, f):
                gamelib.draw_image('img/wall.gif', c*64, f*64)
            if soko.hay_caja(nivel, c, f):
                gamelib.draw_image('img/box.gif', c*64, f*64)
            if soko.hay_objetivo(nivel, c, f):
                gamelib.draw_image('img/goal.gif', c*64, f*64)
    gamelib.draw_image('img/player.gif', c_jug*64, f_jug*64)
    
def main():
    n = niveles('niveles.txt')
    instrucciones = teclas('teclas.txt')
    
    for k,v in n.items() :
        deshacer = Pila()
        rehacer = Pila()
        nivel = soko.crear_grilla(v)
        nivel = arreglar_niveles(nivel)
        
        while gamelib.is_alive():
            if soko.juego_ganado(nivel):
                break
            
            gamelib.draw_begin()
            juego_mostrar(nivel)
            gamelib.draw_end()
            

            gamelib.icon('img/box.gif')
            gamelib.title(f'Sokoban {k}')

            ev = gamelib.wait(gamelib.EventType.KeyPress)
            if not ev:
                break
            
            if ev.type == gamelib.EventType.KeyPress and ev.key == 'r':
                nivel = soko.crear_grilla(niveles('niveles.txt')[k])
                nivel = arreglar_niveles(nivel)
                deshacer = Pila()
                rehacer = Pila()

            
            if ev.type == gamelib.EventType.KeyPress and ev.key == 'Escape':
                return     
            
            instrucciones = teclas('teclas.txt')
            tecla = ev.key
            if tecla in instrucciones:
                if instrucciones[tecla] in ('NORTE', 'SUR', 'ESTE', 'OESTE'): 
                    deshacer.apilar(nivel)
            
                if not instrucciones[tecla] == 'APLICAR':
                    nivel, movimientos = actualizar_juego(nivel,tecla, instrucciones, deshacer, rehacer)
            
                if instrucciones[tecla] == 'APLICAR':
                    if len(movimientos) != 0:
                        deshacer.apilar(nivel)
                        nivel = soko.mover(nivel, movimientos[-1])
                        movimientos.pop(-1)


gamelib.init(main)

