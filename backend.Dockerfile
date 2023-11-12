# backend.Dockerfile

# Этап 1: Установка зависимостей
FROM python:3.8 AS builder

ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt /app/

RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Этап 2: Копирование только необходимых файлов
FROM python:3.8

ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY --from=builder /usr/local/lib/python3.8 /usr/local/lib/python3.8

COPY . /app/openrazor_backend/

# Установка переменных окружения
ENV DJANGO_SETTINGS_MODULE=openrazor_backend.settings