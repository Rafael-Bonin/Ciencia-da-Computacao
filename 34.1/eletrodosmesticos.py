class Geladeira:
    def __init__(self, cor, marca, preco):
        self.__cor = cor
        self.__marca = marca
        self.preco = preco

    def __str__(self):
        return f'''
        cor da geladeira: {self.__cor}
        marca da geladeira: {self.__marca}
        preco da geladeira: {self.preco}
        '''
    
class comprador:
    def __init__(self, idade, saldo):
        self.__idade = idade
        self.__saldo = saldo
        self.geladeira = None

    def __str__(self):
      return f'''
      idade: {self.__idade}
      saldo: {self.__saldo}
      geladeira: {self.geladeira}
      '''

    def comprar_geladeira(self, geladeira: Geladeira):
        if self.__saldo >= geladeira.preco:
            self.__saldo -= geladeira.preco
            self.geladeira = geladeira
    
frosfree = Geladeira('preta', 'eletrolux', 2000)

eu = comprador(20, 5000)

eu.comprar_geladeira(frosfree)

print(eu)