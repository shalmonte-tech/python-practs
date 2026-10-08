class Ropa:
    def __init__(self):
        self.marca = "willow"
        self.talla = "M"
        self.color = "rojo"


camisa = Ropa()
print(camisa.talla, camisa.color, camisa.marca)


class Calc:
    def __init__(self, n1, n2):
        self.suma = n1 + n2
        self.resta = n1 - n2
        self.producto = n1 * n2
        self.division = n1 / n2

operacion = Calc(10, 2)
print(operacion.division, operacion.producto, operacion.suma, operacion.resta)
