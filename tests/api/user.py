import pytest
import requests

base_url = 'https://petstore.swagger.io/v2'        # endereco da API
headers = {'Content-Type': 'application/json'}     # os dados serao no formato json

def testar_incluir_user():

    # Configura (dados de entrada vem de user1.json)
    status_code_esperado = 200        # se a comunicacao teve ida e volta
    code_esperado = 200               # se fex o que pediu (inclusao do usuario)
    type_esperado = 'unknown'
    message_esperada = '230892'

    # Executa
    resultado_obtido = requests.post(
        url=base_url + '/user',
        data=open('C:\\Users\\saman\\PycharmProjects\\133pets\\vendors\\json\\user1.json', 'rb'),
        headers=headers
    )

    # Valida
    assert resultado_obtido.status_code == status_code_esperado
    corpo_da_resposta = resultado_obtido.json()
    assert corpo_da_resposta['code'] == code_esperado
    assert corpo_da_resposta['type'] == type_esperado
    assert corpo_da_resposta['message'] == message_esperada

