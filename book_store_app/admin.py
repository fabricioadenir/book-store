from django.contrib import admin
from .models import Cliente, Livro, Reserva
# Register your models here.

admin.site.register(Cliente)
admin.site.register(Livro)
admin.site.register(Reserva)
