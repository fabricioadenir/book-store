from .models import Livro
from django.views import View
from django.http.response import JsonResponse
import json
from .utils import reserve_livro, retorna_livros_por_usuario


# Create your views here.

class BooksReservade(View):

    def get(self, request, *args, **kwargs):
        id_cliente = kwargs.get('id_cliente')
        livros_reservados = retorna_livros_por_usuario(id_cliente)
        return JsonResponse(livros_reservados, safe=False)


class BookList(View):

    def get(self, request):
        return JsonResponse(list(Livro.objects.all().values()), safe=False)


class ReserveBook(View):

    def post(self, request, *args, **kwargs):
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        reservado_em = body['reservado_em']
        id_cliente = kwargs.get('id_cliente')
        id_livro = kwargs.get('id_livro')
        if request.method == 'POST':
            resultado = reserve_livro(
                id_cliente=id_cliente,
                id_livro=id_livro,
                reservado_em=reservado_em
            )
            return JsonResponse(resultado, safe=False)
        else:
            data = {
                "menssagem": "Caminho só aceita method 'POS'."
            }
        return JsonResponse(data, safe=False)
