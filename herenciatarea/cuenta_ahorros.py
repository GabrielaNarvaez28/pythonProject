from Herencia.cuenta import Cuenta



class Cuenta_ahorros(Cuenta):
    #contador_mostrar_saldo = 0
    def __init__(self, interes:float=None, numero:str=None, nombre:str=None, saldo:float=None, credito:float=None, debito:float=None):
        super().__init__(numero=numero, nombre=nombre,saldo=saldo, credito=credito, debito=debito)
        # Empleado.contador_empleado = Empleado.contador_empleado + 1
        #Interes.contador_interes += 1
        self._interes = interes


    @property
    def interes(self):
        return self._interes

    @interes.setter
    def interes(self, interes):
       self._interes = interes

       def __str__(self):
           # return f'Persona [nombre: {self._nombre}, apellido: {self._apellido}, email: {self._email}]'
           return f'Cuenta_ahorros: {self.__dict__.__str__()}'


if __name__ == '__main__':
    obj = Cuenta_ahorros(numero='2200630933', nombre='Gabriela Narvaez', saldo=1000.00, credito=1000.00
                         , debito=200.00, interes=0.25)
    print(objCuenta_ahorros)
    # objCliente.cedula='1234567890'
    # print(objCliente)