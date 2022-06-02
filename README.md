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

`cd app`, `docker build -t app .`, `cd ..`, `cd Yolov5_DeepSort_OSNet`, `docker build -t deepsort .`

3. Поочерёдно написать комманды из `app_start.txt`, `conventer start.txt`, `trasfer start.txt`, `autobd.txt` в разные терминалы
4. Зайти на `127.0.0.1:8080`

## Weights

Изначально используются веса для трекинга масок СИЗ, вы можете изменить веса, загрузив свой файл `best.pt` в `Yolov5_DeepSort_OSNet/weights/`