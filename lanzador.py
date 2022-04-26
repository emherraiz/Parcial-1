from Ejercicios.Ejercicio_1 import Libro, Coleccion
from Ejercicios.Ejercicio_2 import Animal, Vertebrado, Gestacion
from Ejercicios.Ejercicio_3 import Cuenta, Cuenta_plazo_fijo, Cuenta_vip
import random

# Estas listas se podrían hacer clases también, sería volviendo a usar nuevamente la herencia como hemos utilizado en el ejercicio
biblioteca = []
animales = []

opcion = 0
while opcion < 4:
    # Ejercicio 1:
    opcion = int(input('A que ejercicio quieres acceder:\n1 - Libros\n2 - Animales\n3 - Cuentas Bancarias\n'))
    if opcion == 1:
        nombre_coleccion = input('Introduce el nombre de la coleccion:\n')
        coleccion = Coleccion(nombre_coleccion)
        n = int(input('Numero de libros que contiene nuestra coleccion:\n'))
        for i in range(n):
            nombre = input(f'Nombre del libro {i+1}\n')
            autor = input('Autor:\n')
            tipo = input('Tipo de libro:\n')
            añadir_mas_generos = True
            generos = []
            while añadir_mas_generos:
                genero = input('Genero:')
                generos.append(genero)
                s = input('Si desea seguir añadiendo mas generos pulse <s>: ')
                if s != 's':
                    añadir_mas_generos = False

            libro = Libro(nombre, autor, tipo)
            libro.añadir_genero(generos)
            coleccion.añadir_libros(libro)

        biblioteca.append(coleccion)

    elif opcion == 2:
        nombre = input('Introduce el nombre del animal:\n')
        vertebrado = input('Introduce el tipo de vertebrado:\n')
        oviparidad = input('¿Es ovíparo o vivíparo?\n')
        animal = Gestacion(nombre, vertebrado, oviparidad)
        animales.append(animal)

    elif opcion == 3:
        



