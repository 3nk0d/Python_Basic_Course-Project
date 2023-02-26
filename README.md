# Python_Basic_Course-Project

Данный проект производит автоматический парсинг статей из RSS-лент и выводит их пользователю.

Вывод производится с использованием тэгов.

Пользователь выбирает существующие тэги или добавляет свои.

Тэгом является слово, содержащееся в наименовании или тексте статьи.

Также пользователь может предложить свой источник - RSS-ленту.

## Используемые технологии

- Django
- Docker
- RabbitMQ
- Celery
- PostgreSQL

## Используемые пакеты
- feedparser (Парсинг RSS)
- eventlet (Для Celery на Windows)

## Запуск проекта

В отдельных терминалах запустить из:

Каталога проекта RabbitMQ и PostgreSQL
- docker compose up

Каталога news_portal
Django:
- python manage.py runserver
Celery worker
- celery -A news_portal worker -l DEBUG -P eventlet
Celery scheduled works
- celery -A news_portal beat

## Команды

Заполнение БД тестовыми данными
`fill_db`
Ручной запуск парсинга источников RSS 
`rss_parser`
Ручное обновление тэгов статей
`tags_update`