class Calc:
    def __init__(self, numero):
        self.n = numero
        self.datos = [0 for i in range(numero)]

    def ingresar_datos(self):
        self.datos = [
            int(input("Ingresar datos" + str(i + 1) + "= ")) for i in range(self.n)
        ]


class op_basicas(Calc):
    def __init__(
        self,
    ):
        Calc.__init__(self, 2)

    def suma(self):
        a, b = self.datos
        s = a + b
        print("el resultado es", s)

    def resta(self):
        a, b = self.datos
        s = a - b
        print("el resultado es", s)

    def mult(self):
        a, b = self.datos
        s = a * b
        print("el resultado es", s)

    def division(self):
        a, b = self.datos
        s = a / b
        print("el resultado es", s)


class raiz(Calc):
    def __init__(self):
        Calc.__init__(self, 1)

    def cuadrada(self):
        import math

        (a,) = self.datos
        print(f"el resulado es:", math.sqrt(a))


ejemplo = op_basicas()
ejemplo.ingresar_datos()
ejemplo.suma()
ejemplo.division()
ejemplo.mult()
ejemplo.resta()
