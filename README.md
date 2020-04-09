# Curso de Python

Este repositorio recopila los ejemplos realizados durante las sesiones del curso de python impartido por Namtrik Development.

## Contenido

* `introduction`: ejercicios de introducción a Python como manejo de variables, cadenas, listas, funciones, etc.
* `oop`: ejercicios de programación orientada a objetos en Python.
* `geekside`: proyecto django.

## Proyecto django

Para ejecutar el proyecto django en local ejecuta los siguientes comandos en una terminal dentro del directorio del proyecto.

```shell
pipenv install
pipenv shell
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
python manage.py loaddata fixture.json
```