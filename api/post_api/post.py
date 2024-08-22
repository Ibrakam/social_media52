from fastapi import APIRouter
from db.postservice import *

post_router = APIRouter(prefix="/post", tags=["Посты"])


@post_router.post('/add_post')
async def add_post_api(user_id: int, main_text: str):
    post = add_user_post_db(user_id=user_id, main_text=main_text)
    if post:
        return "Пост опубликован"
    return False


@post_router.get("/get_post")
async def get_post(post_id: int):
    return get_all_or_exact_post_db(post_id)


@post_router.put("/change_post")
async def change_post_api(post_id: int, new_text: str):
    return change_post_text(post_id=post_id, new_text=new_text)


@post_router.delete('/delete_post')
async def delete_post_api(post_id: int):
    return delete_post_db(post_id)


@post_router.post("/add_comment")
async def add_comment_api(user_id: int, post_id: int, text: str):
    return add_comment_db(user_id, post_id, text)


@post_router.get("/get_post_comment")
async def get_post_comment(post_id: int):
    return get_comment_by_post_id(post_id)


@post_router.delete("/delete_comment")
async def delete_comment(comment_id: int):
    return delete_comment_text(comment_id)


@post_router.post("/add_hashtag")
async def add_hashtag_api(name: str, post_id: int):
    return add_hashtag_db(name, post_id)


@post_router.get("/get_hashtag")
async def get_hashtag_by_name(name: str):
    return get_hashtag_db(name)



