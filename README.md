# New Year Counter API

Лабораторная работа №1: Знакомство с клиент-серверным взаимодействием

## Описание проекта
Простой REST API сервис, который возвращает количество дней до Нового года.
Сервис реализован на FastAPI (Python) и упакован в Docker-контейнер.

##  Технологии
- **Python 3.13** - язык программирования
- **FastAPI** - веб-фреймворк
- **Uvicorn** - ASGI сервер
- **Docker** - контейнеризация

##  Запуск проекта

### Локальный запуск (без Docker)

1. **Установите зависимости:**

pip install -r requirements.txt

2. Запустите сервер
Запустите сервер:

uvicorn app.main:app --reload --port 4200


3. Проверьте работу

curl http://localhost:4200/info

Запуск в Docker

1. Соберите образ

docker build -t new-year-counter .

2. Запустите контейнер:

docker run -d -p 4200:4200 --name new-year-counter new-year-counter

3. Проверьте:

curl http://localhost:4200/info


Проверка работоспособности

1. Проверка локального запуска:

curl http://localhost:4200/
# Должны увидеть: {"message":"New Year Counter API","usage":"GET /info - получить количество дней до Нового года"}

2. Проверка основного функционала:

curl http://localhost:4200/info
# Должны увидеть: {"days_before_new_year":316}

3. Проверка в браузере:

http://localhost:4200/info - основной endpoint
http://localhost:4200/docs - документация Swagger


