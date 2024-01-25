# Иструкция по деплою:

https://www.slingacademy.com/article/deploying-fastapi-on-ubuntu-with-nginx-and-lets-encrypt/

### Настройка venv

```
sudo apt update
sudo apt install python3-venv
```

### Запуск venv

```
python3 -m venv venv
source venv/bin/activate
```

### Установка пакетов:

Сначала запускаем venv, после этого устанавливаем пакты

```
pip install -r requirements.txt
```

### Требования и подготовка к запуску:

1. PostgreSQL
2. Python 3.10
3. NGINX
4. Ubuntu Server 22.10

Переименовываем en.v в .env, прописываем данные для подключения к бд, 
генерируем секретный ключ. Сайт для генерации:

https://randomkeygen.com/

### Запуск для тестов

```
uvicorn src.main:app --reload
```

### Адрес документации
В FastApi встроен Swager. Для ипользования необходимо перейти по адресу:
http://hostname/docs

### Создание миграций:

В файле migrations/env.py

Импортируем метаданные из модели

```python
from src.auth.models import metadata as auth_meta
```

В массив target_metadata добавляем импортируем метаданные

```python
target_metadata = [auth_meta]
```

Создаем ревизию(аналог комита)

```
target_metadata = [auth_meta]
```

Проводим миграцию

```
alembic upgrade head 
```