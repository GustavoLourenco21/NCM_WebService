import json
import zipfile
import requests


def buscar_dados():
    url = "https://portalunico.siscomex.gov.br/cadatributos/api/atributo-ncm/download/json"
    request = requests.get(url)
    with open('C:\\Users\\Super\\Downloads\\teste\\NCM.zip', 'wb') as f:
        f.write(request.content)

    alvo = 'C:\\Users\\Super\\Downloads\\teste\\NCM.zip'
    handler = zipfile.ZipFile(alvo)
    handler.extractall('C:\\Users\\Super\\Downloads\\teste')

    abrir_arquivo = open('C:\\Users\\Super\\Downloads\\teste\\ATRIBUTOS_POR_NCM_2022_09_09.json', mode='r', encoding="utf8")
    data = json.loads(abrir_arquivo.read())
    print(data)

    # salvar_arquivo = open("C:\\Users\\Super\\Desktop\\teste2\\NCM.json", "w")
    # salvar_arquivo.write(str(data))
    # salvar_arquivo.close()

    # print(request.headers)


if __name__ == '__main__':
    buscar_dados()
