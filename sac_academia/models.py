from django.db import models

class Mensagem(models.Model):
    nome = models.CharField(max_length=120)
    email = models.EmailField()
    mensagem = models.TextField()
    data_envio = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nome} <{self.email}>"