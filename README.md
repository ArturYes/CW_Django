<h3 align="center">Проект "Сервис email-рассылок"</h3>

## О проекте

Сервис email рассылок - это сервис, на котором зарегистрированные пользователи могут создавать своих клиентов, шаблоны писем и свои рассылки. При наступлении даты отправки происходит автоматическая отправка сообщения вашим клиентам.

## Используемые технологии
- Django
- PostgreSQL
- Redis
- Celery
- Crontab


## Настройка проекта

Для работы с проектом произведите базовые настройки.

### 1. Клонирование проекта

Клонируйте репозиторий используя следующую команду.
  ```sh
  git clone https://github.com/ArturYes/CW_Django
  ```


### 2. Настройка виртуального окружения и установка зависимостей

- Инструкция для работы через виртуальное окружение - poetry: 
```text
poetry init - Создает виртуальное окружение
poetry shell - Активирует виртуальное окружение
poetry install - Устанавливает зависимости
```

- Инструкция для работы через виртуальное окружение - pip:
```text
python3 -m venv venv

source venv/bin/activate          # для Linux и Mac
venv\Scripts\activate.bat         # для Windows

pip install -r requirements.txt
```

### 3. Настройте переменные окружения:
- В корне проекта переименуйте файл .env.template в .env и введите ваши переменные окружения:
```text
# Settings Django
SECRET_KEY = <SECRET_KEY>
DEBUG = <DEBUG>
CACHE_ENABLED = <CACHE_ENABLED>
LOCATION = <LOCATION>

# Settings database
DB_ENGINE = <DB_ENGINE>
DB_NAME = <DB_NAME>
DB_HOST = <DB_HOST>
DB_USER = <DB_USER>
DB_PASSWORD = <DB_PASSWORD>
DB_PORT = <DB_PORT>

# Settings admin
ADMIN_EMAIL = admin@test.com
ADMIN_PASSWORD = qwerty123
ADMIN_USER_NAME = admin
ADMIN_FIRST_NAME = admin
ADMIN_LAST_NAME = admin
ADMIN_MIDDLE_NAME = admin

# Settings email
EMAIL_HOST_USER = <EMAIL_HOST_USER>
EMAIL_HOST_PASSWORD = <EMAIL_HOST_PASSWORD>
```
- О настройке почты smtp: 
[Настройка почтового сервиса SMTP ](https://proghunter.ru/articles/setting-up-the-smtp-mail-service-for-yandex-in-django)

### 4. Настройка БД и кэширования:

- Создать миграции:
  ```text
  python manage.py makemigrations
  ```

- Примените миграции:
  ```text
  python manage.py migrate
  ```

- Если вы хотите чистый сайт без данных и пользователей тогда применять фикстуру ниже не надо, 
для создания суперюзера введите команду: 
  ```text
  python manage.py create_su
  ```
 
- Если вы хотите использовать данные из фикстур этого проекта создавать суперюзера не надо введите команду:
  ```text
  python manage.py fill_db --table all
  ```

- Установите Redis:

  - Linux команда:
   ```text
   sudo apt install redis; 
  или 
  sudo yum install redis;
   ```

  - macOS команда:
   ```text
   brew install redis;
   ```

  Windows инструкция:
  - [Перейти на Redis docs](https://redis.io/docs/install/install-redis/install-redis-on-windows/)


## Использование

- Для запуска проекта наберите в терминале команду:
  ```text
  python manage.py runserver
  ```
  перейдите по адресу: [http://127.0.0.1:8000](http://127.0.0.1:8000)


- Для запуска автоматической отправки рассылок (происходит проверка раз в минуту), необходимо использовать команду запустив рядом с проектом в новом окне:
  ```text
  python manage.py runapscheduler
  ```

- Для ручного запуска рассылок можно использовать команду:
  ```text
  python manage.py start_mailing
  ```
