import time
import array as arr
#import numpy as np

arr.array('d', [1, 3.5])
#np.array()

# def __eq__(self, other): 
# utilizado para comparar o que está vindo como parâmetro ao invés do objeto inteiro.

list = [0,1,2,3,4,5,6,7,8,9]
reverse = reversed(list)
reverselist = list.reverse()
print(reverse)
print(reverselist)
enumerate(list)
for x in enumerate(list):
    print(x)
time.sleep(1)

for x in list:
    print(x)

usuarios = [
    ('Leonardo', 21, 2001),('Pedro', 26, 1996),('Paulo', 37, 1981)
]
time.sleep(0.7)
for x,y,z in usuarios:
    print(x)
    time.sleep(0.5)
    print(y,z)

tuple = (0,1,2,3,4,5,6,7,8,9)
set = {0,1,2,3,4,5,6,7,8,9}
dict = {
    'nome': 'Leonardo',
    'cidade': 'Balneário Camboriú',
    'estado': 'Santa Catarina',
    'ano': 2021
} # Talvez de para ter listas mutáveis dentro do dict

# Printa todos os Collections
print(list)
time.sleep(0.5)
print(tuple)
print('\n')
time.sleep(0.5)
print(set)
print("\n")
time.sleep(0.5)
print(dict)
print('\n')
time.sleep(1)

# Manipulação de Collections
# Listas
list.remove(0)
print(list)

# Tuplas


# SETs



# Dict
#dict.update({'nome:':'André', 'ano': 2021})
print(dict.items())
print('\n')
time.sleep(0.5)
print(dict.values())
print('\n')
time.sleep(0.5)
print(dict['nome'])
time.sleep(0.5)
print(dict['cidade'])
time.sleep(0.5)
print(dict['estado'])
time.sleep(0.5)
print(dict['ano'])
time.sleep(0.5)


