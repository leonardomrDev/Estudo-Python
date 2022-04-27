url = "bytebank.com/cambio?moedaDestino=dolar&quantidade=100&moedaOrigem=real"

# Separação da base e parâmetros
interrogacao_index = url.find('?')
url_base = url[:interrogacao_index] # sem o ponto de interrogação
url_parametros = url[interrogacao_index+1:]
print(url_parametros)

# Busca o valor de um parâmetro
parametro_search = 'quantidade'
parametro_index = url_parametros.find(parametro_search)
valor_index = parametro_index + len(parametro_search) + 1
e_comercial_index = url_parametros.find('&', valor_index)
if e_comercial_index == -1:
    valor = url_parametros[valor_index:]
else:
    valor = url_parametros[valor_index:e_comercial_index]
print(valor)