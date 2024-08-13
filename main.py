import random

class PlacaVeiculo:
 def __init__(self, estado, cidade, numero):
 self.estado = estado
 self.cidade = cidade
 self.numero = numero

 def __str__(self):
 return f"{self.estado} - {self.cidade} - {self.numero}"

class ClonadorPlaca:
 def __init__(self):
 self.placas_clonadas = []

 def clonar_placa(self, placa_original):
 estado = placa_original.estado
 cidade = placa_original.cidade
 numero = placa_original.numero

 # Simula a clonagem da placa
 novo_numero = str(random.randint(1000, 9999))
 nova_placa = PlacaVeiculo(estado, cidade, novo_numero)

 self.placas_clonadas.append(nova_placa)
 return nova_placa

def main():
 clonador = ClonadorPlaca()

 # Cria uma placa original
 placa_original = PlacaVeiculo("SP", "São Paulo", "1234")

 print("Placa original:")
 print(placa_original)

 # Clona a placa
 placa_clonada = clonador.clonar_placa(placa_original)

 print("\nPlaca clonada:")
 print(placa_clonada)

if __name__ == "__main__":
 main()
