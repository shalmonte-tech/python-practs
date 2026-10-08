class Persona:
    def __init__(self, nom, age):
        self.nombre = nom
        self.age = age

    def descript(self):
        return f"{self.nombre} tiene {self.age}"

    def comentario(self, phrase):
        return f"{self.nombre} dice {phrase}"


doctor = Persona("victor", 28)
print(doctor.descript())
print(doctor.comentario("me gusta la medicina"))


class Correo:
    def __init__(self):
        self.enviado = False

    def set_enviado(self):
        self.enviado = True


mi_correo = Correo()
print(f"el correo {"si" if mi_correo.enviado == True else "no"} ha sido enviado")
mi_correo.set_enviado()
print(f"el correo {"si" if mi_correo.enviado == True else "no"} ha sido enviado")
