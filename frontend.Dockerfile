# frontend.Dockerfile

# Этап 1: Установка зависимостей и создание билда
FROM node:14 AS builder

WORKDIR /app

COPY package*.json ./

RUN npm install

COPY . .

RUN npm run build

# Этап 2: Копирование только необходимых файлов
FROM node:14

WORKDIR /app

COPY --from=builder /app/build /app/build

# Задание команды по умолчанию
CMD ["npm", "start"]