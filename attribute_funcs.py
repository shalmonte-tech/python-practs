class Persona:
    edad = 27
    nombre = "victor"


doctor = Persona()
print("la edad es", doctor.edad)
print("su nombre es", doctor.nombre)

print("El doctor tiene edad?", "Si" if hasattr(doctor, "edad") == True else "no")
print("El doctor tiene auto?", "Si" if hasattr(doctor, "auto") == True else "no")

setattr(doctor, "nombre", "charlie")
print("ahora su nombre es:", doctor.nombre)

setattr(doctor, "telefono", "samsung")
print("el telefono del doctor es: ", doctor.telefono)

delattr(doctor, "telefono")
print("(atributo telefono borrado)")
print(
    "el doctor tiene telefono?", "Si" if hasattr(doctor, "telefono") == True else "no"
)
