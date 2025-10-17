# Как запустить сервак

1. Ctrl(Cmd) + Shift + P ---> Python: Create Enviromenent...
2. Устанавливаем зависимости из `requirements.txt`
2. В консольке заходим в папку `server`
3. Пишем `python -m  unvicorn main:app --reload`
4. Переходим в 127.0.0.1:8000/docs и наблюдаем свагер
