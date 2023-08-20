def aprovar_aluno(nomes):
    return nomes + ' APROVADO'

nomes = ['Josiel', 'Laura', 'Lucas', 'Anuska']
print([nome + ' APROVADO' for nome in nomes])

#Também podemos incluir funções na List Compreheension

print([aprovar_aluno(nome) for nome in nomes])