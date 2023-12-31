# Desafio 1: Encontre a palavra simples:
 Olá! Sou uma palavra simples.
* -> Usando regex, digitar:(simples)
* -> Professor: Usando regex, digitar:simples

# Desafio 2:
# Encontre todas as ocorrências de 23(os números juntos) e exatamente com esses valores:
dev123com
developer 123
dev = 123
dev = 1234
dev = 1337
dev = 50000

*  Usando regex, digitar: 23

# Desafio 3:
# Encontre todos os valores, onde o valor inicial é 2, porém o segundo valor você não conhece: Ex:23, 24, 21,
26, etc:
* Usando regex, digitar: 2\d (captura somente dois o 2 mais um dígito)

# Desafio 4:
# Usando os valores a seguir encontre os seguintes números por completo usando regex:
13.35.86
22.36.77
53.12.34
*
*  \d\d\.\d\d\.\d\d

# Desafio 5:
# Crie um regex para encontrar o padrão apenas conforme as combinações descritas abaixo:
bah pular
tah encontrar
jah encontrar
nah encontrar
uai pular
* 
*  Professor: Usando regex, digitar: [tjn]ah

# Desafio 6:
# Encontre a combinação de acordo com o descrito abaixo:
(123)1234-1235 encontrar
(123)1234-1235 encontrar
(129)1234-1235 pular
(129)1234-1235 pular
* 
*  [(]\d\d[3][)]\d\d\d\d[-]\d\d\d\d

# Desafio 7:
# Usando regex, encontre apenas a sequência 1234 abaixo:
1234 encontrar
6462 pular
* 
*  Usando regex, digitar: [1-4]

# Desafio 8:
# Usando regex encontre apenas as letras de p a v:
pqrstuv encontrar
wxyz pular
abcdefg pular
*
  Usando regex, digitar:[p-v]

# Desafio 9:
# Crie um regex para encontrar tanto pizzas enviadas quanto pizza enviada:
2 pizzas enviadas
1 pizza enviada
3 pizzas enviadas
* 
*  Usando regex, digitar: pizzas? enviadas?