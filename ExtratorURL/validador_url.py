import re
url = "https://www.bytebank.com.br/cambio"

url_pattern = re.compile('(http(s)?://)?(www.)?bytebank.com(.br)?/cambio')
match_pattern = url_pattern.match(url)

if not match_pattern:
    raise ValueError("URL inválida")
print('URL válida') 