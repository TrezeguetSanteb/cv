# Sokoban - Juego de Puzzles

Sokoban es una implementación en Python del clásico juego de puzzles japonés donde el jugador debe empujar cajas hasta posiciones objetivo dentro de un almacén. Esta versión incluye una interfaz gráfica, múltiples niveles y un algoritmo de resolución automática.

## Características

- Interfaz gráfica con sprites
- Múltiples niveles cargados desde archivos externos
- Sistema de controles configurables
- Funcionalidad de deshacer/rehacer movimientos
- Algoritmo de backtracking para resolución automática de niveles
- Reinicio de niveles

## Requisitos

- Python 3.x
- Biblioteca gamelib (incluida o instalable mediante pip)

## Estructura del proyecto

- **main.py**: Programa principal que gestiona la interfaz gráfica y la lógica del juego
- **soko.py**: Implementación de las reglas del juego y manipulación del tablero
- **pila.py**: Implementación de la estructura de datos de pila para las funciones de deshacer/rehacer
- **backtracking.py**: Algoritmo para encontrar soluciones automáticas
- **niveles.txt**: Archivo con la definición de los niveles
- **teclas.txt**: Configuración de los controles
- **img/**: Directorio con los archivos gráficos (sprites)

## Instalación

1. Clone el repositorio:
   ```
   git clone https://github.com/tu-usuario/sokoban.git
   ```

2. Navegue al directorio del proyecto:
   ```
   cd sokoban
   ```

3. Asegúrese de tener todas las dependencias instaladas:
   ```
   pip install -r requirements.txt
   ```
   
   (Nota: si no hay un archivo requirements.txt, asegúrese de tener instalada la biblioteca gamelib)

## Uso

Para iniciar el juego, ejecute:

```
python main.py
```

### Controles predeterminados

Los controles se pueden configurar en el archivo `teclas.txt`, pero por defecto son:

- **Flechas de dirección**: Mover al jugador
- **Z**: Deshacer movimiento
- **Y**: Rehacer movimiento
- **B**: Buscar solución automática
- **A**: Aplicar siguiente movimiento de la solución
- **R**: Reiniciar nivel
- **Esc**: Salir del juego

### Formato de los archivos

#### Archivo de niveles (niveles.txt)
```
Level 1
######## 
#  . #  #
#   #   #
# $   $ #
#   # @ #
#  .    #
########

Level 2
...
```

Donde:
- `#`: Representa una pared
- `@`: Representa al jugador
- `$`: Representa una caja
- `.`: Representa un objetivo
- ` `: Representa un espacio vacío

#### Archivo de teclas (teclas.txt)
```
Up = NORTE
Down = SUR
Right = ESTE
Left = OESTE
z = DESHACER
y = REHACER
b = BUSCAR
a = APLICAR
```

## Funcionamiento

### Sistema de juego
El juego consiste en mover al personaje por el tablero para empujar cajas hacia posiciones objetivo. Una vez que todas las cajas están sobre objetivos, el nivel se completa y se avanza al siguiente.

### Algoritmo de resolución
El juego incluye un algoritmo de backtracking que encuentra automáticamente una solución para el nivel actual. Esta solución se puede aplicar paso a paso con la tecla correspondiente.

### Sistema de deshacer/rehacer
Se implementa utilizando dos pilas para almacenar los estados previos y posteriores del tablero, permitiendo al jugador deshacer movimientos incorrectos y rehacerlos si es necesario.

## Personalización

### Añadir nuevos niveles
Para añadir nuevos niveles, edite el archivo `niveles.txt` siguiendo el formato establecido. Asegúrese de separar cada nivel con una línea en blanco y añadir un título "Level X" antes de cada definición.

### Modificar controles
Edite el archivo `teclas.txt` para cambiar las teclas asignadas a cada acción. El formato es `tecla = ACCION`.

## Contribuir

Si deseas contribuir a este proyecto, por favor:
1. Haz un fork del repositorio
2. Crea una rama para tu funcionalidad (`git checkout -b nueva-funcionalidad`)
3. Realiza tus cambios y haz commit (`git commit -m 'Agrega nueva funcionalidad'`)
4. Sube tus cambios (`git push origin nueva-funcionalidad`)
5. Abre un Pull Request

## Créditos

- Las imágenes utilizadas para los sprites pueden estar sujetas a derechos de autor de sus respectivos creadores.
- El concepto original de Sokoban fue creado por Hiroyuki Imabayashi en 1981.

## Licencia

Este proyecto está licenciado bajo la Licencia MIT - ver el archivo LICENSE para más detalles.