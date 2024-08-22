from db import get_db
from db.models import UserPost, Comment, Hashtag


# Добавление в бд пост
def add_user_post_db(user_id, main_text):
    with next(get_db()) as db:
        post = UserPost(user_id=user_id, main_text=main_text)
        db.add(post)
        db.commit()
        return True


# Получение определенного поста или всех
def get_all_or_exact_post_db(post_id):
    with next(get_db()) as db:
        if post_id == 0:
            all_posts = db.query(UserPost).all()
            return all_posts
        else:
            post = db.query(UserPost).filter_by(id=post_id).first()
            return post


# Изменение текста поста
def change_post_text(post_id, new_text):
    with next(get_db()) as db:
        post = db.query(UserPost).filter_by(id=post_id).first()
        if post:
            post.main_text = new_text
            db.commit()
            return "Успшно изменено"
        return False


# Удаление поста
def delete_post_db(post_id):
    with next(get_db()) as db:
        delete_post = db.query(UserPost).filter_by(id=post_id)
        if delete_post:
            delete_post.delete()
            db.commit()
            return "Успешно удалено"
        return False


# Получение комментария
# Добавление хэштега

def add_hashtag_db(name, post_id):
    with next(get_db()) as db:
        new_hashtag = Hashtag(name=name, post_id=post_id)
        db.add(new_hashtag)
        db.commit()
        return 'Успешно добавлено'


# Получение хэштегов

def get_hashtag_db(name):
    with next(get_db()) as db:
        hashtag = db.query(Hashtag).filter_by(name=name).all()
        return hashtag


def add_comment_db(user_id, post_id, text):
    with next(get_db()) as db:
        new_comment = Comment(user_id=user_id, post_id=post_id, text=text)
        db.add(new_comment)
        db.commit()
        return 'Успешно добавлено'


# Получение комментарий по пост айди

def get_comment_by_post_id(post_id):
    with next(get_db()) as db:
        comment_by_id = db.query(Comment).filter_by(post_id=post_id).all()
        return comment_by_id


def delete_comment_text(comment_id):
    with next(get_db()) as db:
        del_comment = db.query(Comment).filter_by(id=comment_id).first()
        return del_comment
