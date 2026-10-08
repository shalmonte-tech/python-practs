class Pastel:
    def __init__(self, ingredientes, tamaño):
        self.ingredientes = ingredientes
        self.tamaño = tamaño

    def __repr__(self):
        return f"Pastel({self.ingredientes}, " f"{self.tamaño}"

    def area(self):
        return self.tamaño_area(self.tamaño)

    @staticmethod
    def tamaño_area(A):
        import math

        return A * math.pi * 2


nuevo_pastel = Pastel(["harina", "azucar", "leche", "crema"], 4)
print(nuevo_pastel.ingredientes)
print(nuevo_pastel.tamaño)
print(nuevo_pastel.tamaño_area(24))
