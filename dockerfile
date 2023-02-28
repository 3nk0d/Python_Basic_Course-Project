FROM python:3.10

WORKDIR app

ENV PYTHONUNBUFFERED=1

RUN pip install --upgrade pip

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

WORKDIR news_portal

#CMD python manage.py makemigrations
#CMD python manage.py migrate
#CMD python manage.py runserver 0.0.0.0:8000

EXPOSE 8000
