from django.conf.urls import url
from . import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    url(
        r"^client/(?P<id_cliente>[-\w]+)/books/$",
        views.BooksReservade.as_view(),
        name="reservations",
    ),
    url(
        r"^client/(?P<id_cliente>[-\w]+)/books/(?P<id_livro>[-\w]+)/reserve/$",
        csrf_exempt(views.ReserveBook.as_view()),
        name="reserve",
    ),
    url(r"^books/", views.BookList.as_view(), name="books"),
]
