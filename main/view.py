# Загружаем необходимые модули и функции
import logging
from json import JSONDecodeError
from flask import Blueprint, render_template, request
from functions import search_posts

# Инициализируем блюпринт
main_blueprint = Blueprint('main_blueprint', __name__, template_folder='templates')


@main_blueprint.route('/')
def main_index():
    """Вюьха показывает главную страницу"""
    return render_template('index.html')


@main_blueprint.route('/search/')
def main_search_page():
    """Эта вюьха показывает поиск"""
    substr = request.args.get('s')
    logging.info('Выполняется поиск')
    try:
        posts = search_posts(substr)
    except FileNotFoundError:
        return 'Файл не найден'
    except JSONDecodeError:
        return 'Невалидный файл'
    return render_template('post_list.html', posts=posts, substr=substr)
