from figura_geometrica import  FiguraGeometrica

class Triangulo(FiguraGeometrica):
    def __init__(self, lado:float=0.0):
        super().__init__(ancho=lado, alto=lado)

    def __str__(self):
        return f'Triangulo [lado = {self.alto}]'

    def calcular_area(self):
        return (self.alto * self.ancho)/2

    def calcular_perimetro(self):
        return 3 * self.alto

if __name__ == '__main__':
    c1 =  Triangulo(lado=3)
    print(c1)
    print(f'El área del Triangulo es: {c1.calcular_area()}')
    print(f'El perimetro del Triangulo es: {c1.calcular_perimetro()}')