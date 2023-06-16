from abc import ABC, abstractmethod


class Cuenta(ABC):

    def __init__(self, numero:str=None, nombre:str=None,saldo:float=None,credito:float=None,debito:float=None):
        self._numero = numero
        self._nombre = nombre
        self._saldo =saldo
        self._credito = credito
        self._debito = debito

        

    @property
    def numero(self):
        return self._numero

    @numero.setter
    def numero(self, numero):
        self._numero= numero

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, saldo):
        self._saldo = saldo

    @property
    def credito(self):
        self._credito = credito

    @credito.setter
    def credito(self, credito):
        self._credito = credito

    @property
    def debito(self):
        self._debito = debito

    @debito.setter
    def debito(self, debito):
        self._debito = debito




    def __str__(self):
        return f'Cuenta [{self.__dict__.__str__()}]'

    @abstractmethod
    def __str__(self):
            # return f'Persona [nombre: {self._nombre}, apellido: {self._apellido}, email: {self._email}]'
            return f'Cuenta: {self.__dict__.__str__()}'

    #def __str__(self):
            #return f'CuentaBancaria: {type(self)}'

    '''
    Display name
    '''

    def saldo_mostrar(self, mostrar_saldo):
        if mostrar_saldo:
                print(f'{self._credito} {self._debito}, emial: {self._cuenta}')
        else:
                print(f'{self._nombre} {self._numero}')

    def obtener_saldo_mostrar(self):
        return f'{self._nombre} {self._numero}'

if __name__ == '__main__':
        pass



