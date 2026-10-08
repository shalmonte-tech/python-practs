curso = "python"
print("tutoriales de % s" % curso)

nombre = "victor"
edad = 25

print("hola soy, % s  y tengo % s años." % (nombre, edad))
print(f"hola soy {nombre} y tengo {edad}.")
print("que tal soy {} y mi edad es {} años.".format(nombre, edad))
print(f"que tal soy {nombre} y mi edad es {edad} años.")


class Estudiante:
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    def __str__(self):
        return f"{self.nombre} {self.apellido} {self.edad}"


nuevo_estudiante = Estudiante("victor", "cruz", 27)
print(f"{nuevo_estudiante}")
