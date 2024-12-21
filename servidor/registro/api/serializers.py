from rest_framework import serializers
from registro.models import Funcionario, Treinamento, RegistroFuncionario

class FuncionarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Funcionario
        fields = ['id', 'slug', 'foto', 'nome', 'cpf']

class TreinamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Treinamento
        fields = ['id', 'modelo']
 
class RegistroFuncionarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegistroFuncionario
        fields = ['funcionario', 'data_hora']
