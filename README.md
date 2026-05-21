# IRL Quest - Sistema de Hábitos RPG

## Descripción
IRL Quest es una aplicación CLI que convierte las tareas y hábitos diarios en misiones estilo RPG. Sube de nivel, mejora estadísticas, caza monstruos y completa misiones principales antes de que expiren.

## Instalación
```bash
git clone https://github.com/Hollman-sudo/IRL-Quest.git
cd IRL-Quest
python3 src/main.py
```

## Requisitos
1. Python 3.6 o superior
2. Linux (cualquier distro)

## Uso rápido
1. Ejecuta python3 src/main.py
2. Crea tu personaje (nombre)
3. Crea misiones diarias o principales
4. Complétalas para ganar puntos
5. Enfréntate a monstruos en eventos aleatorios
6. Usa "Nuevo día" para reiniciar misiones diarias, obtener las recompensas de las misiones y aplicar penalizaciones
7. Guarda tu partida cuando quieras para no perder tu progreso


## Características
* 11 estadísticas (fuerza, velocidad, etc.)
* Sistema de rangos (F a S) según promedio de las estadísticas
* Misiones diarias con recompensa y penalización
* Misiones principales con fecha límite
* Eventos aleatorios (combate por turnos)
* Guardado y carga en JSON


## Herramientas utilizadas

| Herramienta | ¿Por qué es libre? | ¿Por qué la elegí? |
|-------------|--------------------|--------------------|
| **GNU/Linux (Ubuntu)** | Kernel Linux bajo GPL, sistema completo de software libre. | Porque es el estándar en el curso, es bastante fácil de usar y aprender la terminal. |
| **Terminal (Bash)** | Parte del proyecto GNU, licencia GPL. | Para ejecutar el programa, manejar Git y manejo de archivos. |
| **Git** | Licencia GPLv2. | Control de versiones y trabajo colaborativo. |
| **GitHub** | Plataforma que aloja repositorios libres (no es software libre). | Para alojar el proyecto y demostrar uso de Git. |
| **Python 3** | Licencia PSF. | Lenguaje sencillo para principiantes, con bibliotecas estándar libres. |

## Licencias

### Licencia del proyecto: GPLv3
El código fuente de IRL Quest está bajo **GNU General Public License versión 3**. Esto garantiza las cuatro libertades del software libre: usar, estudiar, compartir y modificar el programa.

### Licencias separadas de `json`, `os`, `random`
Estos módulos son parte de la **biblioteca estándar de Python**. Su licencia es la **Python Software Foundation License (PSFL)**, que es compatible con la GPL. No requieren archivos de licencia adicionales porque ya están incluidos en la distribución oficial de Python y su uso no impone restricciones adicionales al proyecto.

## 4. Alcance del proyecto (cumplimiento de requisitos)

| Requisito original | Estado | Notas |
|-------------------|--------|-------|
| Crear personaje con nombre, edad, peso, estatura | ✅ Completo | Se pide nombre; edad, peso, estatura puedo añadirlas fácilmente. |
| 11 estadísticas iniciales en 0 | ✅ Completo | Fuerza, velocidad, defensa, etc. |
| Misiones diarias con dificultad y recompensa | ✅ Completo | El usuario elige estadística, puntos y oro. |
| Misiones principales con fecha límite | ✅ Completo | Se ingresan días límite, se penaliza al usuario si expiran. |
| Subir estadísticas con experiencia | ✅ Completo | Completar misiones otorga puntos directamente. |
| Perder vida si no se cumplen misiones | ✅ Completo | Al usar "Nuevo día" se penaliza. |
| Eventos aleatorios (cacerías) | ✅ Completo | Monstruos con condiciones físicas, combate por turnos. |
| Menú principal y guardado | ✅ Completo | Menú interactivo, guardado en JSON. |
| Rango (F, E, D, C, B, A, S) | ✅ Completo | Calculado según suma de estadísticas. |
