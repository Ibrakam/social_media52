from db import get_db
from db.models import User


def register_user_db(name, email, phone_number,
                     password, user_city=None):
    with next(get_db()) as db:
        new_user = User(name=name, email=email,
                        phone_number=phone_number,
                        password=password,
                        user_city=user_city)
        db.add(new_user)
        db.commit()
        return "Успешно зарегистрировались"


# Получение всех пользователей
def get_all_users():
    with next(get_db()) as db:
        users = db.query(User).all()
        return users


# Изменение пользователя
def change_user_db(user_id, change_info, new_info):
    with next(get_db()) as db:
        user = db.query(User).filter(User.id == user_id).first()
        if user:
            if change_info == "name":
                user.name = new_info
            elif change_info == "phone_number":
                user.phone_number = new_info
            elif change_info == "email":
                user.email = new_info
            elif change_info == "city":
                user.user_city = new_info
            elif change_info == "password":
                user.password = new_info
            db.commit()
            return "Успешно изменено"
        return "Такого пользователя нету"


def get_user_by_id(user_id):
    with next(get_db()) as db:
        user = db.query(User).filter(User.id == user_id).first()
        return user


def del_user_db(user_id):
    with next(get_db()) as db:
        db.query(User).filter(User.id == user_id).delete()
        db.commit()

# def change_user_db(user_id, name=None, email=None, phone_number=None, password=None, user_city=None):
#     with next(get_db()) as db:
#         user = db.query(User).filter(User.id == user_id).first()
#         if name is not None:
#             user.name = name
#         if email is not None:
#             user.email = email
#         if phone_number is not None:
#             user.phone_number = phone_number
#         if password is not None:
#             user.password = password
#         if user_city is not None:
#             user.user_city = user_city
#         db.commit()
