from heap import Heap
from collections import deque
import auxiliares as aux
from grafo import Grafo
import xml.etree.ElementTree as ET

BARATO = "barato"
RAPIDO = "rapido"
CANT_VUELOS = "cant_vuelos"

'''
def camino_minimo(grafo, origen, destino, modo, cmp):
    peso, padre = {}, {}
    for aeropuerto in grafo.obtener_vertices():
        peso[aeropuerto] = float('inf')
    peso[origen] = 0
    padre[origen] = None
    heap = Heap(cmp)
    heap.encolar((0, origen))
    while not heap.esta_vacia():
        _, v = heap.desencolar()
        for w in grafo.adyacentes(v):
            p = grafo.peso_arista(v, w)
            if modo == BARATO:
                peso_por_aca = peso[v] + p.ver_precio()
            elif modo == RAPIDO:
                peso_por_aca = peso[v] + p.ver_tiempo()
            else:
                peso_por_aca = peso[v] + p.ver_cant_vuelos()
            
            if peso_por_aca < peso[w]:
                peso[w] = peso_por_aca
                padre[w] = v
                heap.encolar((peso[w],w))
        if v == destino:
            break
    return padre, peso
'''

def camino_minimo(grafo, origen, destino, modo):
    peso, padre = {}, {}
    for aeropuerto in grafo.obtener_vertices():
        peso[aeropuerto] = float('inf')
    peso[origen] = 0
    padre[origen] = None
    aristas = grafo.obtener_aristas()
    for i in range(len(grafo.obtener_vertices())):
        cambio = False
        for v, w, p in aristas:
            if modo == BARATO:
                peso_por_aca = peso[v] + p.ver_precio()
            elif modo == RAPIDO:
                peso_por_aca = peso[v] + p.ver_tiempo()
            else:
                peso_por_aca = peso[v] + p.ver_cant_vuelos()
            
            if peso_por_aca < peso[w]:
                cambio = True
                padre[w] = v
                peso[w] = peso_por_aca
        if v == destino:
            break
        if not cambio:
            break
    return padre, peso

def bfs(grafo, origen, destino):
    visitados = set()
    dist = {}
    padre = {}
    dist[origen] = 0
    padre[origen] = None
    visitados.add(origen)
    cola = deque()
    cola.appendleft(origen)
    while cola:
        v = cola.popleft()
        for w in grafo.adyacentes(v):
            if w not in visitados:
                dist[w] = dist[v] + 1
                padre[w] = v
                visitados.add(w)
                cola.appendleft(w)
            if w == destino:
                break
    return dist, padre

def centralidad(grafo):
    cent = {}
    for v in grafo.obtener_vertices():
        cent[v] = 0
    for v in grafo.obtener_vertices():
        for w in grafo.obtener_vertices():
            if v == w: continue
            padre, _ = camino_minimo(grafo, v, w, CANT_VUELOS)
            if padre[w] is None: 
                continue
            actual = padre[w]
            while actual != v:
                cent[actual] += 1
                actual = padre[actual]
    return cent

def orden_topologico(grafo):
    grados_entrada = {}
    visitados = set()
    cola = deque()

    for v in grafo.obtener_vertices():
        grados_entrada[v] = 0

    for v in grafo.obtener_vertices():
        for w in grafo.adyacentes(v):
            grados_entrada[w] += 1
            
    for v in grafo.obtener_vertices():
        if grados_entrada[v] == 0:
            cola.appendleft(v)

    orden = []
    
    while cola:
        v = cola.popleft()
        visitados.add(v)
        orden.append(v)
        for w in grafo.adyacentes(v):
            if w not in visitados: 
                grados_entrada[w] -= 1
                if grados_entrada[w] == 0:
                    cola.appendleft(w)

    return orden

def mst_prim(grafo, cmp):
    v = grafo.vertice_aleatorio()
    visitados = set()
    visitados.add(v)
    heap = Heap(cmp)
    arbol = Grafo(False)
    for vertice in grafo.obtener_vertices():    
        arbol.agregar_vertice(vertice)
    for w in grafo.adyacentes(v):
        heap.encolar((grafo.peso_arista(v,w), (v,w)))
    while not heap.esta_vacia():
        peso, (v, w) = heap.desencolar()
        if w in visitados:
            continue
        arbol.agregar_arista(v, w, peso)
        visitados.add(w)
        for u in grafo.adyacentes(w):
            if u not in visitados:
                heap.encolar((grafo.peso_arista(w,u), (w,u)))
    return arbol

def crear_kml(lugares, dic_codigos, ruta, comando):
    contenido = '''<?xml version="1.0" encoding="UTF-8"?>
<kml xmlns="http://earth.google.com/kml/2.1">
    <Document>\n'''
    contenido += '<name>KML de ' + comando + '</name>\n'
    for ciudad in lugares:
        contenido += f'''
        <Placemark>
            <name>{dic_codigos[ciudad].ver_ciudad()}</name>
            <description>{ciudad}</description>
            <Point>
                <coordinates>{dic_codigos[ciudad].ver_longitud()}, {dic_codigos[ciudad].ver_latitud()}</coordinates>
            </Point>
        </Placemark>\n'''
        
    for i in range(1,len(lugares)):
        contenido += f'''
        <Placemark>
            <LineString>
                <coordinates>{dic_codigos[lugares[i-1]].ver_longitud()}, {dic_codigos[lugares[i-1]].ver_latitud()} {dic_codigos[lugares[i]].ver_longitud()}, {dic_codigos[lugares[i]].ver_latitud()}</coordinates>
            </LineString>
        </Placemark>\n'''
    
    contenido += '      </Document>\n</kml>'

    with open(ruta, 'w') as archivo:
        archivo.write(contenido)



    



        
        

