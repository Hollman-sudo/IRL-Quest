# Ramificaciones IRL Quest
## Plano de las ramas
main
|-features
  |-feature menu principal
  |-feature personaje
  |-feature misiones diarias
  |-feature misiones principales
  |-feature cacerías aleatorias
  |-feature tienda

## Estado actual
| Rama                         | Creada | Contenido 
|------------------------------|--------|-----------------------
| main                         | ✅     | README, REQUISITOS, Anteproyecto 
| feature/menu-principal       | ⬜     | 
| feature/personaje            | ⬜     | 
| feature/misiones-diarias     | ⬜     |    
| feature/misiones-principales | ⬜     | 
| feature/eventos-aleatorios   | ⬜     | 
| feature/tienda               | ⬜     | 

## Comandos
### Crear una nueva funcionalidad/feature
git checkout -b feature/nombre

### Trabajar y guardar cambios
git add .
git commit -m "descripción del avance"

### Subir la rama a GitHub
git push -u origin feature/nombre

### Fusionar feature terminada a main
git checkout main
git merge feature/nombre
git push origin main