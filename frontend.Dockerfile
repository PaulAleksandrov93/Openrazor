# frontend.Dockerfile

# Этап 1: Установка зависимостей и создание билда
FROM node:14 AS builder

WORKDIR /openrazor/openrazor_frontend

COPY openrazor_frontend/package*.json ./

RUN npm install

# Устанавливаем рабочую директорию внутри openrazor_frontend
WORKDIR /openrazor/openrazor_frontend

COPY openrazor_frontend/public ./public
COPY openrazor_frontend/src ./src
# COPY openrazor_frontend/.env ./.env

RUN npm run build

# Этап 2: Копирование только необходимых файлов
FROM node:14

WORKDIR /app/frontend

# Копируем собранные файлы из правильного места
COPY --from=builder /openrazor/openrazor_frontend/build /app/frontend/build

# Задание команды по умолчанию
CMD ["npm", "start"]