import time

list = [0,1,2,3,4,5,6,7,8,9]
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


