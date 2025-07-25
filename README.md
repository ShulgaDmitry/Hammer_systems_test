Описание

Система авторизации по номеру телефона с выдачей и проверкой 4-значного кода. Пользователь может активировать только **1 код одновременно**. После подтверждения кода пользователь считается авторизованным.
---
Стек

- Python 3.12
- Django
- Django REST Framework
- PostgreSQL (Реализовано локально, в Pythonanywhere использовался SQLite т.к. PostgreSQL доступен только в платной версии)
- Pythonanywhere
---
Superuser:
LOGIN - admin
PASSWORD - admin

API эндпоинты:

Отправка кода на телефон
POST /send_code/
Описание: Отправка 4-значного кода на номер телефона
Request Body:
{
  "phone": "+375291234567",
}
Response 200:
{
    "message": "Code sent",
    "code": "3725"
}

Верефикация 
GET /verify/
Описание: Верефикация пользователя и отправка инвайт-кода (необязательное поле)
Request Body:
{
  "phone": "+375291234550",
  "code": "3725",
  "invite_code": "0SOO6q"
}
Response 200:
{
    "message": "User verified"
}

Список всех пользователей
GET /users/
Описание: Получить список всех пользователей
Response 200:
[
    {
        "id": 1,
        "phone": "",
        "invite_code": "K0AttI"
    },
    {
        "id": 2,
        "phone": "+375291234567",
        "invite_code": "0SOO6q"
    }
]

---

Установка

bash
git clone <repo_url>
cd <project>
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

Настрой DATABASES в settings.py под свой PostgreSQL

python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver

# Разработчик: Шульга Дмитрий
