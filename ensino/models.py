from django.db import models

# Create your models here.

class Aluno(models.Model):
    nome= models.CharField(max_length=150)
    email= models.EmailField()
    ativo= models.BooleanField()
    nome_mae= models.CharField(max_length=150)
    cpf= models.CharField(max_length=20)
    idade= models.IntegerField()
    def __str__(self):
        return self.nome