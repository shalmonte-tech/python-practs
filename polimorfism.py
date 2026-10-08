class Animales:
    def __init__(self, nombre):
        self.nombre = nombre

    def tipo_animal(self):
        pass


class Leon(Animales):
    def tipo_animal(self):
        print("Animal salvaje")


class Perro(Animales):
    def tipo_animal(self):
        print("Animal domestico")


nuevo_animal = Leon("charli")
nuevo_animal = Perro("tobby")
