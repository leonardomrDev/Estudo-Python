import re

address = 'Rua 1500, Apto 0502, Centro, SC, 82893-293'

pattern = re.compile("[0-9]{5}[-][0-9]{3}")
search = pattern.search(address)
cep = search.group()
print(cep)

print(search)