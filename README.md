Описание

Система авторизации по номеру телефона с выдачей и проверкой 4-значного кода. Пользователь может активировать только **1 код одновременно**. После подтверждения кода пользователь считается авторизованным.

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
POST /api/auth/phone/
Описание: Отправка 4-значного кода на номер телефона
Request Body:
{
  "phone": "+375291234567"
}
Response 200:
{
  "message": "Код отправлен на номер +375291234567"
}

Подтверждение кода
POST /api/auth/verify/
Описание: Верификация кода, выдача токена при успехе
Request Body:
{
  "phone": "+375291234567",
  "code": "1234"
}
Response 200:
{
  "token": "f86829d58d1b56e6b8f739a59c60b4b173e23b58"
}

Получение профиля
GET /api/profile/
Описание: Получить данные авторизованного пользователя
Headers:
Authorization: Token <token>
Response 200:
{
  "id": 1,
  "username": "+375291234567",
  "phone": "+375291234567"
}

Список всех пользователей
GET /api/users/
Описание: Получить список всех пользователей
Headers:
Authorization: Token <token>
Response 200:
[
  {
    "id": 1,
    "username": "+375291234567",
    "phone": "+375291234567"
  },
  {
    "id": 2,
    "username": "+375293334455",
    "phone": "+375293334455"
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

# Настрой DATABASES в settings.py под свой PostgreSQL

python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver

Разработчик: Шульга Дмитрий
