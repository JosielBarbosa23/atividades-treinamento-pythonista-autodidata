#Desafio 1 - Imprima na tela o ganhador de cada sorteio:

from pprint import pprint
import random

sorteios = ['1° Sorteio ', '2° Sorteio ', '3° Sorteio ']
participantes = ['Josiel', 'Laura', 'Joyce', 'Lucas', 'Dhiego', 'Nando', 'Melck', 'Pedro']

pprint({sorteio: random.choice(participantes) for sorteio in sorteios})

#Desafio 2 - Gere 5 valores aleatórios para cada grupo abaixo:

grupos = ['Grupo 1', 'Grupo 2', 'Grupo 3']

pprint({grupo: [random.randint(1, 101) for i in range(5)] for grupo in grupos})
