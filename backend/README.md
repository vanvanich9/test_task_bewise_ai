# Пошаговая инструкция настройки и запуска веб-приложения

### Установка
1. Все приложение развернуто в контейнерах Docker, устананавливаем его: [Ubuntu](https://docs.docker.com/engine/install/ubuntu/), [Linux (Docker Desktop)](https://docs.docker.com/desktop/install/linux-install/), [Mac OS (Docker Desktop)](https://docs.docker.com/desktop/install/mac-install/), [Windows (Docker Desktop)](https://docs.docker.com/desktop/install/windows-install/)
2. Все эти контейнеры запускаются в надстройке `docker compose`, установим также его: [Плагин (для Ubuntu)](https://docs.docker.com/compose/install/linux/#install-using-the-repository), для Docker Desktop его устанавливать не требуется, он уже встроен.
3. Для дальнейшей работы удобнее всего склонировать репозиторий, перед этим необходимо [установить git на компьютер](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
4. Клонируем репозиторий с помощью следующей команды в терминале/консоле: git clone https://github.com/vanvanich9/test_task_bewise_ai.git (перед этим перейдите в путь, в который хотите склонировать репозиторий)

### Настройка

1. Создайте .env файл (файл окружения)
2. Добавьте в него переменные окружения в таком же формате, как описано в .env.example

### Запуск

1. Перейдите в папку backend: `cd backend`
2. Скрипт для запуска docker compose прописан в run.sh файле, выставите ему разрешения: `chmod 777 run.sh` (для Windows пропустить этот ход)
3. Запускаем `run.sh`. После этого на адресе 127.0.0.1 (для Linux и Mac OS доступен еще 0.0.0.0) под портом 5432 будет запущена PostgreSQL, а под 4567 ASGI сервер.

Чтобы завершить работу, необходимо нажать `Control + C`

### Примеры POST-запроса

<i>Request</i>

    POST http://0.0.0.0:4567/api/questions/add
    questions_num=5

<i>Response</i>

    {
        "id": 100538,
        "question": "Gunmen after this South American dictator in 1986 used rockets, bazookas, rifles & grenades--& missed!",
        "answer": "Pinochet",
        "created_at": "2022-12-30T19:27:09.325000",
        "updated_at": "2022-12-30T19:27:09.325000"
    }

<i>Request</i>

    POST http://0.0.0.0:4567/api/questions/add
    questions_num=0

<i>Response</i>

    {}
