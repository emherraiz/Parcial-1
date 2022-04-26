class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

class Vertebrado(Animal):
    def __init__(self, nombre, tipo):
        super().__init__(nombre)
        self.tipo = tipo


class Incuvacion(Vertebrado):
    def __init__(self, nombre, tipo, oviparidad):
        super().__init__(nombre, tipo)
        self.oviparidad = oviparidad

Animal = Animal('Nombre del animal')
Mamifero = Vertebrado(Animal.nombre, 'Mamifero')
Ovíparo = Incuvacion(Mamifero.nombre, Mamifero.tipo, 'Ovíparo')

# Gato
Gato_animal = Animal('Gato')
Gato_mamifero = Vertebrado(Gato_animal.nombre, 'Mamífero')
Gato = Incuvacion(Gato_mamifero.nombre, Gato_mamifero.tipo, 'Viviparo')

# Pollo
Pollo = Incuvacion('Pollo', 'Ave', 'Oviparo')

# Ornitorrinco
Ornitorrinco = Incuvacion('Ornitorrinco', 'Mamifero', 'Oviparo')




