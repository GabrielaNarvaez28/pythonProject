from Biblioteca.pedido import Pedido
from Biblioteca.persona import Persona


class Estudiante(Persona, Pedido):
    contador_estudiante = 0
    contador_id = 0

    def __init__(self, nivel: int = " ", cedula: str = " ", nombre: str = None, apellido: str = None,
                  email: str = None, telefono: str = None, direccion: str = None, numero_libro: int = None,
                 activo: bool = None, carrera: str = None, pedir_libro: bool = None,devolver_libro: bool = None,
                 solicitante : str = None, lista_material: str = None, materia: str = None, fecha_prestamo: str = None,
                 fecha_devolucion: str = None):
        Persona.__init__(self,cedula=cedula,nombre=nombre, apellido=apellido,
                  email=email, telefono=telefono, direccion=direccion, numero_libro=numero_libro, activo=activo,
                         carrera=carrera, pedir_libro=pedir_libro,devolver_libro=devolver_libro)
        Pedido.__init__(self, solicitante=solicitante, lista_material=lista_material, materia=materia,
                        fecha_prestamo=fecha_prestamo, fecha_devolucion=fecha_devolucion)
        Estudiante.contador_estudiante += 1
        Estudiante.contador_id += 1
        self._nivel = nivel
        self._id = Estudiante.contador_id
        self._estudiante = Estudiante.contador_estudiante

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    @property
    def nivel(self):
        return self._nivel

    @nivel.setter
    def nivel(self, nivel):
        self._nivel = nivel

    @property
    def estudiante(self):
        return self._estudiante

    @estudiante.setter
    def estudiante(self, estudiante):
        self._estudiante = estudiante

    def solicitar_material(self):
        return f'{self._devolver_libro} {self._pedir_libro}'

    def __str__(self):
        return f'Estudiante: {self.__dict__.__str__()}, Pedido: {self.__dict__.__str__()}'


if __name__ == '__main__':
    e1 = Estudiante(cedula='0956341366', nombre='wendy', apellido='caicedo', email='wendycaicedo74@gmail.com',
                    telefono='0968662960', direccion='nobol', numero_libro=5, activo=True, carrera='GIG', nivel=2,
                    pedir_libro=True, devolver_libro=False, solicitante='estudiante', lista_material='revista',
                    materia='programacion', fecha_prestamo='02/01/2023', fecha_devolucion='15/01/2023')

    print(e1)
    print(f'Se pidio el libro {e1._pedir_libro} devolvieron el libro {e1._devolver_libro}')
    e2 = Estudiante(cedula='098754679', nombre='tatiana', apellido='caicedo', email='tatianac@gmail.com',
                    telefono='0968547896', direccion='gyq', numero_libro=3, activo=True, carrera='GIG', nivel=3,
                    pedir_libro=True, devolver_libro=False)
    print(e2)
    print(f'Se pidio el libro {e2._pedir_libro} devolvieron el libro {e2._devolver_libro}')
    e1.pedir('Revista', 'Programacion')