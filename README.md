# 🧑‍💻 Registro de Ponto por Reconhecimento Facial

## 📝 Descrição do Projeto

*Registro de Ponto com Reconhecimento Facial* é um sistema desenvolvido em Python com Django e OpenCV para facilitar o registro de presença por meio de reconhecimento facial. Este projeto inclui uma REST API para integração com outros sistemas e um aplicativo desenvolvido em Kivy, permitindo o uso em dispositivos móveis.

## ⚙️ Funcionalidades

- *Registro de Ponto por Reconhecimento Facial*:
    - ✍️ *Funcionários*: Gerenciar informações sobre funcionários, incluindo foto, nome, documento e captura das faces para treinamento.
    - 📷 *Reconhecimento*: Identificação facial do usuário para registrar o ponto automaticamente.
    - 🧾 *Histórico de Registros*: Visualização dos registros de ponto por data e hora.
- *Integração com Kivy App*:
    - 📲 *Aplicativo Mobile*: Aplicativo Kivy que se comunica com a API Django para registro de ponto.
- *API REST*:
    - 🔗 *Endpoints para Reconhecimento e Cadastro*: Permite o consumo de dados de reconhecimento facial.
    - 🔐 *API*: Para operações de registro e consulta de pontos.

## 🛠️ Tecnologias Utilizadas

- *Backend*: Django, Django REST Framework, OpenCV
- *App Mobile*: Kivy, kivymd
- *Linguagem*: Python 3.9

## 📋 Pré-requisitos

Antes de executar o projeto, certifique-se de que os seguintes pré-requisitos estão instalados em sua máquina:

- Python 3.9
- Django (Django==4.2)
- Django REST Framework (djangorestframework==3.15.2)
- Requests (requests==2.32.3)
- OpenCV (opencv-python==4.5.5.64 && opencv-contrib-python==4.5.5.64)
- Numpy (numpy==1.24.4)
- Kivy (para desenvolvimento mobile)

## 🚀 Como Iniciar o Projeto

Em breve