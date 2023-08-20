nomes = ['Josiel', 'Lucas', 'Dhiego', 'Laura', 'Joyce']
def aprovar_aluno(nomes):
    return nomes + ' APROVADO'

print(list(map(aprovar_aluno, nomes)))