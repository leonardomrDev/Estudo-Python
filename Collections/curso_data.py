# APRENDIZADO DE SET

from typing import Counter


alunos_data_science = {15, 23, 43, 56}
alunos_machine_learning = {13, 23, 56, 42}

# Intersection
print(alunos_data_science | alunos_machine_learning)
# Union
print(alunos_data_science & alunos_machine_learning)
# Difference
print(alunos_data_science - alunos_machine_learning)
# Symmetric Difference
print(alunos_data_science ^ alunos_machine_learning)

numero = int(input("Insira o número: "))
if numero not in alunos_data_science:
    alunos_data_science.add(numero)
    print(f'Adicionado o aluno nº {numero}!')
    print(alunos_data_science)
else:
    alunos_machine_learning.add(numero)
    print(f'Adicionado o aluno nº {numero}!')
    print(alunos_machine_learning)

# APRENDIZADO DICTIONARY OU MAP

info = {
    "Leonardo" : 21,
    "Pedro" : 26,
    "André" : 22,
    "Thiago" : 23
}

type(info)
info['Leonardo']
print(info['Pedro'])
info.get('Leonardo', 0)
info.get('Carlos', 0)

for x in info.keys():
    print(x)
for y in info.values():
    print(y)
print('\n')
for z in info.keys():
    print(z, info[z])
for i in info.items():
    print(i)
for chave, valor in info.items():
    print(chave, 'possui', valor, "anos!")

print(['Cidadão: {}, possui {} anos de idade!'.format(chave, valor) for chave, valor in info.items()])

txt = "Romeu Ricardo Rene Julio Eduarda Maria Mariana Marina"
for word in txt.split():
    contador = info.get(word, 0)
    info[word] = contador + 1
for  key, value in info.items():
    print(f'{key} possui {value} anos!')
print(Counter(txt.split()))

# git