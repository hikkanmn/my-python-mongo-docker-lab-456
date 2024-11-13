from flask import Flask, render_template, request, redirect
from pymongo import MongoClient

app = Flask(__name__)

# Подключение к MongoDB (используем имя контейнера как хост)
client = MongoClient('mongodb://mongo_container:27017/')
db = client.simpledb  # Название базы данных
collection = db.records  # Название коллекции

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Получение данных из формы и сохранение в MongoDB
        name = request.form.get('name')
        second_name = request.form.get('second_name')
        if name & second_name:
            collection.insert_one({'name': name, 'second_name': second_name})  # Вставка новой записи в коллекцию
        return redirect('/')  # Перенаправление на главную страницу

    # Получение всех записей из коллекции
    records = collection.find()
    return render_template('index.html', records=records)  # Отображение данных на главной странице

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')  # Запуск приложения с доступом по сети
