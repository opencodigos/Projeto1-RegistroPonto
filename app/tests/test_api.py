import requests

# API - Lista de Funcionários cadastrado no sistema
def obter_dados_funcionarios():
    response = requests.get('http://127.0.0.1:8000/api/funcionarios/')
    if response.status_code == 200:
        return response.json()
    return []

# Obtem o classificador (Treinamento)
def obter_classificador():
    response = requests.get('http://127.0.0.1:8000/api/treinamento/')
    if response.status_code == 200:
        return response.json()
    return None 
