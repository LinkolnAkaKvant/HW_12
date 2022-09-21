# Загружаем необходимые функции и модули
import logging
from json import JSONDecodeError
from flask import Blueprint, render_template, request
from functions import save_picture, add_post

# Инициализируем Блюпринт
loader_blueprint = Blueprint('loader_blueprint', __name__, template_folder='templates')


@loader_blueprint.route('/post')
def create_post():
    """Вьюха показывает форму загрузки поста"""
    return render_template('post_form.html')


@loader_blueprint.route('/post', methods=["POST"])
def upload_post():
    """Эта вьюха показывает загруженый пост"""
    picture = request.files.get('picture')
    content = request.form.get('content')

    picture_url = save_picture(picture)

    if not picture_url:
        logging.info('Загруженай фвайл не картинка')
        return 'Не изображение'
    try:
        add_post({'pic': picture_url, 'content': content})
    except FileNotFoundError:
        logging.error('Файл не найден')
        return 'Файл не найден'
    except JSONDecodeError:
        return 'Невалидный файл'

    return render_template('post_uploaded.html', picture=picture_url, content=content)
