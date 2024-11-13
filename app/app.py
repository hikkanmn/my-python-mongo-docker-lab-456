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
        # Получение данных из формы
        name = request.form.get('name')
        surname = request.form.get('surname')
        email = request.form.get('email')

        if name and surname and email:
            # Вставка новой записи в коллекцию
            collection.insert_one({
                'name': name,
                'surname': surname,
                'email': email
            })
        return redirect('/')

    # Получение всех записей из коллекции
    records = collection.find()
    return render_template('index.html', records=records)  # Отображение данных на главной странице

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')  # Запуск приложения с доступом по сети
