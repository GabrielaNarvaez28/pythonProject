from cuenta import Cuenta

class Cuenta_corriente(Cuenta):

    def __init__(self,cheque:float, tiene_chequera:bool,numero:str=None, nombre:str=None,saldo:float=None,
                 credito:float=None,debito:float=None,mostrar_saldo:float=None):
        super().__init__(numero=numero, nombre=nombre,saldo=saldo, credito=credito, debito=debito,
                         mostrar_saldo =mostrar_saldo)

        self._tiene_chequera = tiene_chequera
        self._cheque = cheque

    @property
    def tiene_chequera(self):
        return self._tiene_chequera

    @tiene_chequera.setter
    def tiene_chequera(self, tiene_chequera):
        self._tiene_chequera = tiene_chequera

    @property
    def cheque(self):
        return self._cheque

    @cheque.setter
    def cheque(self, cheque):
       self._cheque = cheque

    def __str__(self):
           # return f'Persona [nombre: {self._nombre}, apellido: {self._apellido}, email: {self._email}]'
           return f'Cuenta_corriente:[ tiene_chequera = {self.tiene_chequera}]'

    def saldo_mostrar(self):
        return (self._credito + self.saldo) - self._debito
    def pagar_cheque(self):
        return self.saldo_mostrar() - self.cheque


if __name__ == '__main__':
    #cc= Cuenta_corriente (tiene_chequera= True)
    #print(cc)
    cte = Cuenta_corriente(credito=4200.00, debito=1000.00, saldo=2000.00,tiene_chequera= True,cheque=800.00 )
    print(cte)
    print(f'El saldo de la cuenta corriente es :{cte.saldo_mostrar()}')
    print(f'El saldo de la cuenta corriente menos el valor del cheque es :{cte.pagar_cheque()}')
    # objCliente.cedula='1234567890'
    # print(objCliente)
