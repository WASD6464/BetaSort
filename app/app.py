import os
from flask import Flask, request, redirect, url_for, render_template, Response
from werkzeug.utils import secure_filename
from time import sleep
import time


UPLOAD_FOLDER = 'upload/'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'mp4'])
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


#Разрешённые типы файлов из ALLOWED_EXTENSIONS
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


#Главная страница для скачивания файла
@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], "your_video.mp4"))#Все загруженные видео будут называться your_video.mp4
            return redirect('/track')
    return render_template('upload.html')


#Декоратор с шаблоном track.html
@app.route('/track', methods=['GET', 'POST'])
def tracking_file():
    return render_template('track.html')


#Декоратор с запуском трекинга через терминал
# @app.route('/tracking_command/', methods=['GET'])
# def tracking_command():
#     os.chdir("Yolov5_DeepSort_OSNet/")
#     os.system("python track.py --source /Users/wasd64/Desktop/Code/VVIT/DeepSort/Yolov5_DeepSort_OSNet/download_vid/your_video.mp4 --project /Users/wasd64/Desktop/Code/VVIT/DeepSort/Yolov5_DeepSort_OSNet/ --save-txt --save-vid --yolo_model /Users/wasd64/Desktop/Code/VVIT/DeepSort/Yolov5_DeepSort_OSNet/weights/best.pt --exist-ok")
#     return redirect(url_for("index"))

@app.route('/tracking_command/', methods=['GET'])
def tracking_command():
    return redirect(url_for("index"))


#вывод видео с помощью ffmpeg
def uploaded_file():
    os.system("ffplay -i complete/your_video.mp4")

#Декоратор с выводом потока из uploaded_file
@app.route('/video_feed')
def video_feed():
    return Response(uploaded_file(), mimetype='video/mp4')


#Декоратор с шаблоном videopl.html
@app.route('/index', methods=['GET', 'POST'])
def index():
    text = open("complete/your_video").read()
    return render_template('videopl.html',text=text)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)