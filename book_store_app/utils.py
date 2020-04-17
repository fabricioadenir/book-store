from .models import Cliente, Livro, Reserva
from django.forms.models import model_to_dict
from datetime import date, datetime


def formata_data(data):
    formato = "%Y-%m-%d"
    data_atualizada = datetime.strptime(str(data), formato)
    return data_atualizada


def aplica_multa(dias_reservado):
    multa = 0
    if dias_reservado < 1:
        multa = 0
    elif (dias_reservado >= 1) and (dias_reservado <= 3):
        multa = dias_reservado * 0.2
        multa += 3
    elif (dias_reservado > 3) and (dias_reservado <= 5):
        multa = dias_reservado * 0.4
        multa += 5
    elif dias_reservado > 5:
        multa = dias_reservado * 0.6
        multa += 7
    return multa


def retorna_dias_em_reserva(reservado_em, dia_verificacao):
    dias_reservado = dia_verificacao - reservado_em
    if dias_reservado.days > 3:
        dias_reservado = dias_reservado.days - 3
    else:
        dias_reservado = 0
    return dias_reservado


def reserve_livro(id_cliente, id_livro, reservado_em):

    cliente = Cliente.objects.get(id=id_cliente)
    livro = Livro.objects.get(id=id_livro)

    if not livro.reservado:
        livro.reservado = True
        livro.save()
        Reserva.objects.create(cliente=cliente, livro=livro, reservado_em=reservado_em)
        data = {
            "cliente": model_to_dict(cliente),
            "livro": model_to_dict(livro),
            "message": f"Livro reservado com sucesso, em: {reservado_em}",
        }
        return data

    data = {
        "cliente": model_to_dict(cliente),
        "livro": model_to_dict(livro),
        "message": "Livro já está reservado.",
    }
    return data


def retorna_livros_por_usuario(id_cliente):
    livros_reservados = list(Reserva.objects.filter(cliente__id=id_cliente).values())
    data_atual = formata_data(date.today())

    for book in livros_reservados:
        reservado_em = formata_data(book["reservado_em"])
        dias = retorna_dias_em_reserva(reservado_em, data_atual)

        multa = aplica_multa(dias)

        book["dias_atraso"] = dias
        book["multa"] = multa

    return livros_reservados
