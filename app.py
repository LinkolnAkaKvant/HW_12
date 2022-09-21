# Загружаем необходимые модули и функции
import logging
from flask import Flask, send_from_directory
from loader.view import loader_blueprint
from main.view import main_blueprint

POST_PATH = "posts.json"
UPLOAD_FOLDER = "uploads/images"

# Инициализируем фласк
app = Flask(__name__)

# Инициализируем блюпринты
app.register_blueprint(main_blueprint)
app.register_blueprint(loader_blueprint)

# Создаем файл лога
logging.basicConfig(filename='basic.log', level=logging.INFO)


@app.route("/uploads/<path:path>")
def static_dir(path):
    return send_from_directory("uploads", path)


# Запускаем фласк
app.run(debug=True)
