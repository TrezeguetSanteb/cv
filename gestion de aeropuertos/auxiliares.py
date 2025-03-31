import aeropuertos_vuelos as air
from grafo import Grafo

MAX = float('inf')
RAPIDO = "rapido"

def cmp_min(a, b):
    num1, _ = a
    num2, _ = b
    return num2-num1

def cmp_max(a, b):
    num1, _ = a
    num2, _ = b
    return num1-num2

def cmp_min_precio(a, b):
    num1, _ = a
    num2, _ = b
    return num2.ver_precio() - num1.ver_precio()

def leer_aeropuerto(grafo, ruta):
    dic_ciudades = {}
    dic_codigos = {}
    with open(ruta, 'r')as arch:
        for linea in arch:
            linea = linea.rstrip()
            ciudad, codigo, latitud, longitud = linea.split(",")
            aeropuerto = air.aeropuerto(ciudad, codigo, latitud, longitud)
            ciudad_lista = dic_ciudades.get(ciudad, [])
            ciudad_lista.append(aeropuerto)  
            dic_ciudades[ciudad] = ciudad_lista
            dic_codigos[codigo] = aeropuerto
            grafo.agregar_vertice(aeropuerto)
        return grafo, dic_ciudades, dic_codigos
            
def leer_vuelos(grafo, ruta, dic_codigos):
     with open(ruta, 'r')as arch:
        for linea in arch:
            linea = linea.rstrip()
            aeropuerto_i,aeropuerto_j,tiempo,precio,cant_vuelos = linea.split(",")
            vuelo = air.vuelo(tiempo, precio, cant_vuelos)
            grafo.agregar_arista(dic_codigos[aeropuerto_i], dic_codigos[aeropuerto_j], vuelo)
        return grafo
     
def leer_itinerario(grafo, archivo):
    with open(archivo, 'r') as file:
        lineas = file.readlines()
    
        ciudades = lineas[0].rstrip().split(',')
        restricciones = []
        for linea in lineas[1:]:
            linea = linea.rstrip()
            restricciones.append((linea.split(",")))

        grafo_restricciones = Grafo(True)

        for ciudad in ciudades:
            grafo_restricciones.agregar_vertice(ciudad)

        for restriccion in restricciones:
            ciudad_i, ciudad_j = restriccion
            grafo_restricciones.agregar_arista(ciudad_i, ciudad_j, 1)

    return grafo_restricciones

def mostrar_camino(padre, origen, destino):
    res = [destino.ver_codigo()]
    while destino != origen:
        destino = padre[destino]
        res.append(destino.ver_codigo())
    res.reverse()
    imprimir(res)
    return res

def imprimir(lista):
     for i in range(len(lista)):
        if i == len(lista)-1:
            print(lista[i])
            return
        print(lista[i] + "->", end='')

