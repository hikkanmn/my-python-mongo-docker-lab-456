# Используем базовый образ Python
FROM python:3.9-slim

# Установка рабочей директории
WORKDIR /app

# Копируем файл зависимостей в контейнер
COPY requirements.txt requirements.txt

# Установка зависимостей
RUN pip install -r requirements.txt

# Копируем все файлы приложения в рабочую директорию контейнера
COPY . .

# Команда запуска приложения
CMD ["python", "app/app.py"]
