from pprint import pprint

#Desafio 1 - Usando List Compreheension, crie a seguinte lista: ['2, 4, 6, 8, 10']

print([i for i in range(2, 11, 2)]) 

#Desafio 2 - Usando List Compreheension, use a lista cores = ['vermelho', 'azul', 'verde', 'amarelo', 'rosa', 'preto'] como base para criar a lista a seguir: ['1 - vermelho', '2 - azul' e assim por diante]

cores = ['vermelho', 'azul', 'verde', 'amarelo', 'rosa', 'preto']
pprint([str(cores.index(i)+1) + ' - ' + i for i in cores])

#Desafio 3 - Concatene uma lista com nomes com uma de pagamento realizado apenas para alguns nomes.


devedores = ['Josiel', 'Lucas', 'Laura', 'Joyce', 'Zebi', 'João', 'Jéssica', 'Suzany']
pagamento_realizado = ['Josiel', 'Lucas', 'Laura', 'Zebi']

pprint([i + ' - PAGO' if i in pagamento_realizado else i + ' - INADIMPLENTE' for i in devedores])