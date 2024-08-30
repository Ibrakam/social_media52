#Версия пайтона
FROM python:3.12

#Устанавливаем рабочую директорию
WORKDIR /app

#Копируме файл requirements.txt
COPY requirements.txt .

#Установка всех библиотек
RUN pip install -r requirements.txt

#Копируем все наши файлы проекта
COPY . .

#Указываем порт
EXPOSE 8000

#Команда для запуска
CMD ["uvicorn", "main:app", "--reload"]