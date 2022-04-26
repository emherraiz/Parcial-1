class Coleccion():
    def __init__(self, nombre_coleccion):
        self.nombre_coleccion = nombre_coleccion
        self.libros = []

    def añadir_libros(self, libro):
        if type(libro) is list:
            for i in libro:
                self.libros.append(i)
        else:
            self.libros.append(libro)

    def get_nombre_coleccion(self):
        return self.nombre_coleccion

    def __str__(self):
        print(f'Nuestra coleccion {self.nombre_coleccion} contiene los siguientes libros:')
        for i in self.libros:
            print(f'- {i}')

        return '\nEsta seria nuestra colección'


class Libro:
    def __init__(self, nombre, autor, tipo_de_libro):
        self.nombre = nombre
        self.autor = autor
        self.tipo_de_libro = tipo_de_libro
        self.genero = []

    def get_nombre(self):
        return self.nombre

    def get_autor(self):
        return self.autor

    def get_tipo_de_libro(self):
        return self.tipo_de_libro

    def añadir_genero(self, genero):
        if type(genero) is not list:
            self.genero.append(genero)
        else:
            for i in genero:
                self.genero.append(i)

    def get_genero(self):
        return self.genero

    def __str__(self):
        return f'{self.nombre}'

Asterix = Coleccion('Asterix')

Asterix_1 = Libro('Asterix y Obelix', 'Albert Uderzo', 'Comic')
Asterix_1.añadir_genero(['Aventuras', 'Historia'])

Asterix_2 = Libro('Asterix y Obelix en los Juegos Olímpicos', 'Albert Uderzo', 'Comic')
Asterix_2.añadir_genero(['Aventuras', 'Historia', 'Deportes'])


Asterix.añadir_libros([Asterix_1, Asterix_2])

