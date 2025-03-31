import biblioteca
from heap import Heap
import auxiliares as aux

MAX = float('inf')
RAPIDO = "rapido"
     
def camino_mas(grafo, dic_ciudades, origen, destino, modo):
    peso_min, padre_min, origen_min, destino_min = MAX, {}, '', ''
    for aeropuerto_i in dic_ciudades[origen]:
        for aeropuerto_j in dic_ciudades[destino]:
            padre, peso = biblioteca.camino_minimo(grafo, aeropuerto_i, aeropuerto_j, modo)
            if peso[aeropuerto_j] < peso_min:
                peso_min = peso[aeropuerto_j]
                padre_min, origen_min, destino_min = padre, aeropuerto_i, aeropuerto_j
    return aux.mostrar_camino(padre_min, origen_min, destino_min)

def camino_escalas(grafo, dic_ciudades, origen, destino):
    dist_min, padre_min, origen_min, destino_min = MAX, {}, "", ""
    for aeropuerto_i in dic_ciudades[origen]:
        for aeropuerto_j in dic_ciudades[destino]:
            dist, padre = biblioteca.bfs(grafo, aeropuerto_i, aeropuerto_j)
            if dist_min > dist[aeropuerto_j]:
                dist_min = dist[aeropuerto_j]
                padre_min, origen_min, destino_min = padre, aeropuerto_i, aeropuerto_j
    return aux.mostrar_camino(padre_min, origen_min, destino_min)
    
def centralidad_c(grafo,n): 
    cent = biblioteca.centralidad(grafo)
    heap = Heap(aux.cmp_max)
    for aeropuerto, valor in cent.items():
        heap.encolar((valor, aeropuerto.ver_codigo()))
    res = []
    while True:
        _, codigo = heap.desencolar()
        res.append(codigo)
        if n == 1:
            print(codigo)
            break
        print(codigo +  ",", end='')
        n -= 1

def nueva_aerolinea(grafo, ruta):
    arbol = biblioteca.mst_prim(grafo, aux.cmp_min_precio)
    vuelos = arbol.obtener_aristas()
    with open(ruta, 'w') as arch:
        for vuelo in vuelos:
            aeropuerto_i, aeropuerto_j, v = vuelo
            linea = ','.join(map(str, (aeropuerto_i.ver_codigo(), aeropuerto_j.ver_codigo(), v.ver_tiempo(), v.ver_precio(), v.ver_cant_vuelos())))
            arch.write(linea + '\n')
    print("OK")
        
def itinerario(grafo_original, dic_ciudades, archivo):
    grafo_itinerario = aux.leer_itinerario(grafo_original, archivo)
    orden = biblioteca.orden_topologico(grafo_itinerario)
    for i in range(len(orden)):
        if i == len(orden)-1:
            print(orden[i])
            break
        print(orden[i] + ", ",end='')
    for i in range(1,len(orden)):
        camino_mas(grafo_original, dic_ciudades, orden[i-1], orden[i], RAPIDO)
            
def exportar_kml(lugares, dic_codigos, ultimo_comando, ruta_kml):
    biblioteca.crear_kml(lugares, dic_codigos, ruta_kml, ultimo_comando)
    aux.imprimir(lugares)
    print("OK")
    