from django.test import TestCase
from .models import Cliente, Livro
from . import utils
import datetime


class UtilsTestClass(TestCase):
    @classmethod
    def setUpTestData(cls):
        Cliente.objects.create(nome="Fabricio")
        Livro.objects.create(nome="Livro Teste", reservado=False)
        Cliente.objects.create(nome="Fernando")
        Livro.objects.create(nome="Livro Teste 2", reservado=False)
        cls.atual_date = datetime.date(2020, 4, 16)
        cls.reservado_em = datetime.date(2020, 4, 10)
        utils.reserve_livro(2, 2, "2020-04-16")

    def test_aplica_multa(self):
        primeira_multa = utils.aplica_multa(0)
        self.assertTrue(primeira_multa == 0)
        segunda_multa = utils.aplica_multa(1)
        self.assertTrue(segunda_multa == 3.2)
        terceira_multa = utils.aplica_multa(4)
        self.assertTrue(terceira_multa == 6.6)
        quarta_multa = utils.aplica_multa(6)
        self.assertTrue(quarta_multa == 10.6)

    def test_return_days_reserved(self):
        dias = utils.retorna_dias_em_reserva(self.reservado_em, self.atual_date)
        self.assertTrue(dias == 3)

    def test_reserve_book(self):
        resultado = utils.reserve_livro(1, 1, "2020-04-16")
        resultado_esperado = {
            "cliente": {"id": 1, "nome": "Fabricio"},
            "livro": {"id": 1, "nome": "Livro Teste", "reservado": True},
            "message": "Livro reservado com sucesso, em: 2020-04-16",
        }
        self.assertEqual(resultado, resultado_esperado)

    def test_return_list_books_from_user(self):
        utils.reserve_livro(1, 1, "2020-04-16")
        resultado = utils.retorna_livros_por_usuario(1)
        resultado_esperado = {
            "id": 2,
            "cliente_id": 1,
            "livro_id": 1,
            "reservado_em": datetime.date(2020, 4, 16),
            "dias_atraso": 0,
            "multa": 0,
        }
        self.assertEqual(resultado[0], resultado_esperado)
