from fastapi import APIRouter
from db.userservice import *

user_api = APIRouter(prefix="/user")


# Получение всех пользователей
@user_api.get('/all_user')
async def get_all_user_api():
    return get_all_users()


# Получение определнного пользователя
@user_api.get('/get_exact_user')
async def get_exact_user(user_id: int):
    user = get_user_by_id(user_id)
    return user
