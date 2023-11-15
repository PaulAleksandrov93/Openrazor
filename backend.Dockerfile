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
COPY . .

# Вывод содержимого текущей директории (для отладки)
RUN ls -la

# Установка переменных окружения
ENV DJANGO_SETTINGS_MODULE=openrazor_backend.settings

# Запуск сервера Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]