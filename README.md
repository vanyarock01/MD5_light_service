# MD5_light_service
Небольшой веб-сервис, позволяющий посчитать MD5-хеш от файла, расположенного в интернете.
# Использование
API дает возможность ставить задачи на выполнение и проверять их статус

На вход POST запросу передается два аргумента: `email`(необязательный параметр) на который нужно будет отправить результат и `url` файла, для которого необходимо посчитать MD5 сумму.

Пример:

`curl -X POST -d "url=https://sample-videos.com/zip/10mb.zip&email=kutisava@gmail.com" http://127.0.0.1:5000/sumbit`

Запрос вернет нам идентификатор задачи, например:

`{"id":"70ef6d54-facc-455b-9b8c-1767e89dded6"}`

Для проверки статуса данной задачи необходимо написать GET запрос вида:

`curl -X GET http://127.0.0.1:5000/check?id=70ef6d54-facc-455b-9b8c-1767e89dded6`

Для того, что бы функционал отправки писем работал, в файле [here](./app/mail_config.py) необходимо ввести действующие данные почты.


# Запуск и настройка
* Клоним себе репозиторий

`git clone https://github.com/vanyarock01/MD5_light_service.git`

* Если пакет virtualenv не установлен - устанавливаем

`pip3 install virtualenv`

* Создаем окружение

`python3 -m venv env`
 
* Активируем его

`source env/bin/activate`

* Устанавливаем зависимости

`pip install -r requirements.txt`

* Устанавливаем и запускаем redis-server

`./run_redis.sh`

* Запускаем Celery

`./run_workers.sh`

* Запускаем сервер

`python run.py`  
