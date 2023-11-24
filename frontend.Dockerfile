# frontend.Dockerfile

# Этап 1: Установка зависимостей и создание билда
FROM node:16 AS builder

WORKDIR /app/frontend

# Копирование package.json и package-lock.json
COPY openrazor_frontend/package*.json ./

# Установка зависимостей
RUN npm install

# Копирование остальных файлов
COPY openrazor_frontend/ .

# Запуск сборки
RUN npm run build

# Этап 2: Задание команды по умолчанию
CMD ["npm", "start"]