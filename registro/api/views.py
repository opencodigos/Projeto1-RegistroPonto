from rest_framework import viewsets
from registro.api.serializers import FuncionarioSerializer, TreinamentoSerializer
from registro.models import Funcionario, Treinamento

class FuncionarioViewSet(viewsets.ModelViewSet):
    queryset = Funcionario.objects.all()
    serializer_class = FuncionarioSerializer

class TreinamentoViewSet(viewsets.ModelViewSet):
    queryset = Treinamento.objects.all()
    serializer_class = TreinamentoSerializer
