from fastapi import APIRouter, UploadFile, File
import random

photo_router = APIRouter(prefix="/photo", tags=['Фото'])


@photo_router.post("/add_photo")
async def add_photo(post_id: int, photo_file: UploadFile = File(...)):
    file_id = random.randint(1, 10000000)
    if photo_file:
        with open(f"db/photos/photo_{file_id}_{post_id}.txt", "wb") as photo:
            photo_to_save = await photo_file.read()
            photo.write(photo_to_save)
        return {"status": 1, "message": "Успешно загрузилась фотка"}
    return {"status": 0, "message": "Ошибка при загрузке"}
