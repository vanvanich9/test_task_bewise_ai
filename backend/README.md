# Пошаговая инструкция настройки и запуска веб-приложения

### Установка
1. Все приложение развернуто в контейнерах Docker, устананавливаем его: [Ubuntu](https://docs.docker.com/engine/install/ubuntu/), [Linux (Docker Desktop)](https://docs.docker.com/desktop/install/linux-install/), [Mac OS (Docker Desktop)](https://docs.docker.com/desktop/install/mac-install/), [Windows (Docker Desktop)](https://docs.docker.com/desktop/install/windows-install/)
2. Все эти контейнеры запускаются в надстройке `docker compose`, установим также его: [Плагин (для Ubuntu)](https://docs.docker.com/compose/install/linux/#install-using-the-repository), для Docker Desktop его устанавливать не требуется, он уже встроен.

### Настройка

1. Создайте .env файл (файл окружения)
2. Добавьте в него переменные окружения в таком же формате, как описано в .env.example
3. (Для пользователей Windows) ASGI сервер запускается на домене 0.0.0.0, который не работает на Windows. Для его смены перейдите в docker/docker-compose.yaml, контейнер application, параметр command, `--host 0.0.0.0` заменить на `--host 127.0.0.1`

### Запуск

1. Перейдите в папку backend: `cd backend`
2. Скрипт для запуска docker compose прописан в run.sh файле, выставите ему разрешения: `chmod 777`
3. Запускаем `./run.sh`. После этого на адресе 0.0.0.0 (для Windows ранее описано, как сменить на 127.0.0.1) под портом 5432 будет запущена PostgreSQL, а под 4567 ASGI сервер.

Чтобы завершить работу, необходимо нажать `Control + C`