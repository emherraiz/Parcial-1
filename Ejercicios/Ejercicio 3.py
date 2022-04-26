class Cuenta:
    def __init__(self, ID, titular, fecha_apertura, saldo):
        self.ID = ID
        self.titular = titular
        self.fecha_apertura = fecha_apertura
        self.saldo = float(saldo)

    def retirar(self, saldo_a_retirar):
        if saldo_a_retirar <= self.saldo:
            self.saldo = self.saldo - float(saldo_a_retirar)

        else:
            print('La cuenta no dispone de dinero suficiente para realizar esta operacion')

class Cuenta_plazo_fijo(Cuenta):
    def __init__(self):
        super().__init__()
