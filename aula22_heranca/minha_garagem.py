from aula22_heranca.veiculo import Carro, Moto

v1 = Carro('Volkswagen', 'Gol', 2022, 4)
v2 = Moto('Honda', 'CB', 2024, 471)
v3 = Carro('Fiat', 'Uno Mini', 2013, 2)

garagem = [v1, v2, v3]

#Percorrer lista e imprimir tudo

for v in garagem:
    print(v)

#Imprima quantos são carros e quantos são motos

carros = [v for v in garagem if isinstance(v, Carro)]
motos = [v for v in garagem if isinstance(v, Moto)]
print(f'Carros: {len(carros)} | Motos: {len(motos)}')

