import re

class ExtratorURL:
    
    def __init__(self, url) -> None:
        self.url = self.sanitiza_url(url)
        self.valida_url()

    def sanitiza_url(self, url):
        if type(url) == str:
            return url.strip()
        else:
            return ""
    
    def valida_url(self):
        if not self.url:
            raise ValueError("URL Vazia!")
        url_pattern = re.compile('(http(s)?://)?(www.)?bytebank.com(.br)?/cambio')
        match_pattern = url_pattern.match(url)
        if not match_pattern:
            raise ValueError("URL inválida")
        
    def get_url_base(self):
        interrogacao_index = self.url.find('?')
        url_base = self.url[:interrogacao_index]
        return url_base
    
    def get_url_parametros(self):
        interrogacao_index = self.url.find('?')
        url_parametros = self.url[interrogacao_index + 1:]
        return url_parametros
    
    def get_valor_parametros(self, parametro_search):
        parametro_index = self.get_url_parametros().find(parametro_search)
        valor_index = parametro_index + len(parametro_search) + 1
        e_comercial_index = self.get_url_parametros().find('&', valor_index)
        if e_comercial_index == -1:
            valor = self.get_url_parametros()[valor_index:]
        else:
            valor = self.get_url_parametros()[valor_index:e_comercial_index]
        return valor

    def __len__(self):
        return len(self.url)

    def __str__(self) -> str:
        return self.url + "\n" + "Parâmetros: " +self.get_url_parametros() + "\n" + "URL Base: " + self.get_url_base()

    def __eq__(self, other) -> bool:
        return self.url == other.url
        
url = "bytebank.com/cambio?moedaDestino=dolar&quantidade=100&moedaOrigem=real"
extrator_url = ExtratorURL(url)
#extrator_url = ExtratorURL("  ")
#extrator_url = ExtratorURL(None)
valor_quantidade = extrator_url.get_valor_parametros("quantidade")
print(valor_quantidade)
