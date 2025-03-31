#!/usr/bin/python3.

import sys
import comandos
from grafo import Grafo
import auxiliares as aux

def main():
    ruta_aeropuerto = sys.argv[1] 
    ruta_vuelos = sys.argv[2]
    grafo = Grafo(False) #grafo
    grafo, dic_ciudades, dic_codigos = aux.leer_aeropuerto(grafo, ruta_aeropuerto)
    grafo = aux.leer_vuelos(grafo, ruta_vuelos, dic_codigos)
    lugares = [] 
    ultimo_comando = ""
    while True:
        usuario = input()
        if usuario == "":
            return 
        comando, arg = usuario.split(" ",1)
        arg = arg.split(",")
        if comando == "camino_mas":
            modo, origen, destino = arg[0], arg[1], arg[2]
            lugares = comandos.camino_mas(grafo, dic_ciudades, origen, destino, modo)
        elif comando == "camino_escalas":
            origen, destino = arg[0], arg[1]
            lugares = comandos.camino_escalas(grafo, dic_ciudades, origen, destino)
        elif comando == "centralidad":
            cant = int(arg[0])
            comandos.centralidad_c(grafo, cant)
        elif comando == "nueva_aerolinea":
            ruta_vuelos = arg[0]
            comandos.nueva_aerolinea(grafo, ruta_vuelos)
        elif comando == "itinerario":
            ruta_itinerario = arg[0]
            comandos.itinerario(grafo, dic_ciudades, ruta_itinerario)
        elif comando == "exportar_kml":
            ruta_kml = arg[0]
            comandos.exportar_kml(lugares, dic_codigos, ultimo_comando, ruta_kml)
        ultimo_comando = comando

main()   