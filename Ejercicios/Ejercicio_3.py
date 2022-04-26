from datetime import datetime
class Cuenta:
    def __init__(self, ID, titular, fecha_apertura, saldo):
        self.ID = ID
        self.titular = titular
        self.fecha_apertura = fecha_apertura
        self.saldo = saldo

    def ingresar(self, saldo_a_ingresar):
        self.saldo += saldo_a_ingresar

    def retirar(self, saldo_a_retirar, transferencia = 'No', dinero_permitido_a_deber = 0):
        if saldo_a_retirar <= (self.saldo + dinero_permitido_a_deber):
            self.saldo -= saldo_a_retirar
            if transferencia != 'No':
                return saldo_a_retirar

        else:
            print('La cuenta no dispone de dinero suficiente para realizar esta operacion')


class Cuenta_plazo_fijo(Cuenta):
    def __init__(self, ID, titular, fecha_apertura, saldo, fecha_vencimiento):
        super().__init__(ID, titular, fecha_apertura, saldo)
        self.fecha_vencimiento = fecha_vencimiento

    def retirar_a_plazo_fijo(self, saldo_a_retirar, transferencia = 'No'):
        if datetime.now() < self.fecha_vencimiento:
            self.retirar(saldo_a_retirar * 1.05, transferencia)
        else:
            self.retirar(saldo_a_retirar, transferencia)

class Cuenta_vip(Cuenta):
    def __init__(self, ID, titular, fecha_apertura, saldo, dinero_permitido_a_deber):
        super().__init__(ID, titular, fecha_apertura, saldo)
        self.dinero_permitido_a_deber = dinero_permitido_a_deber

    def retirar_vip(self, saldo_a_retirar, transferencia):
        self.retirar(saldo_a_retirar, transferencia, self.dinero_permitido_a_deber)






