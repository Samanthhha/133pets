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

def testar_consultar_user():
    # 1 - Configura

    # 1.1 Dados de Entrada

    username = 'Samantha'

    # 1.2 Resultados Esperados
    status_code_esperado = 200
    username_esperado = 'Samantha'
    firstName_esperado = 'Samantha'
    lastName_esperado = 'Rodrigues'
    email_esperado = 'samantha@teste.com.br'
    password_esperado = '12345'
    phone_esperado = '99999999'

    # Executa
    resultado_obtido = requests.get(
        url=base_url + '/user/' + username,
        headers=headers

    )

    # Valida
    assert resultado_obtido.status_code == status_code_esperado
    corpo_da_resposta = resultado_obtido.json()
    assert corpo_da_resposta['username'] == username_esperado
    assert corpo_da_resposta['firstName'] == firstName_esperado
    assert corpo_da_resposta['lastName'] == lastName_esperado
    assert corpo_da_resposta['email'] == email_esperado
    assert corpo_da_resposta['password'] == password_esperado
    assert corpo_da_resposta['phone'] == phone_esperado

def testar_alterar_user():

    username = 'Samantha'

    status_code_esperado = 200
    code_esperado = 200  # se fex o que pediu (inclusao do usuario)
    type_esperado = 'unknown'
    message_esperada = '230892'



    resultado_obtido = requests.put(
        url=base_url + '/user/' + username,
        data=open('C:\\Users\\saman\\PycharmProjects\\133pets\\vendors\\json\\user2.json', 'rb'),
        headers=headers

    )
    
    assert resultado_obtido.status_code == status_code_esperado
    corpo_da_resposta = resultado_obtido.json()
    assert corpo_da_resposta['code'] == code_esperado
    assert corpo_da_resposta['type'] == type_esperado
    assert corpo_da_resposta['message'] == message_esperada


def testar_excluir_user():

    username = 'Samantha'
    status_code_esperado = 200
    code_esperado = 200
    type_esperado = 'unknown'


    resultado_obtido = requests.delete(
        url=base_url + '/user/' + username,
        headers=headers

    )

    assert resultado_obtido.status_code == status_code_esperado
    corpo_da_resposta = resultado_obtido.json()
    assert corpo_da_resposta['code'] == code_esperado
    assert corpo_da_resposta['type'] == type_esperado
    assert corpo_da_resposta['message'] == username
