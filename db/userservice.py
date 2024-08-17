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
    pass


# Получение пользователя по айди
def get_user_by_id(user_id):
    pass


# Удаление пользователя
def del_user_db(user_id):
    pass


# Изменение пользователя
def change_user_db(user_id, change_info, new_info):
    pass
