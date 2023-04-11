# Taller Evaluable 2 - Programa de Backup

## Estudiante:

Pascual Gomez Londoño, pgomezl@eafit.edu.co

Profesor:

Edison Valencia Diaz, evalenci@eafit.edu.co


## Objetivo

El objetivo de esta práctica evaluable es crear un programa que permita realizar una copia de seguridad de una carpeta en fragmentos de 512 MB, y otro programa que permita restaurar la copia de seguridad a su estado original. El programa debe ser capaz de trabajar con archivos de cualquier tamaño.


## Requisitos

Python 3.10.10 instalado.


## Ejecutar

###
#### Crear copia de seguridad

Para crear la copia de seguridad de la carpeta objetivo correr el comando:
```bash
createbackup.py folder_to_backup\ target_path\
```

Si se desea crear una copia de seguridad de la carpeta "folder1" en la carpeta "output", el comando sería:
```bash
createbackup.py folder1\ output\
```

###
#### Restaurar copia de seguridad

Para restaurar la copia de seguridad de la carpeta objetivo correr el comando:
```bash
restorebackup.py backup_folder\ target_path\
```

Si se desea restaurar una copia de seguridad que está en la carpeta "backup" y se va a ubicar en la carpeta "output", el comando sería:
```bash
createbackup.py backup\ output\
```

#### version README.md -> 1.0 (2023-abril)
