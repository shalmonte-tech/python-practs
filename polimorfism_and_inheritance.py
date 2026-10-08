class Aves:
    def volar(self):
        print("la mayoria de las aves vuelan pero algunas no.")


class Aguilas(Aves):
    def volar(self):
        print("Las aguilas pueden volar")


class Gallina(Aves):
    def volar(self):
        print("las gallinas no pueden volar")


obj_ave = Aves()
obj_ave.volar()

obj_aguila = Aguilas()
obj_aguila.volar()

obj_gallina = Gallina()
obj_gallina.volar()
