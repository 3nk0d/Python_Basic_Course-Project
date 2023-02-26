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
- Postgresql

## Используемые пакеты
- feedparser (Парсинг RSS)
- eventlet (Для Celery на Windows)

## Запуск проекта

В отдельных терминалах запустить из:

Каталога проекта Rabbit-mq и Postgresql
- docker compose up
Каталога news_portal
Django:
- python manage.py runserver
Celery worker
- celery -A news_portal worker -l DEBUG -P eventlet
Celery scheduled works
- celery -A news_portal beat