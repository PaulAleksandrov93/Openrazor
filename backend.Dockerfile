# backend.Dockerfile

# Этап 1: Установка зависимостей
FROM python:3.8 AS builder

ENV PYTHONUNBUFFERED 1

# Установка рабочей директории в /app/openrazor_backend
WORKDIR /app/openrazor_backend

# Копирование requirements.txt и установка зависимостей
COPY requirements.txt .

RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Этап 2: Копирование только необходимых файлов
FROM python:3.8

ENV PYTHONUNBUFFERED 1

# Установка рабочей директории в /app/openrazor_backend
WORKDIR /app/openrazor_backend

# Копирование файлов из предыдущего этапа
COPY --from=builder /usr/local/lib/python3.8 /usr/local/lib/python3.8
COPY openrazor_backend /app/openrazor_backend

# Используем dockerize для ожидания доступности базы данных перед миграцией
RUN apt-get update && apt-get install -y wget
RUN wget https://github.com/jwilder/dockerize/releases/download/v0.6.1/dockerize-linux-amd64-v0.6.1.tar.gz
RUN tar -C /usr/local/bin -xzvf dockerize-linux-amd64-v0.6.1.tar.gz
RUN rm dockerize-linux-amd64-v0.6.1.tar.gz

CMD ["dockerize", "-wait", "tcp://db:5432", "python", "manage.py", "runserver", "0.0.0.0:8000"]
