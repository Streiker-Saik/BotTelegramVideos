# Telegram-бот для аналитики по видео на основе задач на естественном языке

Стек: SQLAlchemy, PostgreSQL, Alembic, Pydantic, Async, Aiogram, Hugging Face

## Содержание:
- [Проверить версию Python](#проверить-версию-python)
- [Установка Poetry](#установка-poetry)
- [Установка](#установка)
- [Запуск проекта](#запуск-проекта)

## Проверить версию Python:

Убедитесь, что у вас установлен Python (версия 3.x). Вы можете проверить установленную версию Python, выполнив команду:
```
python --version
```

[<- на начало](#содержание)

---
## Установка Poetry:
- Если у вас еще не установлен Poetry, вы можете установить его, выполнив следующую команду
    ```bash
    curl -sSL https://install.python-poetry.org | python3 -
    ```
- Проверить Poetry добавлен в ваш PATH.
    ```bash
    poetry --version
    ```

[<- на начало](#содержание)

---
## Установка:
- Клонируйте репозиторий:
    ```bash
    git clone git@github.com:Streiker-Saik/BotTelegramVideos.git
    ```
- Перейдите в директорию проекта:
    ```
    cd BotTelegramVideos
    ```
- ### При использовании PIP:
  - Активируйте виртуальное окружение
      ```
      python -m venv <имя_вашего окружения>
      <имя_вашего_окружения>\Scripts\activate
      ```
  - Установите зависимости
      ```bash
      pip install -r requirements.txt
      ```
- ### При использование POETRY:
  - Активируйте виртуальное окружение
      ```bash
      poetry shell
      ```
  - Установите необходимые зависимости:
      ```bash
      poetry install
      ```
  - Зайдите в файл .env.example и следуйте инструкция

[<- на начало](#содержание)

---  
## Запуск проекта:
- ### Локально:
  ```bash
  python main.py
  ```

[<- на начало](#содержание)
 
---
## Структура проекта:
```
SB1/
├── alembic/
|   ├── versions/ # пакет миграции моделей
|   |   └── ...
|   ├── __init__.py
|   ├── env.py # настройки работы alembic с проектом
|   ├── README
|   └── script.py.mako
├── app/ # приложение
|   ├── __init__.py
|   ├── bot.py # эндпоинты телеграм бота
|   ├── config.py # 
|   ├── database.py # настройки работы с БД
|   ├── llm.py # функции работы с ии
|   ├── models.py # модели обьектов
|   ├── services.py # сервис работы с БД
|   └── utils.py # дополнительный функционал
├── .env
├── .flake8 # настройка для flake8
├── .gitignore
├── alembic.ini # настройки alembic
├── main.py # точка входа
├── poetry.lock
├── pypproject.toml # зависимости для poetry
├── README.md
└── requirements.txt # зависимости для pip
```

[<- на начало](#содержание)
 
---


