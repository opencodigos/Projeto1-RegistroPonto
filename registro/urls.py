from django.urls import path 
from .views import criar_funcionario, criar_coleta_faces 

urlpatterns = [    
    path('', criar_funcionario, name='criar_funcionario'),
    path('criar_coleta_faces/<int:funcionario_id>', criar_coleta_faces, name='criar_coleta_faces'),
]