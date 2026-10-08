class Telefono:
    def __init__(self):
        pass

    def llamar(self):
        print("llamando...")

    def ocupado(self):
        print("ocupado...")


class Camara:
    def __init__(self):
        pass

    def tomar_foto():
        print("tomando foto...")


class Reproduccion:
    def __init__(self):
        pass

    def reproducir_musica(self):
        print("reproduciendo música...")

    def reproducir_video(self):
        print("reproducir un video...")


class smartphone(Telefono, Camara, Reproduccion):
    def __del__(self):
        print("telefono apagado")


movil = smartphone()
movil.llamar()
movil.ocupado()
movil.tomar_foto()
movil.reproducir_video()