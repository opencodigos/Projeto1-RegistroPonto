from rest_framework import viewsets
from registro.api.serializers import FuncionarioSerializer, TreinamentoSerializer, RegistroFuncionarioSerializer
from registro.models import Funcionario, Treinamento, RegistroFuncionario

class FuncionarioViewSet(viewsets.ModelViewSet):
    queryset = Funcionario.objects.all()
    serializer_class = FuncionarioSerializer

class TreinamentoViewSet(viewsets.ModelViewSet):
    queryset = Treinamento.objects.all()
    serializer_class = TreinamentoSerializer 

class RegistroFuncionarioViewSet(viewsets.ModelViewSet):
    queryset = RegistroFuncionario.objects.all()
    serializer_class = RegistroFuncionarioSerializer