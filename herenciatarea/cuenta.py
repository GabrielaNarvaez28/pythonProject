from abc import ABC, abstractmethod

#Gabriela Narváez 3-4N   AUTOR
class Cuenta(ABC):

    def __init__(self, numero:str=None, nombre:str=None,saldo:float=None,credito:float=None,debito:float=None
                 ,mostrar_saldo:float=None):
        self._numero = numero
        self._nombre = nombre
        self._saldo =saldo
        self._credito = credito
        self._debito = debito
        self._mostrar_saldo = mostrar_saldo

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
        return self._credito

    @credito.setter
    def credito(self, credito):
        self._credito = credito

    @property
    def debito(self):
        return self._debito

    @debito.setter
    def debito(self, debito):
        self._debito = debito

    @property
    def mostrar_saldo(self):
        return self._mostrar_saldo

    @mostrar_saldo.setter
    def mostrar_saldo(self, mostrar_saldo):
        self._mostrar_saldo = mostrar_saldo

    @abstractmethod
    def __str__(self):
            # return f'Persona [nombre: {self._nombre}, apellido: {self._apellido}, email: {self._email}]'
            return f'Cuenta: {self.__dict__.__str__()}'


    '''
    Display name
    '''
    @abstractmethod
    def saldo_mostrar(self):
        return (self._credito + self.saldo) - self._debito

if __name__ == '__main__':
        pass



