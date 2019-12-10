from django.db import models


class Contato(models.Model):
    nome = models.CharField(max_length=50)
    endereco = models.CharField(max_length=200)
    email = models.EmailField(max_length=100)
    data_nascimento = models.DateField()
    telefone = models.CharField(max_length=20)

    def __str__(self):
        return self.nome

class Livros(models.Model):
        titulo = models.CharField(max_length=50)
        autor = models.CharField(max_length=200)
        assunto = models.CharField(max_length=100)
        editora = models.CharField(max_length=20)
        isbn = models.CharField(max_length=20)
        ano = models.DateField()

        def __str__(self):
           return self.titulo

# Create your models here.
