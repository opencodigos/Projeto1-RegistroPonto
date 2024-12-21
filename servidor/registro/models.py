from django.db import models
from django.core.exceptions import ValidationError
from django.utils.text import slugify
from random import randint

class Funcionario(models.Model):
    slug = models.SlugField(max_length=200, unique=True)
    foto = models.ImageField(upload_to='foto/')
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=20)

    def __str__(self):
        return self.nome
    
    def save(self, *args, **kwargs):
        seq = self.nome + '_FUNC' + str(randint(1000000, 9999999))
        self.slug = slugify(seq)
        super().save(*args, **kwargs)


class ColetaFaces(models.Model):
    funcionario = models.ForeignKey(Funcionario, 
		    on_delete=models.CASCADE, related_name='funcionario_coletas')
    image = models.ImageField(upload_to='roi/')
    
    
class Treinamento(models.Model):
    modelo = models.FileField(upload_to='treinamento/') # .yml

    class Meta:
        verbose_name = 'Treinamento'
        verbose_name_plural = 'Treinamentos'

    def __str__(self):
        return 'Classificador (frontalface)'

    def clean(self):  # Limita a um único arquivo
        model = self.__class__
        if model.objects.exclude(id=self.id).exists():
            raise ValidationError('Só pode haver um arquivo salvo.')
         
class RegistroFuncionario(models.Model):
    funcionario = models.ForeignKey(Funcionario, on_delete=models.CASCADE)
    data_hora = models.DateTimeField()

    def __str__(self):
        return f"{self.funcionario.nome} - {self.data_hora}"