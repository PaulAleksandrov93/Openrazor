# frontend.Dockerfile

# Этап 1: Установка зависимостей и создание билда
FROM node:16 AS builder

WORKDIR /app/openrazor_frontend

# Копирование package.json и package-lock.json
COPY openrazor_frontend/package*.json ./

# Установка зависимостей
RUN npm install
RUN npm install -g nodemon

# Копирование остальных файлов
COPY openrazor_frontend /app/openrazor_frontend/

# Запуск сборки
RUN npm run build

# Этап 2: Задание команды по умолчанию
CMD ["npm", "run"]

