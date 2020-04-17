# book-store
Livraria Online, onde é possível verificar todos dados dos livros que você está emprestado ou livros que gostaria de realizar uma reserva. Nosso tempo de reserva do livro é 3 dias.
 
## Instalação e configuração usando Docker.
Esse ambiente foi preparado para ser instalado no Docker seguindo os passos abaixo e o banco de dados escolhido foi o PostGres:
 
* Comando responsável pela criação da imagem e subir o banco. 
```
docker-compose up -d --build --no-deps db
```

* Comando responsável pela criação da image e subir API. 
```
docker-compose up -d --build --no-deps book-store
```

* Comando para montar o migrate para o banco de dados
```
docker-compose exec book-store python manage.py makemigrations --noinput
```
 
* Comando responsável por realizar a migração da estrutura de dados para o banco.
```
docker-compose exec book-store python manage.py migrate --noinput
```
 
* Comando responsável para criar alguns dados fictícios para testar a API.
```
docker-compose exec book-store python manage.py loaddata initial.json
```
 
* Comando para criação de usuário para que seja possível acessar o admin do Django.
```
docker-compose exec book-store python manage.py createsuperuser --email admin@example.com --username admin
```
 
## Instalação e configuração ambiente local (Dev).
Rodando  em ambiente local o banco de dados será o padrão sqlite3.

* Comando responsável instalar as dependências.
```
pip install -r requirements.txt
```
 
* Comando para montar o migrate para o banco de dados
```
python manage.py makemigrations
```
 
* Comando responsável por realizar a migração da estrutura de dados para o banco.
```
python manage.py migrate
```
 
* Comando responsável para criar alguns dados fictícios para testar a API.
```
python manage.py loaddata initial.json
```
 
* Comando para criação de usuário para que seja possível acessar o admin do Django.
```
python manage.py createsuperuser --email admin@example.com --username admin
```
 
* Comando para subir a API.
```
python manage.py runserver
```
 
## EndPoit e como usar:
Listagem de livros emprestados, respeitando a multa em caso de atraso:
```
GET
    /client/{id_cliente}/books/

Exemplo do retorno:

[
    {
        "id": 4,
        "cliente_id": 4,
        "livro_id": 4,
        "reservado_em": "2020-04-14",
        "dias_atraso": 0,
        "multa": 0
    }
]

```

Reserva de livro
```
POS
    /client/{id_cliente}/books/{id_livro}/reserve/

--- Payload para reserva de livro: --
{
	"reservado_em": "2020-04-16"
}


-- Exemplos de retorno: --

Caso o livro já reservado:

{
    "cliente": {
        "id": 1,
        "nome": "Fabricio"
    },
    "livro": {
        "id": 6,
        "nome": "Testes Automatizados",
        "reservado": true
    },
    "message": "Livro já está reservado."
}

Caso disponível para reserva:

{
    "cliente": {
        "id": 1,
        "nome": "Fabricio"
    },
    "livro": {
        "id": 7,
        "nome": "Nada Mais",
        "reservado": true
    },
    "message": "Livro reservado com sucesso, em: 2020-04-16"
}
```

Listagem de livros retornando o status do livro:
```
GET
    /books

Exemplo de retorno:

[
    {
        "id": 1,
        "nome": "Clean Code",
        "reservado": true
    },
    {
        "id": 2,
        "nome": "Padrões JavaScripts",
        "reservado": true
    },
    {
        "id": 3,
        "nome": "Data Science do zero",
        "reservado": true
    },
    {
        "id": 4,
        "nome": "Manual de DevOps",
        "reservado": true
    },
    {
        "id": 5,
        "nome": "Entendendo Algoritimos",
        "reservado": true
    },
    {
        "id": 6,
        "nome": "Microsserviços prontos para a produção",
        "reservado": false
    },
    {
        "id": 7,
        "nome": "Introdução à Programação com Python",
        "reservado": false
    },
    {
        "id": 8,
        "nome": "Padrões de Projeto",
        "reservado": false
    },
    {
        "id": 9,
        "nome": "Arquitetura Limpa",
        "reservado": false
    }
]

```

## Executar testes
```
python manage.py test --verbosity 2
```

## Lint
```
flake8 --config=flake8
```
```
pycodestyle --config=pycodestyle .
```