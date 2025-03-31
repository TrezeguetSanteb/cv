# Sistema de Batalla Pokémon

Un sistema de batalla Pokémon implementado en Java utilizando programación orientada a objetos. El proyecto simula combates entre entrenadores Pokémon con mecánicas similares a los juegos originales, incluyendo tipos, efectividad, habilidades, objetos y condiciones climáticas.

## Características

- Sistema de batalla por turnos
- Múltiples tipos de Pokémon con relaciones de efectividad entre ellos
- Habilidades con diferentes efectos y potencias
- Items que pueden ser utilizados durante la batalla
- Condiciones climáticas que afectan el desarrollo del combate
- Carga de datos desde archivos JSON para fácil configuración y extensibilidad

## Requisitos

- Java 11 o superior
- Maven para gestión de dependencias (opcional)

## Estructura del proyecto

- **org.pokemon.model**: Clases que representan las entidades del juego (Pokemon, Jugador, Clima)
- **org.pokemon.model.acciones**: Clases para las acciones posibles (habilidades e items)
- **org.pokemon.controller**: Controladores que manejan la lógica del juego
- **org.pokemon.utilidades**: Clases utilitarias para lectura de archivos y operaciones comunes
- **resources**: Archivos de configuración en formato JSON

### Archivos principales

- **Main.java**: Punto de entrada del programa
- **habilidades.json**: Define las habilidades disponibles para los Pokémon
- **items.json**: Define los objetos que pueden usar los jugadores
- **efectividad_tipos.json**: Define las relaciones de efectividad entre tipos
- **pokemons.json**: Define los Pokémon disponibles con sus características
- **jugadores.json**: Define los jugadores con sus equipos Pokémon e inventarios

## Instalación

1. Clone el repositorio:
   ```
   git clone https://github.com/tu-usuario/pokemon-battle-system.git
   ```

2. Navegue al directorio del proyecto:
   ```
   cd pokemon-battle-system
   ```

3. Compile el proyecto:
   ```
   javac org/pokemon/Main.java
   ```
   
   O si usa Maven:
   ```
   mvn compile
   ```

## Uso

Para iniciar el juego, ejecute:

```
java org.pokemon.Main
```

O con Maven:

```
mvn exec:java -Dexec.mainClass="org.pokemon.Main"
```

### Flujo del juego

1. El sistema carga los datos desde los archivos JSON (climas, habilidades, items, Pokémon y jugadores)
2. Se inicia la batalla con los jugadores configurados
3. Por cada turno, los jugadores pueden elegir entre usar una habilidad, usar un objeto, o cambiar de Pokémon
4. La batalla continúa hasta que todos los Pokémon de un jugador sean derrotados

## Personalización

### Añadir nuevos Pokémon

Para añadir nuevos Pokémon, edite el archivo `pokemons.json` siguiendo la estructura establecida:

```json
{
  "id": 1,
  "nombre": "Pikachu",
  "tipos": ["ELECTRICO"],
  "estadisticas": {
    "hp": 35,
    "ataque": 55,
    "defensa": 40,
    "velocidad": 90
  },
  "habilidades": [1, 2, 3, 4]
}
```

### Añadir nuevas habilidades

Para añadir nuevas habilidades, edite el archivo `habilidades.json`:

```json
{
  "id": 1,
  "nombre": "Impactrueno",
  "tipo": "ELECTRICO",
  "potencia": 40,
  "precision": 100,
  "efectoSecundario": {
    "efecto": "PARALIZAR",
    "probabilidad": 10
  }
}
```

### Añadir nuevos items

Para añadir nuevos items, edite el archivo `items.json`:

```json
{
  "id": 1,
  "nombre": "Poción",
  "efecto": "CURAR",
  "potencia": 20
}
```

## Estructura de clases

### Modelo

- `Pokemon`: Representa un Pokémon con sus estadísticas y habilidades
- `Jugador`: Representa un entrenador con su equipo Pokémon e inventario
- `Clima`: Representa condiciones climáticas que afectan la batalla

### Acciones

- `Accion`: Clase abstracta que representa una acción en el juego
- `Habilidad`: Extiende Accion, representa una habilidad de Pokémon
- `Item`: Extiende Accion, representa un objeto que puede ser usado

### Controlador

- `JuegoControlador`: Maneja la lógica del juego y coordina la batalla

### Utilidades

- `Utilidades`: Proporciona métodos para cargar datos desde archivos JSON

## Contribuir

Si deseas contribuir a este proyecto, por favor:

1. Haz un fork del repositorio
2. Crea una rama para tu funcionalidad (`git checkout -b nueva-funcionalidad`)
3. Realiza tus cambios y haz commit (`git commit -m 'Agrega nueva funcionalidad'`)
4. Sube tus cambios (`git push origin nueva-funcionalidad`)
5. Abre un Pull Request

## Posibles mejoras

- Implementar una interfaz gráfica más elaborada
- Añadir más Pokémon, habilidades y objetos
- Implementar estados alterados adicionales (quemado, envenenado, etc.)
- Añadir modos de juego adicionales (batallas dobles, batallas contra la IA)
- Mejorar la IA de los oponentes controlados por la computadora

## Licencia

Este proyecto está licenciado bajo la Licencia MIT - ver el archivo LICENSE para más detalles.

## Créditos

- Pokémon y todos los personajes relacionados son propiedad de Nintendo, Game Freak y The Pokémon Company
- Este proyecto es solo para fines educativos y no tiene afiliación con las entidades mencionadas anteriormente