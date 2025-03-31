# FlyCombi - Sistema de Gestión de Rutas Aéreas

FlyCombi es una aplicación de línea de comandos que permite la gestión y análisis de rutas aéreas entre distintos aeropuertos. El sistema permite consultar información sobre rutas óptimas, analizar la importancia de los aeropuertos en la red de vuelos y gestionar itinerarios.

## Requisitos

- Python 3.x
- Bibliotecas estándar de Python (no requiere instalaciones adicionales)

## Estructura del proyecto

- **flycombi.py**: Programa principal que procesa los comandos del usuario
- **grafo.py**: Implementación de la estructura de datos de grafo
- **comandos.py**: Funciones que implementan cada uno de los comandos disponibles
- **auxiliares.py**: Funciones auxiliares para la lectura de archivos y procesamiento de datos

## Instalación

1. Clone el repositorio:
   ```
   git clone https://github.com/tu-usuario/flycombi.git
   ```

2. Navegue al directorio del proyecto:
   ```
   cd flycombi
   ```

## Uso

El programa se ejecuta desde la línea de comandos, recibiendo como parámetros las rutas a los archivos de datos:

```
python3 flycombi.py <archivo_aeropuertos> <archivo_vuelos>
```

Donde:
- `<archivo_aeropuertos>`: Archivo CSV con la información de los aeropuertos
- `<archivo_vuelos>`: Archivo CSV con la información de los vuelos

### Formato de los archivos

#### Archivo de aeropuertos
```
ciudad,codigo,latitud,longitud
```

#### Archivo de vuelos
```
aerolinea,origen,destino,tiempo_promedio,precio,cant_vuelos
```

### Comandos disponibles

Una vez iniciado el programa, se pueden ejecutar los siguientes comandos:

#### 1. Camino más rápido/barato
```
camino_mas rapido,origen,destino
camino_mas barato,origen,destino
```
Encuentra la ruta más rápida o económica entre dos ciudades.

#### 2. Camino con menos escalas
```
camino_escalas origen,destino
```
Encuentra la ruta con menor cantidad de escalas entre dos ciudades.

#### 3. Análisis de centralidad
```
centralidad n
```
Muestra los `n` aeropuertos más importantes según su centralidad en la red.

#### 4. Agregar nueva aerolínea
```
nueva_aerolinea archivo_rutas
```
Agrega nuevas rutas de vuelo al sistema desde un archivo.

#### 5. Procesar itinerario
```
itinerario archivo_itinerario
```
Procesa un archivo de itinerario con múltiples consultas.

#### 6. Exportar a KML
```
exportar_kml archivo_salida
```
Exporta la última ruta calculada a un archivo KML para visualizarla en Google Earth.

## Ejemplos de uso

```
$ python3 flycombi.py aeropuertos.csv vuelos.csv
camino_mas rapido,Buenos Aires,Madrid
camino_escalas Buenos Aires,Nueva York
centralidad 5
exportar_kml ultima_ruta.kml
```

## Estructura de los datos

### Aeropuertos
Los aeropuertos se representan en un grafo donde cada nodo corresponde a un aeropuerto con su código IATA y las aristas representan los vuelos disponibles entre ellos.

### Vuelos
Los vuelos son las conexiones entre aeropuertos, con atributos como tiempo de vuelo, precio y frecuencia.

## Consideraciones de rendimiento

- La búsqueda de rutas óptimas utiliza el algoritmo de Dijkstra para encontrar el camino más corto
- El cálculo de centralidad utiliza algoritmos de análisis de redes para determinar la importancia de cada nodo
- La estructura de grafo permite operaciones eficientes para redes de aeropuertos de gran escala

## Contribuir

Si deseas contribuir a este proyecto, por favor:
1. Haz un fork del repositorio
2. Crea una rama para tu funcionalidad (`git checkout -b nueva-funcionalidad`)
3. Realiza tus cambios y haz commit (`git commit -m 'Agrega nueva funcionalidad'`)
4. Sube tus cambios (`git push origin nueva-funcionalidad`)
5. Abre un Pull Request

## Licencia

Este proyecto está licenciado bajo la Licencia MIT - ver el archivo LICENSE para más detalles.
