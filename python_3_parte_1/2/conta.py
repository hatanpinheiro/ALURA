class Conta:

    def __init__(self, numero, titular, saldo, limite):
        print("Construindo objeto...{}".format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print("Saldo {} do títular {}".format(self.__saldo, self.__titular))

    def deposita(self, valor):
        self.__saldo += valor

    def saca(self, valor):
        self.__saldo -= valor

    def transfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)

    def get_saldo(self):
        return self.__saldo

    def get_titular(self):
        return self.__titular

    @property
    def get_limite(self):
        return self.__limite

    @limite.setter   
    def __limite(self, limite):
        self.__limite = limite

# from conta import Conta
# conta = Conta(123, "Nico", 55.5, 1000.0)
# conta2 = Conta(321, "Marco", 100.0, 1000.0)