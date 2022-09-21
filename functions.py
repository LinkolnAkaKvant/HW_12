# Загружаем модуль json
import json


def load_posts(path='posts.json'):
    """Функция считывает посты из файла json"""
    posts = []
    with open(path, 'r', encoding='utf-8') as file:
        posts = json.load(file)
    return posts


def search_posts(subster):
    """Функция поиска постов"""
    posts_found = []
    posts_json = load_posts()
    for post in posts_json:
        if subster in post['content']:
            posts_found.append(post)
    return posts_found


def save_picture(picture):
    """Функция сохраняет картинку и её название"""
    filename = picture.filename
    filetype = filename.split('.')[-1]
    if filetype not in ['jpg', 'jpeg', 'svg', 'png']:
        return
    picture.save(f'./uploads/images/{filename}')
    return f'/uploads/images/{filename}'


def add_post(post):
    """Функция добавления поста"""
    posts = load_posts()
    posts.append(post)
    save_posts_to_json(posts)


def save_posts_to_json(posts, path='posts.json'):
    """Функция записывает новый пост"""
    with open(path, 'w', encoding='utf-8') as file:
        json.dump(posts, file)
