class Tomate:
    def tipo(self):
        print("vegetal")

    def color(self):
        print("rojo")


class Manzana:
    def tipo(self):
        print("fruta")

    def color(self):
        print("verde")


def func(obj):
    obj.tipo()
    obj.color()


nuevo_tomate = Tomate()
nueva_manzana = Manzana()

func(nueva_manzana)
func(nuevo_tomate)
