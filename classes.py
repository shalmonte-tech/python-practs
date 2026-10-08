from dataclasses import dataclass


@dataclass
class Auto:
    marca: str = ""
    modelo: int = 0
    placa: str = ""


taxi = Auto(marca="Audi", modelo=1829, placa="KJ43LA1")
print(taxi.marca, taxi.modelo, taxi.placa)
