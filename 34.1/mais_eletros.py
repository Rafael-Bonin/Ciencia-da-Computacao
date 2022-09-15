class Eletrodomesticos:
    def __init__(self, cor, voltagem, preco, marca):
          self.cor = cor
          self.voltagem = voltagem
          self.preco = preco
          self.marca = marca

    def __str__(self):
        return f'''
        cor: {self.cor}
        voltagem: {self.voltagem}
        preco: {self.preco}
        marca: {self.marca}
        '''

class Microondas(Eletrodomesticos):
    def __init__(self, cor, voltagem, preco, marca, rotacao):
         super().__init__(cor, voltagem, preco, marca)
         self.rotacao = rotacao

bonzao = Microondas('amarelo', 220, 1500, 'eletrolux', '150rpm')

print(bonzao)

class Monitor(Eletrodomesticos):
    def __init__(self, cor, voltagem, preco, marca, led):
        super().__init__(cor, voltagem, preco, marca)
        self.led = led

aoc = Monitor('preto', 110, 2500, 'aoc', 'da boa')

print(aoc)