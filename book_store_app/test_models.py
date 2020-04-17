from django.test import TestCase
from .models import Cliente, Livro, Reserva


class ClientTestClass(TestCase):
    @classmethod
    def setUpTestData(cls):
        Cliente.objects.create(nome="Fernando")

    def test_campo_nome(self):
        cliente = Cliente.objects.get(id=1)
        campo_nome = cliente._meta.get_field('nome').verbose_name
        self.assertEquals(campo_nome, 'nome')

    def test_campo_nome_max_length(self):
        cliente = Cliente.objects.get(id=1)
        max_length = cliente._meta.get_field('nome').max_length
        self.assertEquals(max_length, 150)


class LivroTestClass(TestCase):
    @classmethod
    def setUpTestData(cls):
        Livro.objects.create(nome="Fernando")

    def test_campo_nome(self):
        livro = Livro.objects.get(id=1)
        campo_nome = livro._meta.get_field('nome').verbose_name
        self.assertEquals(campo_nome, 'nome')

    def test_campo_nome_max_length(self):
        livro = Livro.objects.get(id=1)
        max_length = livro._meta.get_field('nome').max_length
        self.assertEquals(max_length, 200)


class ReserveTestClass(TestCase):
    @classmethod
    def setUpTestData(cls):
        Cliente.objects.create(nome="Fernando")
        Livro.objects.create(nome="Clean Code", reservado=False)
        cliente = Cliente.objects.get(id=1)
        livro = Livro.objects.get(id=1)
        Reserva.objects.create(cliente=cliente, livro=livro, reservado_em="2020-04-15")

    def test_labels(self):
        reservas = Reserva.objects.get(id=1)
        cliente = reservas._meta.get_field('cliente').verbose_name
        livro = reservas._meta.get_field('livro').verbose_name
        reservado_em = reservas._meta.get_field('reservado_em').verbose_name
        self.assertEquals(cliente, 'cliente')
        self.assertEquals(livro, 'livro')
        self.assertEquals(reservado_em, 'reservado em')
