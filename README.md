# BetaSort

## Requirements

1. Docker

`https://docs.docker.com/engine/install/`

2. PostgreSQL

`https://www.postgresql.org/download/`

3. FFmpeg

`https://pypi.org/project/ffmpeg-python/`

## How to Install

1. Клонировать репозиторий

`git clone https://github.com/WASD6464/BetaSort.git`

2. Создать образы app и Yolov5:

`cd app`, `docker build -t app .`, `cd ..`, `cd Yolov5_DeepSort_OSNet`, `docker build -t deepsort .`, важно именно так назвать образы для работы

3. Поочерёдно написать комманды из `info.txt` в разные терминалы

4. Зайти на `127.0.0.1:8080`

В файле commands.txt находится пример команд для запуска докера, в зависимости от ваших папок нужно изменить путь volume у docker

## Weights

Изначально используются веса для трекинга масок СИЗ, вы можете изменить веса, загрузив свой файл `best.pt` в `Yolov5_DeepSort_OSNet/weights/`