from django.db import models


class Cliente(models.Model):
    nome = models.CharField(max_length=150)

    class Meta:
        db_table = 'clientes'

    def __str__(self):
        return self.nome


class Livro(models.Model):
    nome = models.CharField(max_length=200)
    reservado = models.BooleanField(default=False)

    class Meta:
        db_table = 'livros'

    def __str__(self):
        return self.nome


class Reserva(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE)
    reservado_em = models.DateField()

    class Meta:
        db_table = 'reservas'
