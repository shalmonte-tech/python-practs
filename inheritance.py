class pokemon:
    pass

    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo

    def descript(self):
        return f"{self.nombre} es un pokemon de tipo: {self.tipo}"


class pikachu(pokemon):
    def ataque(self, ataque):
        return f"{self.nombre} hizo un ataque: {ataque}"


class charmander(pokemon):
    def ataque(self, ataque):
        return f"{self.nombre} hizo un ataque: {ataque}"


nuevo_pokemon = pikachu("bubba", "electrico")
nuevo_pokemon2 = charmander("fidodido", "fuego")

print(nuevo_pokemon.descript())
print(nuevo_pokemon2.descript())

print(nuevo_pokemon.ataque("Cola de hierro"))
print(nuevo_pokemon2.ataque("Llamarada"))
