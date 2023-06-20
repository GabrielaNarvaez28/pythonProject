class Pedido ():
    contador_pedido = 0
    contador_id = 0

    def __init__(self, solicitante: str = None, lista_material: str = None, materia: str = None,
                    fecha_prestamo: str = None, fecha_devolucion: str = None):
        Pedido.contador_id += 1
        Pedido.contador_pedido += 1
        self._id = Pedido.contador_pedido
        self._pedido = Pedido.contador_pedido
        self._solicitante = solicitante
        self._lista_material = lista_material
        self._materia = materia
        self._fecha_prestamo = fecha_prestamo
        self._fecha_devolucion = fecha_devolucion

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    @property
    def solicitante(self):
        return self._solicitante

    @solicitante.setter
    def solicitante(self, solicitante):
        self._solicitante = solicitante

    @property
    def lista_material(self):
        return self._lista_material

    @lista_material.setter
    def lista_material(self, lista_material):
        self._lista_material = lista_material

    @property
    def materia(self):
        return self.materia

    @materia.setter
    def materia(self, materia):
        self._materia = materia

    @property
    def fecha_prestamo(self):
        return self._fecha_prestamo

    @fecha_prestamo.setter
    def fecha_prestamo(self, fecha_prestamo):
        self._fecha_prestamo = fecha_prestamo

    @property
    def fecha_devolucion(self):
        return self._fecha_devolucion

    @fecha_devolucion.setter
    def fecha_devolucion(self, fecha_devolucion):
        self._fecha_devolucion = fecha_devolucion

    @property
    def revista(self):
        return self._revista

    @revista.setter
    def revista(self, revista):
        self._revista  = revista

    def __str__(self):
        return f'Pedido: {self.__dict__.__str__()}'

    def pedir_material(self):
        return f'{self._lista_material} {self._solicitante} {self._materia}'

    def devolver_material (self):
        return f'{self._solicitante} '


if __name__ == '__main__':
    #pass
    p1 = Pedido(solicitante='estudiante', lista_material='revista', materia='programacion',
                 fecha_prestamo='02/01/2023', fecha_devolucion='15/01/2023')
    print(p1)
    print(f'Solicitamos el Material {p1._lista_material} Solicitante:{p1._solicitante} Materia {p1._materia}')
    print (f'Devuelve el material {p1._solicitante}')
    # , debito=200.00)
    # print(obj)

