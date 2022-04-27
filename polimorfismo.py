class Personas:

    def __init__(self, nombre):
        self.nombre = nombre

    def avanza(self):
        print("ando caminando")


class Ciclista(Personas):

    def __init__(self, nombre):
        super().__init__(nombre)

    def avanza(self):
        print("ando en bicicleta")


def main():
    persona = Personas("David")
    persona.avanza()

    ciclista = Ciclista("Andrea")
    ciclista.avanza()

if __name__ == "__main__":
    main()